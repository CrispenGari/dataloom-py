import inspect
from dataloom.constants import CURRENT_TIME_STAMP, SQLITE_CURRENT_TIME_STAMP
from dataloom.exceptions import UnknownColumnException, UnsupportedDialectException
from dataloom.columns import (
    Column,
    CreatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
    TableColumn,
    UpdatedAtColumn,
)
from dataloom.statements import GetStatement
from dataloom.types import Order, Include
from typing import Optional
from dataloom.types import DIALECT_LITERAL, Filter
from dataloom.utils import get_operator


class Model:
    def __init__(self, **args) -> None:
        self._data = {}
        for k, v in args.items():
            self._data[k] = v

    def __getattribute__(self, key: str):
        _data = object.__getattribute__(self, "_data")
        if key in _data:
            return _data[key]
        return object.__getattribute__(self, key)

    @classmethod
    def _create_sql(cls, dialect: DIALECT_LITERAL, ignore_exists=True):
        sql = GetStatement(
            dialect=dialect, model=cls, table_name=cls._get_table_name()
        )._get_create_table_command
        return sql

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

    def _get_insert_one_stm(self, dialect: DIALECT_LITERAL):
        cls = self.__class__
        fields = []
        placeholders = []
        values = []
        pk = None
        for _name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                value = getattr(self, _name)
                if not isinstance(value, Column):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
            elif isinstance(field, ForeignKeyColumn):
                value = getattr(self, _name)
                if not isinstance(value, ForeignKeyColumn):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
            elif isinstance(field, PrimaryKeyColumn):
                pk = f'"{_name}"'
                value = getattr(self, _name)
                if not isinstance(value, PrimaryKeyColumn):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
        data = (values, placeholders, fields)
        if dialect == "postgres" or "mysql" or "sqlite":
            values = GetStatement(
                dialect=dialect, model=cls, table_name=self._get_table_name()
            )._get_insert_one_command(data=data, pk=pk)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return values

    def _get_insert_bulk_attrs(self, dialect: DIALECT_LITERAL):
        cls = self.__class__
        fields = []
        placeholders = []
        values = []
        for _name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                value = getattr(self, _name)
                if not isinstance(value, Column):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
            elif isinstance(field, ForeignKeyColumn):
                value = getattr(self, _name)
                if not isinstance(value, ForeignKeyColumn):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
            elif isinstance(field, PrimaryKeyColumn):
                value = getattr(self, _name)
                if not isinstance(value, PrimaryKeyColumn):
                    fields.append(_name)
                    values.append(value)
                    placeholders.append("?" if dialect == "sqlite" else "%s")
        column_names = ", ".join(
            [f'"{f}"' if dialect == "postgres" else f"`{f}`" for f in fields]
        )
        placeholder_values = ", ".join(placeholders)
        return column_names, placeholder_values, values

    @classmethod
    def _get_insert_bulk_smt(
        cls, dialect: DIALECT_LITERAL, placeholders, columns, data
    ):
        if dialect == "postgres" or "mysql" or "sqlite":
            sql, values = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_insert_bulk_command(data=(placeholders, columns, data))
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, values

    @staticmethod
    def _get_child_table_params(include: Include):
        fields = []
        filters = []
        limit = include.limit
        offset = include.offset
        orders = None
        select = include.select
        pk_name = None
        table__name = include.model._get_table_name()
        alias = include.model.__name__.lower()
        for (
            name,
            field,
        ) in inspect.getmembers(include.model):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
                pk_name = name
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)

        for column in select:
            if column not in fields:
                raise UnknownColumnException(
                    f'The table "{table__name}" does not have a column "{column}".'
                )

        return {
            "alias": alias,
            "fields": fields,
            "filters": filters,
            "offset": offset,
            "limit": limit,
            "orders": orders,
            "select": select,
            "table": table__name,
            "pk_name": pk_name,
        }

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
        pk_name = None
        orders = list()
        fields = []
        query_params = []
        includes = []
        # what are the foreign keys?
        fks = dict()

        for _include in include:
            includes.append(cls._get_child_table_params(_include))

        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
                table_name = field.table._get_table_name()
                fks[table_name] = name
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
                pk_name = name
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)

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

        if filters is not None:
            if isinstance(filters, list):
                for idx, filter in enumerate(filters):
                    key = filter.column
                    if key not in fields:
                        raise UnknownColumnException(
                            f"Table {cls._get_table_name()} does not have column '{key}'."
                        )
                    op = get_operator(filter.operator)
                    join = (
                        ""
                        if len(filters) == idx + 1
                        else f" {filter.join_next_filter_with}"
                    )
                    _key = (
                        f'"{key}" {op} %s {join}'
                        if dialect == "postgres"
                        else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'} {join}"
                    )
                    query_params.append((_key, filter.value))
            else:
                filter = filters
                key = filter.column
                if key not in fields:
                    raise UnknownColumnException(
                        f"Table {cls._get_table_name()} does not have column '{key}'."
                    )
                op = get_operator(filter.operator)
                _key = (
                    f'"{key}" {op} %s'
                    if dialect == "postgres"
                    else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'}"
                )
                query_params.append((_key, filter.value))
        if dialect == "postgres" or "mysql" or "sqlite":
            if len(query_params) == 0:
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
                    query_params=query_params,
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
            [qp[1] for qp in query_params],
            fields if len(select) == 0 else select,
        )

    @classmethod
    def _get_select_by_pk_stm(
        cls,
        dialect: DIALECT_LITERAL,
        select: list[str] = [],
        include: list[Include] = [],
    ):
        fields = []
        # what is the pk name?
        pk_name = None
        includes = []
        # what are the foreign keys?
        fks = dict()
        for _include in include:
            includes.append(cls._get_child_table_params(_include))

        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
                table_name = field.table._get_table_name()
                fks[table_name] = name
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"

            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)

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
        return sql, fields if len(select) == 0 else select

    @classmethod
    def _get_update_by_pk_stm(
        cls, dialect: DIALECT_LITERAL, args: dict = {}, include: list[Include] = []
    ):
        fields = []
        # what is the pk name and updated column name?
        pk_name = None
        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)
                updatedAtColumName = (
                    f'"{name}"' if dialect == "postgres" else f"`{name}`"
                )
        values = list()
        placeholders = list()
        for key, value in args.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key in fields:
                placeholders.append(_key)
                values.append(value)
            else:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )

        if updatedAtColumName is not None:
            placeholders.append(
                f'{updatedAtColumName} = {
                                '?' if dialect == 'sqlite' else '%s'}'
            )
            values.append(
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
        return sql, values

    @classmethod
    def _get_update_one_stm(
        cls, dialect: DIALECT_LITERAL, filters: dict = {}, values: dict = {}
    ):
        fields = []
        # what is the pk name and updated column name?
        pk_name = None
        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)
                updatedAtColumName = (
                    f'"{name}"' if dialect == "postgres" else f"`{name}`"
                )

        new_values = []
        placeholders_of_new_values = []
        placeholder_filter_values = []
        placeholder_filters = []

        for key, value in filters.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key in fields:
                placeholder_filters.append(_key)
                placeholder_filter_values.append(value)
            else:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )
        for key, value in values.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key in fields:
                placeholders_of_new_values.append(_key)
                new_values.append(value)
            else:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )

        if updatedAtColumName is not None:
            placeholders_of_new_values.append(
                f'{updatedAtColumName} = {
                                              '?' if dialect == 'sqlite' else '%s'}'
            )
            new_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_update_one_command(
                pk_name=pk_name,
                placeholders_of_new_values=placeholders_of_new_values,
                placeholder_filters=placeholder_filters,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, new_values, placeholder_filter_values

    @classmethod
    def _get_update_bulk_where_stm(
        cls, dialect: DIALECT_LITERAL, filters: dict = {}, values: dict = {}
    ):
        fields = []
        # what is updated column name?

        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                fields.append(name)
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)
                updatedAtColumName = (
                    f'"{name}"' if dialect == "postgres" else f"`{name}`"
                )

        new_values = []
        placeholders_of_new_values = []
        placeholder_filter_values = []
        placeholder_filters = []

        for key, value in filters.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key in fields:
                placeholder_filters.append(_key)
                placeholder_filter_values.append(value)
            else:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )
        for key, value in values.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key in fields:
                placeholders_of_new_values.append(_key)
                new_values.append(value)
            else:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )

        if updatedAtColumName is not None:
            placeholders_of_new_values.append(
                f'{updatedAtColumName} = {
                                              '?' if dialect == 'sqlite' else '%s'}'
            )
            new_values.append(
                SQLITE_CURRENT_TIME_STAMP if dialect == "sqlite" else CURRENT_TIME_STAMP
            )

        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_update_bulk_command(
                placeholders_of_new_values=placeholders_of_new_values,
                placeholder_filters=placeholder_filters,
            )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, new_values, placeholder_filter_values

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
    def _get_delete_where_stm(cls, dialect: DIALECT_LITERAL, args: dict = {}):
        fields = []
        filters = []
        params = []
        pk_name = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
                fields.append(name)
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)
        for key, value in args.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key not in fields:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )
            else:
                filters.append(_key)
                params.append(value)

        if dialect == "postgres" or "mysql" or "sqlite":
            if len(filters) == 0:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_first_command(pk_name=pk_name)
            else:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_one_where_command(pk_name=pk_name, filters=filters)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, params

    @classmethod
    def _get_delete_bulk_where_stm(cls, dialect: DIALECT_LITERAL, args: dict = {}):
        fields = []
        filters = []
        params = []
        pk_name = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
            elif isinstance(field, ForeignKeyColumn):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
                fields.append(name)
            elif isinstance(field, CreatedAtColumn):
                fields.append(name)
            elif isinstance(field, UpdatedAtColumn):
                fields.append(name)
        for key, value in args.items():
            _key = (
                f'"{key}" = %s'
                if dialect == "postgres"
                else f"`{key}` = {'%s' if dialect == 'mysql' else '?'}"
            )
            if key not in fields:
                raise UnknownColumnException(
                    f"Table {cls._get_table_name()} does not have column '{key}'."
                )
            else:
                filters.append(_key)
                params.append(value)

        if dialect == "postgres" or "mysql" or "sqlite":
            if len(filters) == 0:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_all_command()
            else:
                sql = GetStatement(
                    dialect=dialect, model=cls, table_name=cls._get_table_name()
                )._get_delete_bulk_where_command(filters=filters)
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql, params


# class IModel[T](ABC):

#     @abstractmethod
#     def find_one(self, filters: dict = {}) -> T:
#         raise NotImplemented

#     @abstractmethod
#     def create(self, TModel: T) -> None:
#         raise NotImplemented


# @dataclass(kw_only=True)
# class Model[T](IModel[T]):

#     def _get_pk_attributes(self):
#         pk = None
#         pk_type = "BIGSERIAL"
#         for name, field in inspect.getmembers(self.model):
#             if isinstance(field, PrimaryKeyColumn):
#                 pk = name
#                 pk_type = field.sql_type
#         return pk, pk_type


#     def __create_table(self) -> None:
#         [dialect, cursor, _] = self.instance

#         self._execute_sql(sql)

#     def __init__[Y](self, model: T, instance: Y) -> None:
#         super().__init__()
#         self.model = model
#         self.instance = instance
#         self.logging = instance[-1]
#         self.__create_table()

#     def create(self, TModel: T) -> None:
#         pass

#     def find_one(self, filters: dict = {}) -> T:
#         pass
