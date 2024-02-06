from typing_extensions import Literal, Any
from dataclasses import dataclass, field
from typing import Optional

OPERATOR_LITERAL = Literal["eq", "lt", "gt", "leq", "geq", "in", "notIn", "like"]
SLQ_OPERAND_LITERAL = Literal["AND", "OR"]

SLQ_OPERATORS = {
    "eq": "=",
    "lt": "<",
    "gt": ">",
    "leq": "<=",
    "geq": ">=",
    "in": "IN",
    "notIn": "NOT IN",
    "like": "LIKE",
}
SLQ_OPERAND = {
    "AND": "AND",
    "OR": "OR",
}


@dataclass(kw_only=True, repr=False)
class Filter:
    column: str = field(repr=False)
    operator: OPERATOR_LITERAL = field(repr=False, default="eq")
    value: Any = field(repr=False)
    join_next_filter_with: Optional[SLQ_OPERAND_LITERAL] = field(default="AND")


@dataclass(kw_only=True, repr=False)
class ColumnValue:
    name: str = field(repr=False)
    value: Any = field(repr=False)


@dataclass(kw_only=True, repr=False)
class Order:
    column: str = field(repr=False)
    order: Literal["ASC", "DESC"] = field(repr=False, default="ASC")


@dataclass(kw_only=True, repr=False)
class Include[Model]:
    model: Model = field(repr=False)
    order: list[Order] = field(repr=False, default_factory=list)
    limit: Optional[int] = field(default=None)
    offset: Optional[int] = field(default=None)
    select: Optional[list[str]] = field(default_factory=list())


POSTGRES_SQL_TYPES = {
    "int": "INTEGER",
    "smallint": "SMALLINT",
    "bigint": "BIGINT",
    "serial": "SERIAL",
    "bigserial": "BIGSERIAL",
    "smallserial": "SMALLSERIAL",
    "float": "REAL",
    "double precision": "DOUBLE PRECISION",
    "numeric": "NUMERIC",
    "text": "TEXT",
    "varchar": "VARCHAR",
    "char": "CHAR",
    "boolean": "BOOLEAN",
    "date": "DATE",
    "time": "TIME",
    "timestamp": "TIMESTAMP",
    "interval": "INTERVAL",
    "uuid": "UUID",
    "json": "JSON",
    "jsonb": "JSONB",
    "bytea": "BYTEA",
    "array": "ARRAY",
    "inet": "INET",
    "cidr": "CIDR",
    "macaddr": "MACADDR",
    "tsvector": "TSVECTOR",
    "point": "POINT",
    "line": "LINE",
    "lseg": "LSEG",
    "box": "BOX",
    "path": "PATH",
    "polygon": "POLYGON",
    "circle": "CIRCLE",
    "hstore": "HSTORE",
}

POSTGRES_SQL_TYPES_LITERAL = Literal[
    "int",
    "smallint",
    "bigint",
    "serial",
    "bigserial",
    "smallserial",
    "float",
    "double precision",
    "numeric",
    "text",
    "varchar",
    "char",
    "boolean",
    "date",
    "time",
    "timestamp",
    "interval",
    "uuid",
    "json",
    "jsonb",
    "bytea",
    "array",
    "inet",
    "cidr",
    "macaddr",
    "tsvector",
    "point",
    "line",
    "lseg",
    "box",
    "path",
    "polygon",
    "circle",
    "hstore",
]

MYSQL_SQL_TYPES = {
    "int": "INT",
    "smallint": "SMALLINT",
    "bigint": "BIGINT",
    "float": "FLOAT",
    "double": "DOUBLE",
    "numeric": "DECIMAL",
    "text": "TEXT",
    "varchar": "VARCHAR",
    "char": "CHAR",
    "boolean": "BOOLEAN",
    "date": "DATE",
    "time": "TIME",
    "timestamp": "TIMESTAMP",
    "json": "JSON",
    "blob": "BLOB",
}
MYSQL_SQL_TYPES_LITERAL = Literal[
    "int",
    "smallint",
    "bigint",
    "float",
    "double",
    "numeric",
    "text",
    "varchar",
    "char",
    "boolean",
    "date",
    "time",
    "timestamp",
    "json",
    "blob",
]

SQLITE3_SQL_TYPES = {
    "int": "INTEGER",
    "smallint": "SMALLINT",
    "bigint": "BIGINT",
    "float": "REAL",
    "double precision": "DOUBLE",
    "numeric": "NUMERIC",
    "text": "TEXT",
    "varchar": "VARCHAR",
    "char": "CHAR",
    "boolean": "BOOLEAN",
    "date": "DATE",
    "time": "TIME",
    "timestamp": "TIMESTAMP",
    "json": "JSON",
    "blob": "BLOB",
}

SQLITE3_SQL_TYPES_LITERAL = Literal[
    "int",
    "smallint",
    "bigint",
    "float",
    "double precision",
    "numeric",
    "text",
    "varchar",
    "char",
    "boolean",
    "date",
    "time",
    "timestamp",
    "json",
    "blob",
]


CASCADE_LITERAL = Literal["NO ACTION", "CASCADE", "SET NULL"]
DIALECT_LITERAL = Literal["postgres", "mysql", "sqlite"]
