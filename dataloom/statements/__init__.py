import inspect
import re
from dataclasses import dataclass
from typing import Optional
from dataloom.exceptions import (
    InvalidColumnValuesException,
    InvalidFiltersForTableColumnException,
    PkNotDefinedException,
    TooManyPkException,
    UnsupportedDialectException,
)
from dataloom.model import (
    Column,
    CreatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
    UpdatedAtColumn,
)
from dataloom.statements.statements import (
    MySqlStatements,
    PgStatements,
    Sqlite3Statements,
)


@dataclass(kw_only=True)
class GetStatement[T]:
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

    def _get_insert_one_command(self, pk, data) -> tuple[Optional[str], list]:
        (values, placeholders, fields) = data
        if self.dialect == "postgres":
            sql = PgStatements.INSERT_COMMAND_ONE.format(
                table_name=f'"{self.table_name}"',
                column_names=", ".join([f'"{f}"' for f in fields]),
                placeholder_values=", ".join(placeholders),
                pk=pk,
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.INSERT_COMMAND_ONE.format(
                table_name=f"`{self.table_name}`",
                column_names=", ".join([f"`{f}`" for f in fields]),
                placeholder_values=", ".join(placeholders),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.INSERT_COMMAND_ONE.format(
                table_name=f"`{self.table_name}`",
                column_names=", ".join([f"`{f}`" for f in fields]),
                placeholder_values=", ".join(placeholders),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, values

    def _get_insert_bulk_command(self, data) -> tuple[Optional[str], list]:
        placeholder_values, column_names, values = data
        if self.dialect == "postgres":
            sql = PgStatements.INSERT_COMMAND_MANY.format(
                table_name=f'"{self.table_name}"',
                column_names=column_names,
                placeholder_values=placeholder_values,
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.INSERT_COMMAND_MANY.format(
                table_name=f"`{self.table_name}`",
                column_names=column_names,
                placeholder_values=placeholder_values,
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.INSERT_COMMAND_MANY.format(
                table_name=f"`{self.table_name}`",
                column_names=column_names,
                placeholder_values=placeholder_values,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, values

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

    def _get_select_where_command(
        self,
        filters: list = [],
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        options = [
            "" if limit is None else f"LIMIT {limit}",
            "" if offset is None else f"OFFSET { offset}",
        ]

        if self.dialect == "postgres":
            sql = PgStatements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f'"{f}"' for f in fields]),
                table_name=f'"{self.table_name}"',
                filters=" AND ".join(filters),
                options=" ".join(options),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
                options=" ".join(options),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
                options=" ".join(options),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_command(
        self,
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        options = [
            "" if limit is None else f"LIMIT {limit}",
            "" if offset is None else f"OFFSET { offset}",
        ]
        if self.dialect == "postgres":
            sql = PgStatements.SELECT_COMMAND.format(
                column_names=", ".join([f'"{name}"' for name in fields]),
                table_name=f'"{self.table_name}"',
                options=" ".join(options),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_by_pk_command(self, pk_name: str, fields: list = []):
        if self.dialect == "postgres":
            sql = PgStatements.SELECT_BY_PK.format(
                column_names=", ".join([f'"{name}"' for name in fields]),
                table_name=f'"{self.table_name}"',
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_BY_PK.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_BY_PK.format(
                column_names=", ".join([f"`{name}`" for name in fields]),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="?",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_update_by_pk_command(self, placeholders: list = [], pk_name=str):
        if len(placeholders) == 0:
            raise InvalidColumnValuesException(
                f"There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table '{self.table_name}'."
            )
        if self.dialect == "postgres":
            sql = PgStatements.UPDATE_BY_PK_COMMAND.format(
                placeholder_values=", ".join(placeholders),
                table_name=f'"{self.table_name}"',
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.UPDATE_BY_PK_COMMAND.format(
                placeholder_values=", ".join(placeholders),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.UPDATE_BY_PK_COMMAND.format(
                placeholder_values=", ".join(placeholders),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="?",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_update_one_command(
        self,
        pk_name: str,
        placeholders_of_new_values: list = [],
        placeholder_filters: list = [],
    ):
        if len(placeholders_of_new_values) == 0:
            raise InvalidColumnValuesException(
                f"There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table '{self.table_name}'."
            )
        if len(placeholder_filters) == 0:
            raise InvalidFiltersForTableColumnException(
                f"There are no column filter passed to perform the UPDATE ONE operation or you passed filters that does not match columns in table '{self.table_name}'."
            )
        if self.dialect == "postgres":
            sql = PgStatements.UPDATE_ONE_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f'"{self.table_name}"',
                pk_name=pk_name,
                placeholder_filters=", ".join(placeholder_filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.UPDATE_ONE_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                placeholder_filters=", ".join(placeholder_filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.UPDATE_ONE_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                placeholder_filters=", ".join(placeholder_filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_update_bulk_command(
        self,
        placeholders_of_new_values: list = [],
        placeholder_filters: list = [],
    ):
        if len(placeholders_of_new_values) == 0:
            raise InvalidColumnValuesException(
                f"There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table '{self.table_name}'."
            )
        if len(placeholder_filters) == 0:
            raise InvalidFiltersForTableColumnException(
                f"There are no column filter passed to perform the UPDATE ONE operation or you passed filters that does not match columns in table '{self.table_name}'."
            )
        if self.dialect == "postgres":
            sql = PgStatements.UPDATE_BULK_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f'"{self.table_name}"',
                placeholder_filters=", ".join(placeholder_filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.UPDATE_BULK_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                placeholder_filters=", ".join(placeholder_filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.UPDATE_BULK_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                placeholder_filters=", ".join(placeholder_filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_by_pk_command(self, pk_name: str):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_BY_PK.format(
                table_name=f'"{self.table_name}"',
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_BY_PK.format(
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="%s",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_BY_PK.format(
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                pk="?",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_one_where_command(self, pk_name: str, filters: list = []):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f'"{self.table_name}"',
                filters=" AND ".join(filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_first_command(self, pk_name: str):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_FIRST_COMMAND.format(
                pk_name=pk_name,
                table_name=f'"{self.table_name}"',
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_FIRST_COMMAND.format(
                table_name=f"`{self.table_name}`", pk_name=pk_name
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_FIRST_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_bulk_where_command(self, filters: list = []):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f'"{self.table_name}"',
                filters=" AND ".join(filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f"`{self.table_name}`",
                filters=" AND ".join(filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_all_command(self):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_ALL_COMMAND.format(
                table_name=f'"{self.table_name}"',
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_ALL_COMMAND.format(
                table_name=f"`{self.table_name}`",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_ALL_COMMAND.format(
                table_name=f"`{self.table_name}`",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql
