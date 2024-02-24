from dataclasses import dataclass
from typing import Optional
from dataloom.exceptions import (
    InvalidColumnValuesException,
    InvalidFiltersForTableColumnException,
    PkNotDefinedException,
    TooManyPkException,
    UnsupportedDialectException,
)
from dataloom.statements.statements import (
    MySqlStatements,
    PgStatements,
    Sqlite3Statements,
)
from dataloom.types import DIALECT_LITERAL, INCREMENT_DECREMENT_LITERAL
from dataloom.utils import (
    get_formatted_query,
    get_relationships,
    get_create_table_params,
    get_table_fields,
    AlterTable,
)


@dataclass(kw_only=True)
class GetStatement[T]:
    def __init__(
        self,
        dialect: DIALECT_LITERAL,
        model: Optional[T] = None,
        table_name: Optional[str] = None,
        ignore_exists: bool = True,
    ) -> None:
        self.dialect = dialect
        self.model = model
        self.table_name = table_name
        self.ignore_exists = ignore_exists

    def _get_describe_command(
        self,
        fields: list[str] = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.DESCRIBE_TABLE_COMMAND.format(
                table_name="%s",
                fields=", ".join([f'"{f}"' for f in fields]),
                db_name="%s",
                table_schema="%s",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DESCRIBE_TABLE_COMMAND.format(
                table_name="%s",
                fields=", ".join([f"`{f}`" for f in fields]),
                db_name="%s",
            )

        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DESCRIBE_TABLE_COMMAND.format(
                table_name=self.table_name
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_insert_one_command(
        self, pk_name: str, placeholders: list[str], fields: list[str]
    ) -> tuple[Optional[str], list]:
        if self.dialect == "postgres":
            sql = PgStatements.INSERT_COMMAND_ONE.format(
                table_name=f'"{self.table_name}"',
                column_names=", ".join([f'"{f}"' for f in fields]),
                placeholder_values=", ".join(placeholders),
                pk_name=pk_name,
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
        return sql

    def _get_insert_bulk_command(
        self, placeholder_values: str, column_names: str
    ) -> str:
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
        return sql

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
    def _get_create_table_command(self) -> Optional[list[str]]:
        # is the primary key defined in this table?
        pks, user_fields, predefined_fields = get_create_table_params(
            dialect=self.dialect,
            model=self.model,
        )

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
        if self.dialect == "postgres":
            sql = (
                PgStatements.CREATE_NEW_TABLE.format(
                    table_name=f'"{self.table_name}"', fields_name=fields_name
                )
                if not self.ignore_exists
                else PgStatements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f'"{self.table_name}"', fields_name=fields_name
                )
            )

        elif self.dialect == "mysql":
            sql = (
                MySqlStatements.CREATE_NEW_TABLE.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
                if not self.ignore_exists
                else MySqlStatements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
            )

        elif self.dialect == "sqlite":
            sql = (
                Sqlite3Statements.CREATE_NEW_TABLE.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
                if not self.ignore_exists
                else Sqlite3Statements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                    table_name=f"`{self.table_name}`", fields_name=fields_name
                )
            )

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return [sql]

    def _get_select_where_command(
        self,
        placeholder_filters: list[str],
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: Optional[list[str]] = [],
        groups: list[tuple[str]] = [],
        having: list[str] = [],
    ):
        (group_columns, group_fns) = groups
        options = [
            "" if len(group_columns) == 0 else f"GROUP BY {', '.join(group_columns)}",
            "" if len(having) == 0 else f"HAVING {' '.join(having)}",
            "" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            "" if limit is None else f"LIMIT {limit}",
            "" if offset is None else f"OFFSET { offset}",
        ]
        if self.dialect == "postgres":
            sql = PgStatements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f'"{f}"' for f in fields] + group_fns),
                table_name=f'"{self.table_name}"',
                filters=" ".join(placeholder_filters),
                options=" ".join(options),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields] + group_fns),
                table_name=f"`{self.table_name}`",
                filters=" ".join(placeholder_filters),
                options=" ".join(options),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields] + group_fns),
                table_name=f"`{self.table_name}`",
                filters=" ".join(placeholder_filters),
                options=" ".join(options),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_command(
        self,
        pk_name: str,
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: Optional[list[str]] = [],
        groups: list[tuple[str]] = [],
        having: list[str] = [],
    ):
        (group_columns, group_fns) = groups
        options = [
            "" if len(group_columns) == 0 else f"GROUP BY {', '.join(group_columns)}",
            "" if len(having) == 0 else f"HAVING {' '.join(having)}",
            "" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            "" if limit is None else f"LIMIT {limit}",
            "" if offset is None else f"OFFSET { offset}",
        ]

        if self.dialect == "postgres":
            sql = PgStatements.SELECT_COMMAND.format(
                column_names=", ".join([f'"{name}"' for name in fields] + group_fns),
                table_name=f'"{self.table_name}"',
                options=" ".join(options),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields] + group_fns),
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_COMMAND.format(
                column_names=", ".join([f"`{name}`" for name in fields] + group_fns),
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_by_pk_command(
        self, pk_name: str, fields: list = [], includes: list[dict] = [], fks: dict = {}
    ):
        if len(includes) != 0:
            from_parent = len(fks) == 0
            relationships = get_relationships(
                includes=includes,
                fks=fks,
                parent_table_name=self.table_name if from_parent else None,
            )
            table_names = {
                "parent_table_name": self.table_name,
                "parent_columns": fields,
                "parent_pk_name": pk_name,
                "parent_pk": "?" if self.dialect == "sqlite" else "%s",
            }
            sql = get_formatted_query(
                dialect=self.dialect,
                table_names=table_names,
                relationships=relationships,
                from_parent=from_parent,
            )
            return sql

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

    def _get_update_by_pk_command(self, placeholders: list[str] = [], pk_name=str):
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
                placeholder_filters=" ".join(placeholder_filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.UPDATE_ONE_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                placeholder_filters=" ".join(placeholder_filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.UPDATE_ONE_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                placeholder_filters=" ".join(placeholder_filters),
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
                placeholder_filters=" ".join(placeholder_filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.UPDATE_BULK_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                placeholder_filters=" ".join(placeholder_filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.UPDATE_BULK_WHERE_COMMAND.format(
                placeholder_values=", ".join(placeholders_of_new_values),
                table_name=f"`{self.table_name}`",
                placeholder_filters=" ".join(placeholder_filters),
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

    def _get_delete_one_where_command(
        self,
        pk_name: str,
        filters: list[str] = [],
        offset: Optional[int] = None,
        orders: list[str] | None = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f'"{self.table_name}"',
                filters=" ".join(filters),
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
                filters=" ".join(filters),
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_ONE_WHERE_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
                filters=" ".join(filters),
                offset="" if offset is None else "OFFSET ?",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_first_command(
        self,
        pk_name: str,
        offset: Optional[int] = None,
        orders: list[str] | None = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_FIRST_COMMAND.format(
                pk_name=pk_name,
                table_name=f'"{self.table_name}"',
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_FIRST_COMMAND.format(
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_FIRST_COMMAND.format(
                pk_name=pk_name,
                table_name=f"`{self.table_name}`",
                offset="" if offset is None else "OFFSET ?",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_bulk_where_command(
        self,
        pk_name: str,
        filters: list[str],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: list[str] | None = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f'"{self.table_name}"',
                filters=" ".join(filters),
                pk_name=pk_name,
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f"`{self.table_name}`",
                filters=" ".join(filters),
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                pk_name=pk_name,
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )

        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=f"`{self.table_name}`",
                filters=" ".join(filters),
                limit="" if limit is None else "LIMIT ?",
                offset="" if offset is None else "OFFSET ?",
                pk_name=pk_name,
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_delete_all_command(
        self,
        pk_name: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: list[str] | None = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.DELETE_ALL_COMMAND.format(
                table_name=f'"{self.table_name}"',
                pk_name=pk_name,
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.DELETE_ALL_COMMAND.format(
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.DELETE_ALL_COMMAND.format(
                table_name=f"`{self.table_name}`",
                pk_name=pk_name,
                limit="" if limit is None else "LIMIT ?",
                offset="" if offset is None else "OFFSET ?",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_increment_decrement_command(
        self,
        operator: INCREMENT_DECREMENT_LITERAL,
        placeholders_of_column_values: list = [],
        placeholder_filters: list = [],
    ):
        if len(placeholders_of_column_values) == 0:
            raise InvalidColumnValuesException(
                f"There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table '{self.table_name}'."
            )
        if len(placeholder_filters) == 0:
            raise InvalidFiltersForTableColumnException(
                f"There are no column filter passed to perform the UPDATE ONE operation or you passed filters that does not match columns in table '{self.table_name}'."
            )

        (v, placeholder) = placeholders_of_column_values[0].split("=")
        phs = "".join(
            [
                v.strip(),
                " = ",
                v.strip(),
                f" {'-' if operator == 'decrement' else '+'} ",
                placeholder,
            ]
        )
        if self.dialect == "postgres":
            sql = PgStatements.INCREMENT_DECREMENT_COMMAND.format(
                placeholder_values=", ".join([phs, *placeholders_of_column_values[1:]]),
                table_name=f'"{self.table_name}"',
                placeholder_filters=" ".join(placeholder_filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.INCREMENT_DECREMENT_COMMAND.format(
                placeholder_values=", ".join([phs, *placeholders_of_column_values[1:]]),
                table_name=f"`{self.table_name}`",
                placeholder_filters=", ".join(placeholder_filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.INCREMENT_DECREMENT_COMMAND.format(
                placeholder_values=", ".join([phs, *placeholders_of_column_values[1:]]),
                table_name=f"`{self.table_name}`",
                placeholder_filters=", ".join(placeholder_filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_child_by_pk_command(
        self,
        child_pk_name: str,
        parent_pk_name: str,
        parent_table_name: str,
        child_foreign_key_name: str,
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: list[str] = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.SELECT_CHILD_BY_PK.format(
                child_column_names=", ".join([f'"{name}"' for name in fields]),
                child_table_name=f'"{self.table_name}"',
                child_pk_name=child_pk_name,
                child_foreign_key_name=f'"{child_foreign_key_name}"',
                parent_table_name=f'"{parent_table_name}"',
                parent_pk_name=parent_pk_name,
                parent_pk="%s",
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_CHILD_BY_PK.format(
                child_column_names=", ".join([f"`{name}`" for name in fields]),
                child_table_name=f"`{self.table_name}`",
                child_pk_name=child_pk_name,
                child_foreign_key_name=f"`{child_foreign_key_name}`",
                parent_table_name=f"`{parent_table_name}`",
                parent_pk_name=parent_pk_name,
                parent_pk="%s",
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_CHILD_BY_PK.format(
                child_column_names=", ".join([f"`{name}`" for name in fields]),
                child_table_name=f"`{self.table_name}`",
                child_pk_name=child_pk_name,
                child_foreign_key_name=f"`{child_foreign_key_name}`",
                parent_table_name=f"`{parent_table_name}`",
                parent_pk_name=parent_pk_name,
                parent_pk="?",
                limit="" if limit is None else "LIMIT ?",
                offset="" if offset is None else "OFFSET ?",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_select_parent_by_pk_stm(
        self,
        child_pk_name: str,
        child_table_name: str,
        parent_fk_name: str,
        fields: list = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: list[str] = [],
    ):
        if self.dialect == "postgres":
            sql = PgStatements.SELECT_PARENT_BY_PK.format(
                parent_column_names=", ".join([f'"{name}"' for name in fields]),
                parent_table_name=f'"{self.table_name}"',
                parent_fk_name=f'"{parent_fk_name}"',
                child_table_name=f'"{child_table_name}"',
                child_pk_name=child_pk_name,
                child_pk="%s",
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.SELECT_PARENT_BY_PK.format(
                parent_column_names=", ".join([f"`{name}`" for name in fields]),
                parent_table_name=f"`{self.table_name}`",
                parent_fk_name=f"`{parent_fk_name}`",
                child_table_name=f"`{child_table_name}`",
                child_pk_name=child_pk_name,
                child_pk="%s",
                limit="" if limit is None else "LIMIT %s",
                offset="" if offset is None else "OFFSET %s",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_PARENT_BY_PK.format(
                parent_column_names=", ".join([f"`{name}`" for name in fields]),
                parent_table_name=f"`{self.table_name}`",
                parent_fk_name=f"`{parent_fk_name}`",
                child_table_name=f"`{child_table_name}`",
                child_pk_name=child_pk_name,
                child_pk="?",
                limit="" if limit is None else "LIMIT ?",
                offset="" if offset is None else "OFFSET ?",
                orders="" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_pk_command(
        self,
        pk_name: str,
        filters: list[str],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orders: Optional[list[str]] = [],
    ):
        """
        Getting the primary key value of the table  based on filters.
        """
        options = [
            "" if len(orders) == 0 else f"ORDER BY {', '.join(orders)}",
            "" if limit is None else f"LIMIT {limit}",
            "" if offset is None else f"OFFSET { offset}",
        ]
        if self.dialect == "postgres":
            sql = PgStatements.GET_PK_COMMAND.format(
                table_name=f'"{self.table_name}"',
                options=" ".join(options),
                pk_name=pk_name,
                filters="" if len(filters) == 0 else "WHERE " + " ".join(filters),
            )
        elif self.dialect == "mysql":
            sql = MySqlStatements.GET_PK_COMMAND.format(
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
                pk_name=pk_name,
                filters="" if len(filters) == 0 else "WHERE " + " ".join(filters),
            )
        elif self.dialect == "sqlite":
            sql = Sqlite3Statements.GET_PK_COMMAND.format(
                table_name=f"`{self.table_name}`",
                options=" ".join(options),
                pk_name=pk_name,
                filters="" if len(filters) == 0 else "WHERE " + " ".join(filters),
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    def _get_alter_table_command(self, old_columns: list[str]) -> str:
        """
        1. get table columns
        2. check if is new column
        3. check if the column has been removed
        """
        pks, alterations = AlterTable(
            dialect=self.dialect, model=self.model, old_columns=old_columns
        ).get_alter_table_params

        alterations = " ".join(alterations) if self.dialect != "sqlite" else ""

        # do we have a single primary key or not?
        if len(pks) == 0:
            raise PkNotDefinedException(
                "Your table does not have a primary key column."
            )
        if len(pks) > 1:
            raise TooManyPkException(
                f"You have defined many field as primary keys which is not allowed. Fields ({', '.join(pks)}) are primary keys."
            )
        if self.dialect == "postgres":
            sql = PgStatements.ALTER_TABLE_COMMAND.format(alterations=alterations)
        elif self.dialect == "mysql":
            sql = MySqlStatements.ALTER_TABLE_COMMAND.format(
                table_name=f"`{self.table_name}`", alterations=alterations
            )

        elif self.dialect == "sqlite":
            old_table_name = f"`{self.table_name}`"
            columns, _, _, _ = get_table_fields(self.model, dialect=self.dialect)
            new_table_name = f"`{self.table_name}_new`"
            pks, user_fields, predefined_fields = get_create_table_params(
                dialect=self.dialect,
                model=self.model,
            )
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
            create_command = Sqlite3Statements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                table_name=new_table_name, fields_name=fields_name
            )

            sql = Sqlite3Statements.ALTER_TABLE_COMMAND.format(
                create_new_table_command=create_command,
                new_table_name=new_table_name,
                old_table_name=old_table_name,
                new_table_columns=", ".join(
                    [f"`{col}`" for col in old_columns if col in columns]
                ),
            )

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql
