import inspect
from dataloom.constants import CURRENT_TIME_STAMP, SQLITE_CURRENT_TIME_STAMP
from dataloom.exceptions import UnknownColumnException, UnsupportedDialectException
from dataloom.columns import (
    PrimaryKeyColumn,
    TableColumn,
)
from dataloom.statements import GetStatement

from typing import Optional
from dataloom.types import (
    DIALECT_LITERAL,
    Filter,
    ColumnValue,
    INCREMENT_DECREMENT_LITERAL,
    Order,
    Include,
    Group,
)
from dataloom.utils import (
    get_table_filters,
    get_column_values,
    get_child_table_params,
    get_table_fields,
    get_groups,
    is_collection,
)


class Model:
    """
    Model
    -----

    A top-level class that all database tables inherit from.

    Attributes
    ----------
    __tablename__ : Optional[TableColumn]
        The name of the table in the database. If not specified, it defaults to None.

    Examples
    --------
    >>> from dataloom import Model, TableColumn, PrimaryKeyColumn, Column
    ... from typing import Optional
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)

    The above example shows you how you can use the model class to create a table called "users".

    """

    @classmethod
    def _create_sql(cls, dialect: DIALECT_LITERAL):
        sqls = GetStatement(
            dialect=dialect, model=cls, table_name=cls._get_table_name()
        )._get_create_table_command
        return sqls

    @classmethod
    def _alter_sql(cls, dialect: DIALECT_LITERAL, old_columns: list[str]):
        return GetStatement(
            dialect=dialect, model=cls, table_name=cls._get_table_name()
        )._get_alter_table_command(old_columns=old_columns)

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
        select: Optional[list[str] | str] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ):
        if not is_collection(select):
            select = [select]
        orders = []
        # what are the foreign keys?

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
        (
            group_fns,
            group_columns,
            having_columns,
            having_values,
            return_aggregation_column,
        ) = get_groups(
            fields=fields,
            dialect=dialect,
            select=select,
            group=group,
            table_name=cls._get_table_name(),
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
                    pk_name=pk_name,
                    groups=(group_columns, group_fns),
                    having=having_columns,
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
                    groups=(group_columns, group_fns),
                    having=having_columns,
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )

        selected = []
        if len(select) == 0:
            selected = fields + group_fns if return_aggregation_column else fields
        else:
            selected = (
                list(select) + group_fns if return_aggregation_column else list(select)
            )

        return (sql, placeholder_filter_values, selected, having_values)

    @classmethod
    def _get_select_by_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        select: Optional[list[str] | str] = [],
        include: list[Include] = [],
    ):
        if not is_collection(select):
            select = [select]

        # what is the pk name?
        # what are the foreign keys?
        includes = []
        for _include in include:
            includes.append(get_child_table_params(_include, dialect=dialect))

        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        if is_collection(select):
            for column in select:
                if column not in fields:
                    raise UnknownColumnException(
                        f'The table "{cls._get_table_name()}" does not have a column "{column}".'
                    )
        else:
            column = select
            select = [select]
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
        order: Optional[list[Order] | Order] = [],
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
        order: Optional[list[Order] | Order] = [],
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

    @classmethod
    def _get_select_child_by_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        parent_pk_name: str,
        parent_table_name: str,
        child_foreign_key_name: str,
        select: Optional[list[str] | str] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ):
        if not is_collection(select):
            select = [select]
        # what is the pk name?
        # what are the foreign keys?
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        orders = []
        if order is not None:
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
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_select_child_by_pk_command(
                fields=select if len(select) != 0 else fields,
                child_pk_name=pk_name,
                parent_pk_name=parent_pk_name,
                parent_table_name=parent_table_name,
                child_foreign_key_name=child_foreign_key_name,
                limit=limit,
                offset=offset,
                orders=orders,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, fields if len(select) == 0 else select

    @classmethod
    def _get_select_parent_by_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        child_pk_name: str,
        child_table_name: str,
        parent_fk_name: str,
        select: Optional[list[str] | str] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: list[Order] = [],
    ):
        if not is_collection(select):
            select = [select]
        # what is the pk name?
        # what are the foreign keys?
        fields, pk_name, fks, updatedAtColumName = get_table_fields(
            cls, dialect=dialect
        )
        orders = []
        if order is not None:
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
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_select_parent_by_pk_stm(
                fields=select if len(select) != 0 else fields,
                child_pk_name=child_pk_name,
                child_table_name=child_table_name,
                parent_fk_name=parent_fk_name,
                limit=limit,
                offset=offset,
                orders=orders,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, fields if len(select) == 0 else select

    @classmethod
    def _get_select_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ):
        orders = []
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

        placeholder_filters, placeholder_filter_values = get_table_filters(
            table_name=cls._get_table_name(),
            dialect=dialect,
            fields=fields,
            filters=filters,
        )
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_pk_command(
                filters=placeholder_filters,
                limit=limit,
                offset=offset,
                orders=orders,
                pk_name=pk_name,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, placeholder_filter_values
