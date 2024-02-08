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


def get_create_table_params(
    model,
    dialect: DIALECT_LITERAL,
    child_alias_name: str,
    child_pk_name: str,
    child_name: str,
):
    pks = []
    user_fields = []
    predefined_fields = []
    parent_pk_name = None
    parent_pk_type = None
    n_2_n = None
    my_name = ""
    for name, field in inspect.getmembers(model):
        if isinstance(field, PrimaryKeyColumn):
            pks.append(f'"{name}"' if dialect == "postgres" else f"`{name}`")
            parent_pk_name = name
            parent_pk_type = field.sql_type(dialect=dialect)

            _values = re.sub(
                r"\s+",
                " ",
                "{_type} PRIMARY KEY {auto_increment} {unique} {nullable} {default} ".format(
                    _type=field.sql_type(dialect),
                    default=field.default_constraint,
                    nullable=field.nullable_constraint,
                    unique=field.unique_constraint,
                    auto_increment=""
                    if dialect == "postgres"
                    else "AUTO_INCREMENT"
                    if dialect == "mysql"
                    else "AUTOINCREMENT",
                ).strip(),
            )
            user_fields.append(
                (f'"{name}"' if dialect == "postgres" else f"`{name}`", _values)
            )
        elif isinstance(field, Column):
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
            user_fields.append(
                (f'"{name}"' if dialect == "postgres" else f"`{name}`", _values)
            )
        elif isinstance(field, CreatedAtColumn):
            predefined_fields.append(
                (
                    f'"{name}"' if dialect == "postgres" else f"`{name}`",
                    field.created_at,
                )
            )
        elif isinstance(field, UpdatedAtColumn):
            predefined_fields.append(
                (
                    f'"{name}"' if dialect == "postgres" else f"`{name}`",
                    field.updated_at,
                )
            )
        elif isinstance(field, ForeignKeyColumn):
            # qns:
            # 1. what is the pk in the parent table?
            # 2. what is the type of the parent table pk?
            # 3. what is the name of the parent table?
            # 4. What is the relationship type being mapped?
            pk, pk_type = field.table._get_pk_attributes(dialect=dialect)
            parent_table_name = field.table._get_table_name()
            if field.maps_to == "N-N":
                n_2_n = True
                my_name = field.table.__name__.lower()

                continue
            else:
                value = (
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
                predefined_fields.append(
                    (f'"{name}"' if dialect == "postgres" else f"`{name}`", value)
                )

    sql = None
    if n_2_n is not None:
        ref_name = (
            f'"{my_name+ '_' + child_alias_name}"'
            if dialect == "postgres"
            else f"`{my_name+ '_' + child_alias_name}`"
        )

        child_pk_column_name = (
            f'"{child_alias_name}_{child_pk_name.replace(r'"', '')}"'
            if dialect == "postgres"
            else f'`{child_alias_name}_{re.sub(r'"|`', '', child_pk_name)}`'
        )
        parent_pk_column_name = (
            f'"{my_name}_{parent_pk_name}"'
            if dialect == "postgres"
            else f"`{my_name}_{parent_pk_name}`"
        )
        sql = f"""
            CREATE TABLE IF NOT EXISTS {ref_name} (
                {child_pk_column_name} {parent_pk_type},
                {parent_pk_column_name} {parent_pk_type},
                PRIMARY KEY ({parent_pk_column_name}, {child_pk_column_name}),
                FOREIGN KEY ({parent_pk_column_name}) REFERENCES {parent_table_name}({pks[0]}),
                FOREIGN KEY ({child_pk_column_name}) REFERENCES {child_name}({child_pk_name})
            );
        """

    return pks, user_fields, predefined_fields, None  # sql if sql else None
