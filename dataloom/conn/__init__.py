from dataclasses import dataclass, field
from dataloom.exceptions import UnsupportedDialect
from sqlite3.dbapi2 import Connection
from os import PathLike
from typing_extensions import TypeAlias

StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]


@dataclass(kw_only=True)
class Dialect:
    def connection_options[T](self) -> T:
        return {}


@dataclass(kw_only=True)
class PostgresDialect(Dialect):
    # "postgres://postgres:postgres@localhost:5432/db"
    connection_string: str | None = field(default=None)
    database: str
    user: str | None = field(default="postgres")
    host: str | None = field(default="localhost")
    port: int | None = field(default=5432)
    password: str | None = field(default="postgres")

    def connection_options[T](self) -> T:
        return (
            self.connection_string if self.connection_string is not None else vars(self)
        )


@dataclass(kw_only=True)
class MySQLDialect(Dialect):
    connection_string: str | None = field(default=None)
    database: str
    user: str | None = field(default="root")
    host: str | None = field(default="localhost")
    port: int | None = field(default=3306)
    password: str | None = field(default="root")

    def connection_options[T](self) -> T:
        return (
            self.connection_string if self.connection_string is not None else vars(self)
        )


@dataclass(kw_only=True)
class SQLiteDialect(Dialect):
    database: StrOrBytesPath = field(default="users.db")
    timeout: float | None = field(default=None)
    detect_types: int | None = field(default=None)
    isolation_level: str | None = field(default=None)
    check_same_thread: bool = field(default=None)
    factory: type[Connection] | None = field(default=None)
    cached_statements: int | None = field(default=None)
    uri: bool | None = field(default=None)

    def connection_options[T](self) -> T:
        return vars(self)


@dataclass
class ConnectionOptionsFactory:
    @staticmethod
    def get_connection_options(dialect, **kwargs):
        if dialect == "postgres":
            return {
                k: v
                for k, v in PostgresDialect(**kwargs).connection_options().items()
                if v is not None
            }
        elif dialect == "sqlite":
            return SQLiteDialect(**kwargs).connection_options()
        elif dialect == "mysql":
            return {
                k: v
                for k, v in MySQLDialect(**kwargs).connection_options().items()
                if v is not None
            }
        else:
            raise UnsupportedDialect(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
