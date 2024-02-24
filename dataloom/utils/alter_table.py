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
from dataloom.exceptions import InvalidDropOperationException


class AlterTable:
    def __init__(self, model, dialect: DIALECT_LITERAL, old_columns: list[str]) -> None:
        self.dialect = dialect
        self.old_columns = old_columns
        self.model = model
        self.table_name = (
            f'"{model._get_table_name()}"'
            if self.dialect == "postgres"
            else f"`{model._get_table_name()}`"
        )

    def column_alteration(self, name: str, field: Column) -> str:
        col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        _values = re.sub(
            r"\s+",
            " ",
            "{_type} {unique} {nullable} {default} ".format(
                _type=field.sql_type(self.dialect),
                unique=field.unique_constraint,
                nullable=field.nullable_constraint,
                default=field.default_constraint,
            ).strip(),
        )
        old_name = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        if name in self.old_columns:
            self.old_columns = [c for c in self.old_columns if c != name]
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} MODIFY COLUMN {col} {_values};"
            elif self.dialect == "postgres":
                default_alterations = ", ".join(
                    [
                        i
                        for i in [
                            f"ALTER COLUMN {old_name} DROP DEFAULT",
                            f"ALTER COLUMN {old_name} SET DEFAULT '{field.default}'"
                            if field.default is not None
                            else "",
                        ]
                        if bool(i)
                    ]
                )
                type_alteration = (
                    f"ALTER COLUMN {old_name} TYPE {field.sql_type(self.dialect)}"
                )
                rename_column = (
                    f"RENAME COLUMN {old_name} TO {col}" if old_name != col else ""
                )
                nullable_alteration = ", ".join(
                    [
                        i
                        for i in [
                            f"ALTER COLUMN {old_name} DROP NOT NULL",
                            f"ALTER COLUMN {old_name} SET NOT NULL"
                            if field.nullable_constraint
                            else "",
                        ]
                        if bool(i)
                    ]
                )
                unique_alterations = ", ".join(
                    [
                        i
                        for i in [
                            f'DROP CONSTRAINT IF EXISTS  "unique_{name}"',
                            f'ADD CONSTRAINT "unique_{name}" UNIQUE ({old_name})'
                            if field.unique_constraint
                            else "",
                        ]
                        if bool(i)
                    ]
                )
                all_column_alterations = ", ".join(
                    [
                        i
                        for i in [
                            type_alteration,
                            default_alterations,
                            nullable_alteration,
                            unique_alterations,
                            rename_column,
                        ]
                        if bool(i)
                    ]
                )
                alteration = f"""
                ALTER TABLE {self.table_name} {all_column_alterations};
                """
                return alteration

        else:
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} ADD {col} {_values};"
            else:
                return f"""ALTER TABLE {self.table_name} ADD COLUMN IF NOT EXISTS {col} {_values};"""

    def created_at_alterations(self, name: str, field: CreatedAtColumn) -> str:
        col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        old_name = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        if name in self.old_columns:
            self.old_columns = [c for c in self.old_columns if c != name]
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} MODIFY COLUMN {col} {field.created_at};"
            elif self.dialect == "postgres":
                return (
                    f"ALTER TABLE {self.table_name} RENAME COLUMN {old_name} TO {col};"
                    if old_name != col
                    else ""
                )
        else:
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} ADD {col} {field.created_at};"
            else:
                return f"""ALTER TABLE {self.table_name} ADD COLUMN IF NOT EXISTS {col} {field.created_at};"""

    def updated_at_alteration(self, name: str, field: UpdatedAtColumn) -> str:
        col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        old_name = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        if name in self.old_columns:
            self.old_columns = [c for c in self.old_columns if c != name]
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} MODIFY COLUMN {col} {field.updated_at};"
            elif self.dialect == "postgres":
                return (
                    f"ALTER TABLE {self.table_name} RENAME COLUMN {old_name} TO {col};"
                    if old_name != col
                    else ""
                )
        else:
            if self.dialect == "mysql":
                return f"ALTER TABLE {self.table_name} ADD {col} {field.updated_at};"
            else:
                return f"""ALTER TABLE {self.table_name} ADD COLUMN IF NOT EXISTS {col} {field.updated_at};"""

    def foreign_key_alteration(self, name: str, field: ForeignKeyColumn) -> str:
        pk, pk_type = field.table._get_pk_attributes(dialect=self.dialect)
        parent_table_name = field.table._get_table_name()
        col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        old_name = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
        _value = (
            "{pk_type} {unique} {nullable} REFERENCES {parent_table_name}({pk}) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                onDelete=field.onDelete,
                onUpdate=field.onUpdate,
                pk_type=pk_type,
                parent_table_name=f'"{parent_table_name}"'
                if self.dialect == "postgres"
                else f"`{parent_table_name}`",
                pk=f'"{pk}"' if self.dialect == "postgres" else f"`{pk}`",
                nullable="NOT NULL",
                unique="UNIQUE" if field.maps_to == "1-1" else "",
            )
            if field.required
            else "{pk_type} REFERENCES {parent_table_name}({pk}) ON DELETE SET NULL".format(
                pk_type=pk_type,
                parent_table_name=f'"{parent_table_name}"'
                if self.dialect == "postgres"
                else f"`{parent_table_name}`",
                pk=f'"{pk}"' if self.dialect == "postgres" else f"`{pk}`",
            )
        )

        if old_name in self.old_columns:
            self.old_columns = [c for c in self.old_columns if c != name]
            if self.dialect == "mysql":
                return f"""
                -- First, drop the existing foreign key constraint
                ALTER TABLE {self.table_name} DROP {col};
                
                -- Then, modify the column and add the new foreign key constraint
                ALTER TABLE {self.table_name} ADD {col} {_value};
                """
            elif self.dialect == "postgres":
                return f"RENAME COLUMN {old_name} TO {col}" if old_name != col else ""

        else:
            if self.dialect == "postgres":
                return f"ALTER TABLE {self.table_name} ADD {col} {_value};"
            else:
                return f"ALTER TABLE {self.table_name} ADD {col} {_value};"

    @property
    def get_alter_table_params(self):
        pks = []
        alterations = []
        # add or modify columns
        for name, field in inspect.getmembers(self.model):
            if isinstance(field, PrimaryKeyColumn):
                col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
                if name not in self.old_columns:
                    raise InvalidDropOperationException(
                        f"You can not alter the primary key column to '{name}' consider setting the drop option to recreate the table '{self.model._get_table_name()}'."
                    )
                self.old_columns = [c for c in self.old_columns if c != name]
                pks.append(col)
            elif isinstance(field, Column):
                alterations.append(self.column_alteration(name=name, field=field))
            elif isinstance(field, CreatedAtColumn):
                alterations.append(self.created_at_alterations(name=name, field=field))
            elif isinstance(field, UpdatedAtColumn):
                alterations.append(self.updated_at_alteration(name=name, field=field))
            elif isinstance(field, ForeignKeyColumn):
                alterations.append(self.foreign_key_alteration(name=name, field=field))

        # delete columns
        for name in self.old_columns:
            col = f'"{name}"' if self.dialect == "postgres" else f"`{name}`"
            if self.dialect == "mysql":
                alterations.append(f"ALTER TABLE {self.table_name} DROP COLUMN {col};")
            elif self.dialect == "postgres":
                alterations.append(f"ALTER TABLE {self.table_name} DROP COLUMN {col};")

        return pks, list(reversed(alterations))
