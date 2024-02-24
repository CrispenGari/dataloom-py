from dataclasses import dataclass, field
from dataloom.exceptions import UnsupportedDialectException
from sqlite3.dbapi2 import Connection
from os import PathLike
from typing_extensions import TypeAlias
from typing import Optional
from urllib.parse import urlparse, parse_qs
from dataloom.constants import instances


StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]


@dataclass(kw_only=True)
class Dialect:
    def connection_options[T](self) -> T:
        return {}


@dataclass(kw_only=True)
class PostgresDialect(Dialect):
    # "postgres://postgres:postgres@localhost:5432/db"
    connection_string: Optional[str] = field(default=None)
    database: str
    user: Optional[str] = field(default=instances["postgres"].get("user"))
    host: Optional[str] = field(default=instances["postgres"].get("host"))
    port: Optional[int] = field(default=instances["postgres"].get("port"))
    password: Optional[str] = field(default=instances["postgres"].get("user"))

    def connection_options[T](self) -> T:
        return (
            self.connection_string if self.connection_string is not None else vars(self)
        )


@dataclass(kw_only=True)
class MySQLDialect(Dialect):
    connection_string: Optional[str] = field(default=None)
    database: str
    user: Optional[str] = field(default=instances["mysql"].get("user"))
    host: Optional[str] = field(default=instances["mysql"].get("host"))
    port: Optional[int] = field(default=instances["mysql"].get("port"))
    password: Optional[str] = field(default=instances["mysql"].get("password"))

    def connection_options[T](self) -> T:
        return (
            self.connection_string if self.connection_string is not None else vars(self)
        )


@dataclass(kw_only=True)
class SQLiteDialect(Dialect):
    database: StrOrBytesPath = field(default=instances["sqlite"].get("database"))
    timeout: Optional[float] = field(default=None)
    detect_types: Optional[int] = field(default=None)
    isolation_level: Optional[str] = field(default=None)
    check_same_thread: bool = field(default=None)
    factory: type[Connection] | None = field(default=None)
    cached_statements: Optional[int] = field(default=None)
    uri: Optional[bool] = field(default=None)

    def connection_options[T](self) -> T:
        return vars(self)


@dataclass
class ConnectionOptionsFactory:
    @staticmethod
    def get_connection_options(**kwargs):
        dialect = kwargs.get("dialect")
        kwargs = {k: v for k, v in kwargs.items() if k != "dialect"}
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
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )

    @staticmethod
    def get_mysql_uri_connection_options(uri: str) -> dict:
        components = urlparse(uri)
        user = components.username
        password = components.password
        hostname = components.hostname
        port = components.port
        db = components.path.lstrip("/")

        return {
            "user": user,
            "password": password,
            "host": hostname,
            "port": port,
            "database": db,
            **parse_qs(components.query),
        }
