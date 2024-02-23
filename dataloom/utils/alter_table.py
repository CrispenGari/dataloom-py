import inspect
from dataloom.columns import (
    PrimaryKeyColumn,
    ForeignKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
)
from dataloom.types import DIALECT_LITERAL
import re


def get_alter_table_params(model, dialect: DIALECT_LITERAL, old_columns: list[str]):
    pks = []
    alterations = []

    # add or modify columns
    for name, field in inspect.getmembers(model):
        if isinstance(field, PrimaryKeyColumn):
            col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            pks.append(col)
            old_columns = [c for c in old_columns if c != name]

        elif isinstance(field, Column):
            col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            _values = re.sub(
                r"\s+",
                " ",
                "{_type} {unique} {nullable} {default} ".format(
                    _type=field.sql_type(dialect),
                    unique=field.unique_constraint,
                    nullable=field.nullable_constraint,
                    default=field.default_constraint,
                ).strip(),
            )
            old_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            if name in old_columns:
                old_columns = [c for c in old_columns if c != name]
                if dialect == "mysql":
                    alterations.append(f"MODIFY COLUMN {col} {_values}")
                elif dialect == "postgres":
                    alterations.append(f"RENAME COLUMN {old_name} TO {col}")
                elif dialect == "sqlite":
                    alterations.append(f"RENAME COLUMN {old_name} TO {col}")
            else:
                if dialect == "mysql":
                    alterations.append(f"ADD {col} {_values}")
                else:
                    alterations.append(f"ADD COLUMN {col} {_values}")

        elif isinstance(field, CreatedAtColumn):
            col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            if name in old_columns:
                old_columns = [c for c in old_columns if c != name]
                if dialect == "mysql":
                    alterations.append(f"MODIFY COLUMN {col} {_values}")
                elif dialect == "postgres":
                    alterations.append(f"ALTER COLUMN {col} {_values}")
                elif dialect == "sqlite":
                    alterations.append(f"RENAME TO {col} {_values}")
            else:
                alterations.append(f"ADD {col} {field.created_at}")
        elif isinstance(field, UpdatedAtColumn):
            col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            if name in old_columns:
                old_columns = [c for c in old_columns if c != name]
                if dialect == "mysql":
                    alterations.append(f"MODIFY COLUMN {col} {_values}")
                elif dialect == "postgres":
                    alterations.append(f"ALTER COLUMN {col} {_values}")
                elif dialect == "sqlite":
                    alterations.append(f"RENAME TO {col} {_values}")
            else:
                alterations.append(f"ADD {col} {field.updated_at}")
        elif isinstance(field, ForeignKeyColumn):
            pk, pk_type = field.table._get_pk_attributes(dialect=dialect)
            parent_table_name = field.table._get_table_name()
            col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            _value = (
                "{pk_type} {unique} {nullable} REFERENCES {parent_table_name}({pk}) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                    onDelete=field.onDelete,
                    onUpdate=field.onUpdate,
                    pk_type=pk_type,
                    parent_table_name=f'"{parent_table_name}"'
                    if dialect == "postgres"
                    else f"`{parent_table_name}`",
                    pk=f'"{pk}"' if dialect == "postgres" else f"`{pk}`",
                    nullable="NOT NULL",
                    unique="UNIQUE" if field.maps_to == "1-1" else "",
                )
                if field.required
                else "{pk_type} REFERENCES {parent_table_name}({pk}) ON DELETE SET NULL".format(
                    pk_type=pk_type,
                    parent_table_name=f'"{parent_table_name}"'
                    if dialect == "postgres"
                    else f"`{parent_table_name}`",
                    pk=f'"{pk}"' if dialect == "postgres" else f"`{pk}`",
                )
            )

            if name in old_columns:
                old_columns = [c for c in old_columns if c != name]
                if dialect == "mysql":
                    alterations.append(f"MODIFY COLUMN {col} {_values}")
                elif dialect == "postgres":
                    alterations.append(f"ALTER COLUMN {col} {_values}")
                elif dialect == "sqlite":
                    alterations.append(f"RENAME TO {col} {_values}")
            else:
                alterations.append(f"ADD {col} {_value}")

    # delete columns
    for name in old_columns:
        col = f'"{name}"' if dialect == "postgres" else f"`{name}`"
        alterations.append(f"DROP COLUMN {col}")

    return pks, alterations
