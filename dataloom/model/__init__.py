from dataloom.exceptions import UnsupportedDialectException
from dataloom.statements import GetStatement
import inspect
from dataloom.model.column import (
    PrimaryKeyColumn,
    TableColumn,
)


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
    def _create_sql(cls, dialect: str, ignore_exists=True):
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
            f"{self.__name__.lower()}" if __tablename__ is None else f"{__tablename__}"
        )

    @classmethod
    def _get_pk_attributes(cls, dialect: str):
        pk = None
        pk_type = "BIGSERIAL" if dialect == "postgres" else "INT"
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                pk = name
                pk_type = field.sql_type(dialect)
        return pk, pk_type

    @classmethod
    def _drop_sql(cls, dialect: str):
        if dialect == "postgres" or "mysql" or "sqlite":
            sql = GetStatement(
                dialect=dialect, model=cls, table_name=cls._get_table_name()
            )._get_drop_table_command.format(table_name=cls._get_table_name())

        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return sql


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
