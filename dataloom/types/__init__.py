from typing_extensions import Literal, Any
from dataclasses import dataclass, field
from typing import Optional

OPERATOR_LITERAL = Literal["eq", "neq", "lt", "gt", "leq", "geq", "in", "notIn", "like"]
SLQ_OPERAND_LITERAL = Literal["AND", "OR"]
INCREMENT_DECREMENT_LITERAL = Literal["increment", "decrement"]
SQL_LOGGER_LITERAL = Literal["console", "file"]

CASCADE_LITERAL = Literal["NO ACTION", "CASCADE", "SET NULL"]
DIALECT_LITERAL = Literal["postgres", "mysql", "sqlite"]
RELATIONSHIP_LITERAL = Literal["1-1", "1-N", "N-1", "N-N"]
INCLUDE_LITERAL = Literal["one", "many"]


SLQ_OPERATORS = {
    "eq": "=",
    "neq": "!=",
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

AGGREGATION_LITERALS = Literal["AVG", "COUNT", "SUM", "MAX", "MIN"]


@dataclass(kw_only=True, repr=False)
class Having:
    """
    Having
    ------

    This class method is used to specify the filters to be applied on Grouped data during aggregation in dataloom.

    Parameters
    ----------
    column : str
        The name of the column to filter on.
    operator : OPERATOR_LITERAL, optional
        The operator to use for the filter. Default is "eq".
    value : Any
        The value to compare against.
    join_next_with : "AND" | "OR", optional
        The SQL operand to join the next filter with. Default is "AND".

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Filter : Class used to define filter conditions.
    ColumnValue : Class for defining column values.
    Order : Class for defining order specifications.

    Examples
    --------
    >>> from dataloom import Group, Having
    ...
    ... posts = pg_loom.find_many(
    ...     Post,
    ...     select="id",
    ...     filters=Filter(column="id", operator="gt", value=1),
    ...     group=Group(
    ...         column="id",
    ...         function="MAX",
    ...         having=Having(column="id", operator="in", value=(2, 3, 4)),
    ...         return_aggregation_column=True,
    ...    ),
    ... )
    """

    column: str = field(repr=False)
    operator: OPERATOR_LITERAL = field(repr=False, default="eq")
    value: Any = field(repr=False)
    join_next_with: Optional[SLQ_OPERAND_LITERAL] = field(default="AND")


@dataclass(repr=False, kw_only=True)
class Group:
    """
    Group
    -----

    This class is used for data aggregation and grouping data in dataloom.

    Parameters
    ----------
    column : str
        The name of the column to group by.
    function : "COUNT" | "AVG" | "SUM" | "MIN" | "MAX", optional
        The aggregation function to apply on the grouped data. Default is "COUNT".
    having : list[Having] | Having | None, optional
        Filters to apply to the grouped data. It can be a single Having object, a list of Having objects, or None to apply no filters. Default is None.
    return_aggregation_column : bool, optional
        Whether to return the aggregation column in the result. Default is False.

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Having : Class used to filter grouped data.
    ColumnValue : Class for defining column values.
    Order : Class for defining order specifications.

    Examples
    --------
    >>> from dataloom import Group, Having
    ...
    ... posts = pg_loom.find_many(
    ...     Post,
    ...     select="id",
    ...     filters=Filter(column="id", operator="gt", value=1),
    ...     group=Group(
    ...         column="id",
    ...         function="MAX",
    ...         having=Having(column="id", operator="in", value=(2, 3, 4)),
    ...         return_aggregation_column=True,
    ...    ),
    ... )
    """

    column: str = field(repr=False)
    function: AGGREGATION_LITERALS = field(default="COUNT", repr=False)
    having: Optional[list[Having] | Having] = field(default=None, repr=False)
    return_aggregation_column: Optional[bool] = field(default=False, repr=True)


@dataclass(kw_only=True, repr=False)
class Filter:
    """
    Filter
    ------

    Constructor method for the Filter class.

    Parameters
    ----------
    column : str
        The name of the column to filter on.
    operator : "eq" |"neq" |"lt" |"gt" |"leq" |"geq" |"in" |"notIn" |"like"
        The operator to use for the filter.
    value : Any
        The value to compare against.
    join_next_with : "AND" | "OR" | None, optional
        The SQL operand to join the next filter with. Default is "AND".

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Group : Class used to group data.
    Having : Class used to filter grouped data.
    ColumnValue : Class for defining column values.
    Order : Class for defining order specifications.

    Examples
    --------
    >>> from dataloom import Filter, ColumnValue, Order, User
    ...
    ... # Creating a filter for users with id equals 1 or username equals 'miller'
    ... affected_rows = loom.update_one(
    ...     User,
    ...     filters=[
    ...         Filter(column="id", value=1, operator="eq", join_next_with="OR"),
    ...         Filter(column="username", value="miller"),
    ...     ],
    ...     values=[
    ...         [
    ...             ColumnValue(name="username", value="Mario"),
    ...             ColumnValue(name="name", value="Mario"),
    ...         ]
    ...     ],
    ... )
    ... print(affected_rows)

    """

    column: str = field(repr=False)
    operator: OPERATOR_LITERAL = field(repr=False, default="eq")
    value: Any = field(repr=False)
    join_next_with: Optional[SLQ_OPERAND_LITERAL] = field(default="AND")


@dataclass(kw_only=True, repr=False)
class ColumnValue[T]:
    """
    ColumnValue
    -----------

    Constructor method for the ColumnValue class.

    Parameters
    ----------
    name : str
        The name of the column.
    value : Any
        The value to assign to the column.

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Filter : Class for defining filters.
    Order : Class for defining order specifications.
    Group : Class used to group data.
    Having : Class used to filter grouped data.

    Examples
    --------
    >>> from dataloom import ColumnValue, Filter, Order
    ...
    ... # Model definitions
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)
    ...
    ... class Post(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     title = Column(type="text", nullable=False)
    ...     content = Column(type="text", nullable=False)
    ...     userId = ForeignKeyColumn(User, maps_to="1-N", type="int", required=False, onDelete="CASCADE", onUpdate="CASCADE")
    ...
    ... # Updating the username and name columns for the user with ID 1
    ... affected_rows = loom.update_one(
    ...     User,
    ...     filters=Filter(column="id", value=1),
    ...     values=[
    ...         [
    ...             ColumnValue(name="username", value="Mario"),
    ...             ColumnValue(name="name", value="Mario"),
    ...         ]
    ...     ],
    ... )
    ... print(affected_rows)

    """

    name: str = field(repr=False)
    value: T = field(repr=False)


@dataclass(kw_only=True, repr=False)
class Order:
    """
    Order
    -----

    Constructor method for the Order class.

    Parameters
    ----------
    column : str
        The name of the column to order by.
    order : Literal['ASC', 'DESC'], optional
        The order direction. Default is "ASC" (ascending).

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Include : Class for defining included models.
    Filter : Class for defining filters.
    ColumnValue : Class for defining column values.
    Group : Class used to group data.
    Having : Class used to filter grouped data.

    Examples
    --------
    >>> from dataloom import Order, Include, Model
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)
    ...
    ... class Post(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
    ...     title = Column(type="text", nullable=False)
    ...     content = Column(type="text", nullable=False)
    ...     userId = ForeignKeyColumn(User, maps_to="1-N", type="int", required=False, onDelete="CASCADE", onUpdate="CASCADE")
    ...
    ... # Including posts for a user with ID 1 and ordering by ID in descending order
    ... # and then by createdAt in descending order
    ... users = loom.find_many(
    ...     User,
    ...     pk=1,
    ...     include=[Include(Post, limit=2, offset=0, maps_to="1-N")],
    ...     order=[Order(column="id", order="DESC"), Order(column="createdAt", order="DESC")]
    ... )

    """

    column: str = field(repr=False)
    order: Literal["ASC", "DESC"] = field(repr=False, default="ASC")


@dataclass(kw_only=True, repr=False)
class Include[Model]:
    """
    Include
    -------

    Constructor method for the Include class.

    Parameters
    ----------
    model : Model
        The model to be included when eger fetching records.
    order : list[Order], optional
        The list of order specifications for sorting the included data. Default is an empty list.
    limit : int | None, optional
        The maximum number of records to include. Default is 0 (no limit).
    offset : int | None, optional
        The number of records to skip before including. Default is 0 (no offset).
    select : list[str] | None, optional
        The list of columns to include. Default is None (include all columns).
    has : INCLUDE_LITERAL, optional
        The relationship type between the current model and the included model. Default is "many".
    include : list[Include], optional
        The extra included models.

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Order: Class for defining order specifications.
    Filter : Class for defining filters.
    ColumnValue : Class for defining column values.
    Group : Class used to group data.
    Having : Class used to filter grouped data.

    Examples
    --------
    >>> from dataloom import Include, Model, Order
    ...
    ... # get the profile and the user of that profile in one eager query.
    ... profile = mysql_loom.find_many(
    ...     instance=Profile,
    ...     include=[Include(model=User, select=["id", "username", "tokenVersion"], has="one")],
    ... )
    """

    model: Model = field(repr=False)
    order: list[Order] = field(repr=False, default_factory=list)
    limit: Optional[int] = field(default=None)
    offset: Optional[int] = field(default=None)
    select: Optional[list[str]] = field(default_factory=list)
    include: list["Include"] = field(default_factory=list)
    has: INCLUDE_LITERAL = field(default="many")


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
