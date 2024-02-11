import inspect
from dataloom.constants import CURRENT_TIME_STAMP, SQLITE_CURRENT_TIME_STAMP
from dataloom.exceptions import UnknownColumnException, UnsupportedDialectException
from dataloom.columns import (
    PrimaryKeyColumn,
    TableColumn,
)
from dataloom.statements import GetStatement
from dataloom.types import Order, Include
from typing import Optional
from dataloom.types import (
    DIALECT_LITERAL,
    Filter,
    ColumnValue,
    INCREMENT_DECREMENT_LITERAL,
)
from dataloom.utils import (
    get_table_filters,
    get_column_values,
    get_child_table_params,
    get_table_fields,
)


class Model:
    @classmethod
    def _create_sql(cls, dialect: DIALECT_LITERAL, ignore_exists=True):
        sqls = GetStatement(
            dialect=dialect, model=cls, table_name=cls._get_table_name()
        )._get_create_table_command
        return sqls

    @classmethod
    def _get_table_name(self):
        __tablename__ = None
        for _, field in inspect.getmembers(self):
            if isinstance(field, TableColumn):
                __tablename__ = field.name
        return (
            f"{self.__name__.lower()}"
            if __tablename__ is None
            else f"{
                __tablename__}"
        )

    @classmethod
    def _get_pk_attributes(cls, dialect: DIALECT_LITERAL):
        pk = None
        pk_type = "BIGSERIAL" if dialect == "postgres" else "INT"
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                pk = name
                pk_type = field.sql_type(dialect)
        return pk, pk_type

    @classmethod
    def _drop_sql(cls, dialect: DIALECT_LITERAL):
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_drop_table_command.format(table_name=cls._get_table_name())

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    @classmethod
    def _get_insert_one_stm(
        cls, dialect: DIALECT_LITERAL, values: list[ColumnValue] | ColumnValue
    ):
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholders, column_values, column_names = get_column_values(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            values=values,
        )
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_insert_one_command(
                fields=column_names,
                pk_name=pk_name,
                placeholders=[
                    "?" if dialect == "sqlite" else "%s" for _ in placeholders
                ],
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, column_values

    @classmethod
    def _get_insert_bulk_smt(
        cls, dialect: DIALECT_LITERAL, column_names: str, placeholder_values: str
    ):
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_insert_bulk_command(
                column_names=column_names, placeholder_values=placeholder_values
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    @classmethod
    def _get_select_where_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
        include: list[Include] = [],
    ):
        orders = []
        includes = []
        # what are the foreign keys?

        for _include in include:
            includes.append(get_child_table_params(_include, dialect=dialect))

        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        for _order in order:
            if _order.column not in fields:
                raise UnknownColumnException(
                    f'The table "{cls._get_table_name()}" does not have a column "{_order.column}".'
                )
            orders.append(
                f'"{_order.column}" {_order.order}'
                if dialect == "postgres"
                else f"`{_order.column}` {_order.order}"
            )

        for column in select:
            if column not in fields:
                raise UnknownColumnException(
                    f'The table "{cls._get_table_name()}" does not have a column "{column}".'
                )
        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )
        if dialect == "postgres" or "mysql" or "sqlite":
            if len(placeholder_filters) == 0:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_select_command(
                    fields=fields if len(select) == 0 else select,
                    limit=limit,
                    offset=offset,
                    orders=orders,
                    includes=includes,
                    fks=fks,
                    pk_name=pk_name,
                )
            else:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_select_where_command(
                    placeholder_filters=placeholder_filters,
                    fields=fields if len(select) == 0 else select,
                    limit=limit,
                    offset=offset,
                    orders=orders,
                    includes=includes,
                    fks=fks,
                    pk_name=pk_name,
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return (
            sql,
            placeholder_filter_values,
            fields if len(select) == 0 else select,
        )

    @classmethod
    def _get_select_by_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        select: list[str] = [],
        include: list[Include] = [],
    ):
        # what is the pk name?
        # what are the foreign keys?
        includes = []
        for _include in include:
            includes.append(get_child_table_params(_include, dialect=dialect))

        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        for column in select:
            if column not in fields:
                raise UnknownColumnException(
                    f'The table "{cls._get_table_name()}" does not have a column "{column}".'
                )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_select_by_pk_command(
                fields=select if len(select) != 0 else fields,
                pk_name=pk_name,
                includes=includes,
                fks=fks,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, fields if len(select) == 0 else select, includes

    @classmethod
    def _get_update_by_pk_stm(
        cls, dialect: DIALECT_LITERAL, values: ColumnValue | list[ColumnValue]
    ):
        fields = []
        # what is the pk name and updated column name?
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholders, column_values, column_names = get_column_values(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            values=values,
        )
        if updatedAtColumName is not None:
            placeholders.append(
                f'{updatedAtColumName} = {
                                '?' if dialect == 'sqlite' else '%s'}'
            )
            column_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_update_by_pk_command(placeholders=placeholders, pk_name=pk_name)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, column_values

    @classmethod
    def _get_update_one_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        # what is the pk name and updated column name?
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )

        placeholders_of_column_values, column_values, column_names = get_column_values(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            values=values,
        )
        if updatedAtColumName is not None:
            placeholders_of_column_values.append(
                f'{updatedAtColumName} = {
                                              '?' if dialect == 'sqlite' else '%s'}'
            )
            column_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_update_one_command(
                pk_name=pk_name,
                placeholders_of_new_values=placeholders_of_column_values,
                placeholder_filters=placeholder_filters,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, column_values, placeholder_filter_values

    @classmethod
    def _get_update_bulk_where_stm(
        cls, dialect: DIALECT_LITERAL, filters: dict = {}, values: dict = {}
    ):
        # what is updated column name?

        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )

        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )
        placeholders_of_column_values, column_values, column_names = get_column_values(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            values=values,
        )

        if updatedAtColumName is not None:
            placeholders_of_column_values.append(
                f'{updatedAtColumName} = {
                                              '?' if dialect == 'sqlite' else '%s'}'
            )
            column_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_update_bulk_command(
                placeholders_of_new_values=placeholders_of_column_values,
                placeholder_filters=placeholder_filters,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, column_values, placeholder_filter_values

    @classmethod
    def _get_delete_by_pk_stm(cls, dialect: DIALECT_LITERAL):
        # what is the pk name?
        pk_name = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_delete_by_pk_command(pk_name=pk_name)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql

    @classmethod
    def _get_delete_where_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )
        orders = []
        for _order in order:
            if _order.column not in fields:
                raise UnknownColumnException(
                    f'The table "{cls._get_table_name()}" does not have a column "{_order.column}".'
                )
            orders.append(
                f'"{_order.column}" {_order.order}'
                if dialect == "postgres"
                else f"`{_order.column}` {_order.order}"
            )
        if dialect == "postgres" or "mysql" or "sqlite":
            if len(placeholder_filters) == 0:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_first_command(
                    pk_name=pk_name,
                    offset=offset,
                    orders=orders,
                )
            else:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_one_where_command(
                    pk_name=pk_name,
                    filters=placeholder_filters,
                    offset=offset,
                    orders=orders,
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, placeholder_filter_values

    @classmethod
    def _get_delete_bulk_where_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )

        orders = []
        for _order in order:
            if _order.column not in fields:
                raise UnknownColumnException(
                    f'The table "{cls._get_table_name()}" does not have a column "{_order.column}".'
                )
            orders.append(
                f'"{_order.column}" {_order.order}'
                if dialect == "postgres"
                else f"`{_order.column}` {_order.order}"
            )
        if dialect == "postgres" or "mysql" or "sqlite":
            if len(placeholder_filters) == 0:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_all_command(
                    pk_name=pk_name, offset=offset, limit=limit, orders=orders
                )
            else:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_bulk_where_command(
                    filters=placeholder_filters,
                    pk_name=pk_name,
                    offset=offset,
                    limit=limit,
                    orders=orders,
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, placeholder_filter_values

    @classmethod
    def _get_increment_decrement_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]],
        value: ColumnValue[int | float],
        operator: INCREMENT_DECREMENT_LITERAL,
    ):
        # what is the pk name and updated column name?
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        placeholder_filters, filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )

        placeholders_of_column_values, column_values, column_names = get_column_values(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            values=value,
        )
        if updatedAtColumName is not None:
            placeholders_of_column_values.append(
                f'{updatedAtColumName} = {
                                              '?' if dialect == 'sqlite' else '%s'}'
            )
            column_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_increment_decrement_command(
                placeholders_of_column_values=placeholders_of_column_values,
                placeholder_filters=placeholder_filters,
                operator=operator,
            )

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, column_values, filter_values

    @classmethod
    def _get_describe_stm(cls, dialect: DIALECT_LITERAL, fields: list[str] = []):
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_describe_command(fields=fields)

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql
