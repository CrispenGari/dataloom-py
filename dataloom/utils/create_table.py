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
from dataloom.exceptions import InvalidReferenceNameException, IllegalColumnException


def get_create_table_params(
    model,
    dialect: DIALECT_LITERAL,
):
    fks = []
    pks = []
    user_fields = []
    predefined_fields = []

    for name, field in inspect.getmembers(model):
        if isinstance(field, PrimaryKeyColumn):
            pks.append(f'"{name}"' if dialect == "postgres" else f"`{name}`")
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
            # 5. Is it a self relations
            #  + in a self relation the field.table is a string that matches field.model.__class__.__name__

            if isinstance(field.table, str):
                # it is a self relation
                if field.table.lower() == model.__name__.lower():
                    pk, pk_type = model._get_pk_attributes(dialect=dialect)
                    parent_table_name = model._get_table_name()
                else:
                    raise InvalidReferenceNameException(
                        f"It seems like you are trying to create self relations on model '{ model.__name__}', however reference model is a string that does not match this model class definition signature."
                    )

            else:
                pk, pk_type = field.table._get_pk_attributes(dialect=dialect)
                parent_table_name = field.table._get_table_name()

            fks.append(f'"{name}"' if dialect == "postgres" else f"`{name}`")
            value = (
                "{pk_type} {unique} {nullable} REFERENCES {parent_table_name}({pk}) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                    onDelete=field.onDelete,
                    onUpdate=field.onUpdate,
                    pk_type=field.sql_type(dialect=dialect),
                    parent_table_name=f'"{parent_table_name}"'
                    if dialect == "postgres"
                    else f"`{parent_table_name}`",
                    pk=f'"{pk}"' if dialect == "postgres" else f"`{pk}`",
                    nullable="NOT NULL",
                    unique="UNIQUE" if field.maps_to == "1-1" else "",
                )
                if field.required
                else "{pk_type} REFERENCES {parent_table_name}({pk}) ON DELETE SET NULL".format(
                    pk_type=field.sql_type(dialect=dialect),
                    parent_table_name=f'"{parent_table_name}"'
                    if dialect == "postgres"
                    else f"`{parent_table_name}`",
                    pk=f'"{pk}"' if dialect == "postgres" else f"`{pk}`",
                )
            )
            predefined_fields.append(
                (f'"{name}"' if dialect == "postgres" else f"`{name}`", value)
            )
    return pks, fks, user_fields, predefined_fields


def get_create_reference_table_params(
    model,
    dialect: DIALECT_LITERAL,
):
    pks = []
    user_fields = []
    fks = []

    for name, field in inspect.getmembers(model):
        if isinstance(field, PrimaryKeyColumn) or isinstance(field, Column):
            raise IllegalColumnException(
                "Primary keys and columns can not be manually added in a reference table."
            )
        elif isinstance(field, CreatedAtColumn) or isinstance(field, UpdatedAtColumn):
            raise IllegalColumnException(
                "Created at and Updated at columns are not allowed in reference tables."
            )
        elif isinstance(field, ForeignKeyColumn):
            columnName = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            pk, pk_type = field.table._get_pk_attributes(dialect=dialect)
            pk = f'"{pk}"' if dialect == "postgres" else f"`{pk}`"
            table_name = (
                f'"{field.table._get_table_name()}"'
                if dialect == "postgres"
                else f"`{field.table._get_table_name()}`"
            )
            user_fields.append(
                "{columnName} {pk_type} {nullable}".format(
                    pk_type=field.sql_type(dialect=dialect),
                    nullable="NOT NULL" if field.required else "",
                    columnName=columnName,
                )
            )
            pks.append(columnName)
            fks.append(
                "FOREIGN KEY ({columnName}) REFERENCES {table_name}({pk}) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                    pk=pk,
                    table_name=table_name,
                    onDelete=field.onDelete,
                    onUpdate=field.onUpdate,
                    columnName=columnName,
                )
            )
    return pks, user_fields, fks
