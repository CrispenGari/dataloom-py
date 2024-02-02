from dataclasses import dataclass
from dataloom.model.column import (
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    ForeignKeyColumn,
    UpdatedAtColumn,
)
import inspect
from typing import Optional
from dataloom.model.statements import *
import re
from dataloom.exceptions import (
    UnsupportedDialectException,
    PkNotDefinedException,
    TooManyPkException,
)


@dataclass(kw_only=True)
class GetStatement[T]():
    def __init__(
        self,
        dialect: str,
        model: Optional[T] = None,
        table_name: Optional[str] = None,
        ignore_exists: bool = True,
    ) -> None:
        self.dialect = dialect
        self.model = model
        self.table_name = table_name
        self.ignore_exists = ignore_exists

    @property
    def _get_drop_table_command(self) -> Optional[str]:
        if self.dialect == "postgres":
            sql = PgStatements.DROP_TABLE.format(table_name=f'"{self.table_name}"')
        elif self.dialect == "mysql":
            sql = MySqlStatements.DROP_TABLE.format(table_name=f"`{self.table_name}`")
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DROP_TABLE.format(table_name=self.table_name)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    @property
    def _get_tables_command(self) -> Optional[str]:
        if self.dialect == "postgres":
            sql = PgStatements.GET_TABLES.format(schema_name="public")
        elif self.dialect == "mysql":
            sql = MySqlStatements.GET_TABLES
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.GET_TABLES.format(type="table")
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    @property
    def _get_create_table_command(self) -> Optional[str]:
        # is the primary key defined in this table?
        pks = list()
        user_fields = list()
        predefined_fields = list()
        if self.dialect == "postgres":
            for name, field in inspect.getmembers(self.model):
                if isinstance(field, PrimaryKeyColumn):
                    pks.append(f'"{name}"')
                    _values = re.sub(
                        r"\s+",
                        " ",
                        "{_type} PRIMARY KEY {unique} {nullable} {default} ".format(
                            _type=field.sql_type(self.dialect),
                            default=field.default_constraint,
                            nullable=field.nullable_constraint,
                            unique=field.unique_constraint,
                        ).strip(),
                    )
                    user_fields.append((f'"{name}"', _values))
                elif isinstance(field, Column):
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
                    user_fields.append((f'"{name}"', _values))
                elif isinstance(field, CreatedAtColumn):
                    predefined_fields.append((f'"{name}"', field.created_at))
                elif isinstance(field, UpdatedAtColumn):
                    predefined_fields.append((f'"{name}"', field.updated_at))
                elif isinstance(field, ForeignKeyColumn):
                    # qns:
                    # 1. what is the pk in the parent table?
                    # 2. what is the type of the parent table pk?
                    # 3. what is the name of the parent table?
                    pk, pk_type = field.table._get_pk_attributes(dialect=self.dialect)
                    parent_table_name = field.table._get_table_name()

                    value = (
                        '{pk_type} {nullable} REFERENCES {parent_table_name}("{pk}") ON DELETE {onDelete} ON UPDATE {onUpdate}'.format(
                            onDelete=field.onDelete,
                            onUpdate=field.onUpdate,
                            pk_type=pk_type,
                            parent_table_name=f'"{parent_table_name}"',
                            pk=pk,
                            nullable="NOT NULL",
                        )
                        if field.required
                        else '{pk_type} REFERENCES {parent_table_name}("{pk}") ON DELETE SET NULL'.format(
                            pk_type=pk_type,
                            parent_table_name=f'"{parent_table_name}"',
                            pk=pk,
                        )
                    )
                    predefined_fields.append((f'"{name}"', value))

            # do we have a single primary key or not?
            if len(pks) == 0:
                raise PkNotDefinedException(
                    "Your table does not have a primary key column."
                )
            if len(pks) > 1:
                raise TooManyPkException(
                    f"You have defined many field as primary keys which is not allowed. Fields ({', '.join(pks)}) are primary keys."
                )
            fields = [*user_fields, *predefined_fields]
            fields_name = ", ".join(f for f in [" ".join(field) for field in fields])
            sql = (
                PgStatements.CREATE_NEW_TABLE.format(
                    table_name=f'"{self.table_name}"', fields_name=fields_name
                )
                if not self.ignore_exists
                else PgStatements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f'"{self.table_name}"', fields_name=fields_name
                )
            )
            return sql
        elif self.dialect == "mysql":
            for name, field in inspect.getmembers(self.model):
                if isinstance(field, PrimaryKeyColumn):
                    pks.append(f"`{name}`")
                    _values = re.sub(
                        r"\s+",
                        " ",
                        "{_type} PRIMARY KEY {auto_increment} {unique} {nullable} {default} ".format(
                            _type=field.sql_type(self.dialect),
                            default=field.default_constraint,
                            nullable=field.nullable_constraint,
                            unique=field.unique_constraint,
                            auto_increment=(
                                "AUTO_INCREMENT" if field.auto_increment else ""
                            ),
                        ).strip(),
                    )
                    user_fields.append((f"`{name}`", _values))
                elif isinstance(field, Column):
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
                    user_fields.append((f"`{name}`", _values))
                elif isinstance(field, CreatedAtColumn):
                    predefined_fields.append((f"`{name}`", field.created_at))
                elif isinstance(field, UpdatedAtColumn):
                    predefined_fields.append((f"`{name}`", field.updated_at))
                elif isinstance(field, ForeignKeyColumn):
                    # qns:
                    # 1. what is the pk in the parent table?
                    # 2. what is the type of the parent table pk?
                    # 3. what is the name of the parent table?
                    pk, pk_type = field.table._get_pk_attributes(dialect=self.dialect)
                    parent_table_name = field.table._get_table_name()
                    predefined_fields.append(
                        (
                            f"`{name}`",
                            "{pk_type} {nullable} REFERENCES {parent_table_name}(`{pk}`) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                                onDelete=field.onDelete,
                                onUpdate=field.onUpdate,
                                pk_type=pk_type,
                                parent_table_name=f"`{parent_table_name}`",
                                pk=pk,
                                nullable="NOT NULL" if field.required else "NULL",
                            ),
                        )
                    )

            # do we have a single primary key or not?
            if len(pks) == 0:
                raise PkNotDefinedException(
                    "Your table does not have a primary key column."
                )
            if len(pks) > 1:
                raise TooManyPkException(
                    f"You have defined many field as primary keys which is not allowed. Fields ({', '.join(pks)}) are primary keys."
                )
            fields = [*user_fields, *predefined_fields]
            fields_name = ", ".join(f for f in [" ".join(field) for field in fields])
            sql = (
                MySqlStatements.CREATE_NEW_TABLE.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
                if not self.ignore_exists
                else MySqlStatements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
            )
            return sql

        elif self.dialect == "sqlite":
            for name, field in inspect.getmembers(self.model):
                if isinstance(field, PrimaryKeyColumn):
                    pks.append(f"`{name}`")
                    _values = re.sub(
                        r"\s+",
                        " ",
                        "{_type} PRIMARY KEY {auto_increment} {unique} {nullable} {default} ".format(
                            _type=field.sql_type(self.dialect),
                            default=field.default_constraint,
                            nullable=field.nullable_constraint,
                            unique=field.unique_constraint,
                            auto_increment=(
                                "AUTOINCREMENT" if field.auto_increment else ""
                            ),
                        ).strip(),
                    )
                    user_fields.append((f"`{name}`", _values))
                elif isinstance(field, Column):
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
                    user_fields.append((f"`{name}`", _values))
                elif isinstance(field, CreatedAtColumn):
                    predefined_fields.append((f"`{name}`", field.created_at))
                elif isinstance(field, UpdatedAtColumn):
                    predefined_fields.append((f"`{name}`", field.updated_at))
                elif isinstance(field, ForeignKeyColumn):
                    # qns:
                    # 1. what is the pk in the parent table?
                    # 2. what is the type of the parent table pk?
                    # 3. what is the name of the parent table?
                    pk, pk_type = field.table._get_pk_attributes(dialect=self.dialect)
                    parent_table_name = field.table._get_table_name()
                    predefined_fields.append(
                        (
                            f"`{name}`",
                            "{pk_type} {nullable} REFERENCES {parent_table_name}(`{pk}`) ON DELETE {onDelete} ON UPDATE {onUpdate}".format(
                                onDelete=field.onDelete,
                                onUpdate=field.onUpdate,
                                pk_type=pk_type,
                                parent_table_name=f"`{parent_table_name}`",
                                pk=pk,
                                nullable="NOT NULL" if field.required else "NULL",
                            ),
                        )
                    )

            # do we have a single primary key or not?
            if len(pks) == 0:
                raise PkNotDefinedException(
                    "Your table does not have a primary key column."
                )
            if len(pks) > 1:
                raise TooManyPkException(
                    f"You have defined many field as primary keys which is not allowed. Fields ({', '.join(pks)}) are primary keys."
                )
            fields = [*user_fields, *predefined_fields]
            fields_name = ", ".join(f for f in [" ".join(field) for field in fields])
            sql = (
                MySqlStatements.CREATE_NEW_TABLE.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
                if not self.ignore_exists
                else MySqlStatements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
            )
            return sql
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
