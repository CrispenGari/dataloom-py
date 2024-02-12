from dataloom.types import (
    POSTGRES_SQL_TYPES,
    MYSQL_SQL_TYPES,
    SQLITE3_SQL_TYPES,
    MYSQL_SQL_TYPES_LITERAL,
    POSTGRES_SQL_TYPES_LITERAL,
    SQLITE3_SQL_TYPES_LITERAL,
    CASCADE_LITERAL,
    DIALECT_LITERAL,
    RELATIONSHIP_LITERAL,
)
from dataclasses import dataclass
from dataloom.exceptions import UnsupportedTypeException, UnsupportedDialectException


class CreatedAtColumn:
    """
    CreatedAtColumn
    ---------------

    Constructor method for the CreatedAtColumn class.

    Parameters
    ----------
    None

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Column : Class for defining regular columns.
    PrimaryKeyColumn : Class for defining primary key columns.
    UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
    TableColumn : Class for defining table names in the database.
    ForeignKeyColumn : Class for defining foreign key columns.

    Examples
    --------
    >>> from dataloom import CreatedAtColumn, Model, TableColumn
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)
    ...     createdAt = CreatedAtColumn()

    """

    def __init__(self):
        """
        CreatedAtColumn
        ---------------

        Constructor method for the CreatedAtColumn class.

        Parameters
        ----------
        None

        Returns
        -------
        None
            This method does not return any value.

        See Also
        --------
        Column : Class for defining regular columns.
        PrimaryKeyColumn : Class for defining primary key columns.
        UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
        TableColumn : Class for defining table names in the database.
        ForeignKeyColumn : Class for defining foreign key columns.

        Examples
        --------
        >>> from dataloom import CreatedAtColumn, Model, TableColumn
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     createdAt = CreatedAtColumn()

        """

    @property
    def created_at(self):
        return "{type} DEFAULT {value}".format(
            type=POSTGRES_SQL_TYPES["timestamp"], value="CURRENT_TIMESTAMP"
        )


class UpdatedAtColumn:
    """
    UpdatedAtColumn
    ---------------

    Constructor method for the UpdatedAtColumn class.

    Parameters
    ----------
    None

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Column : Class for defining regular columns.
    PrimaryKeyColumn : Class for defining primary key columns.
    CreatedAtColumn : Class for defining "created_at" timestamp columns.
    TableColumn : Class for defining table names in the database.
    ForeignKeyColumn : Class for defining foreign key columns.

    Examples
    --------
    >>> from dataloom import UpdatedAtColumn, Model, TableColumn
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)
    ...     updatedAt = UpdatedAtColumn()

    """

    def __init__(self):
        """
        UpdatedAtColumn
        ---------------

        Constructor method for the UpdatedAtColumn class.

        Parameters
        ----------
        None

        Returns
        -------
        None
            This method does not return any value.

        See Also
        --------
        Column : Class for defining regular columns.
        PrimaryKeyColumn : Class for defining primary key columns.
        CreatedAtColumn : Class for defining "created_at" timestamp columns.
        TableColumn : Class for defining table names in the database.
        ForeignKeyColumn : Class for defining foreign key columns.

        Examples
        --------
        >>> from dataloom import UpdatedAtColumn, Model, TableColumn
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     updatedAt = UpdatedAtColumn()

        """

    @property
    def updated_at(self):
        return "{type} DEFAULT {value}".format(
            type=POSTGRES_SQL_TYPES["timestamp"], value="CURRENT_TIMESTAMP"
        )


@dataclass(kw_only=True, repr=False)
class TableColumn:
    """
    TableColumn
    -----------

    Constructor method for the TableColumn class.

    Parameters
    ----------
    name : str
        The name of the table.

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Column : Class for defining regular columns.
    PrimaryKeyColumn : Class for defining primary key columns.
    CreatedAtColumn : Class for defining "created_at" timestamp columns.
    UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
    ForeignKeyColumn : Class for defining foreign key columns.

    Examples
    --------
    >>> from dataloom import TableColumn, Model
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")

    """

    name: str

    def __init__(self, name: str) -> None:
        """
        TableColumn
        -----------

        Constructor method for the TableColumn class.

        Parameters
        ----------
        name : str
            The name of the table.

        Returns
        -------
        None
            This method does not return any value.

        See Also
        --------
        Column : Class for defining regular columns.
        PrimaryKeyColumn : Class for defining primary key columns.
        CreatedAtColumn : Class for defining "created_at" timestamp columns.
        UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
        ForeignKeyColumn : Class for defining foreign key columns.

        Examples
        --------
        >>> from dataloom import TableColumn, Model
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")

        """
        self.name = name


class ForeignKeyColumn:
    """
    ForeignKeyColumn
    ----------------

    Constructor method for the ForeignKeyColumn class.

    Parameters
    ----------
    table : Model
        The referenced model to which the foreign key points.
    maps_to : '1-1' | '1-N' | 'N-1' | 'N-N'
        The relationship type between the current model and the referenced model. For example, "1-N" for one-to-many.
    type : str
        The SQL data type for the foreign key column.
    required : bool, optional
        Indicates whether the foreign key column is required. Default is True.
    onDelete : str, optional
        The behavior of the foreign key column on deletion of the referenced row. Default is "CASCADE".
    onUpdate : str, optional
        The behavior of the foreign key column on update of the referenced row. Default is "CASCADE".

    Returns
    -------
    None
        This method does not return any value.

    See Also
    --------
    Column : Class for defining regular columns.
    PrimaryKeyColumn : Class for defining primary key columns.
    CreatedAtColumn : Class for defining "created_at" timestamp columns.
    UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
    TableColumn : Class for defining table names in the database.

    Examples
    --------
    >>> from dataloom import ForeignKeyColumn, Model, TableColumn
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)
    ...     createdAt = CreatedAtColumn()
    ...     updatedAt = UpdatedAtColumn()
    ...
    ... class Post(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     title = Column(type="text", nullable=False)
    ...     body = Column(type="text", nullable=False)
    ...     userId = ForeignKeyColumn(
    ...         User,
    ...         maps_to="1-1",
    ...         type="int",
    ...         required=False,
    ...         onDelete="CASCADE",
    ...         onUpdate="CASCADE",
    ...     )

    """

    def __init__(
        self,
        table,
        type: MYSQL_SQL_TYPES_LITERAL
        | POSTGRES_SQL_TYPES_LITERAL
        | SQLITE3_SQL_TYPES_LITERAL,
        maps_to: RELATIONSHIP_LITERAL = "1-N",
        required: bool = True,
        onDelete: CASCADE_LITERAL = "NO ACTION",
        onUpdate: CASCADE_LITERAL = "NO ACTION",
    ):
        """
        ForeignKeyColumn
        ----------------

        Constructor method for the ForeignKeyColumn class.

        Parameters
        ----------
        table : Model
            The referenced model to which the foreign key points.
        maps_to : '1-1' | '1-N' | 'N-1' | 'N-N'
            The relationship type between the current model and the referenced model. For example, "1-N" for one-to-many.
        type : str
            The SQL data type for the foreign key column.
        required : bool, optional
            Indicates whether the foreign key column is required. Default is True.
        onDelete : str, optional
            The behavior of the foreign key column on deletion of the referenced row. Default is "CASCADE".
        onUpdate : str, optional
            The behavior of the foreign key column on update of the referenced row. Default is "CASCADE".

        Returns
        -------
        None
            This method does not return any value.

        See Also
        --------
        Column : Class for defining regular columns.
        PrimaryKeyColumn : Class for defining primary key columns.
        CreatedAtColumn : Class for defining "created_at" timestamp columns.
        UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
        TableColumn : Class for defining table names in the database.

        Examples
        --------
        >>> from dataloom import ForeignKeyColumn, Model, TableColumn
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     createdAt = CreatedAtColumn()
        ...     updatedAt = UpdatedAtColumn()
        ...
        ... class Post(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="posts")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     title = Column(type="text", nullable=False)
        ...     body = Column(type="text", nullable=False)
        ...     userId = ForeignKeyColumn(
        ...         User,
        ...         maps_to="1-1",
        ...         type="int",
        ...         required=False,
        ...         onDelete="CASCADE",
        ...         onUpdate="CASCADE",
        ...     )

        """
        self.table = table
        self.required = required
        self.onDelete = onDelete
        self.onUpdate = onUpdate
        self.type = type
        self.maps_to = maps_to

    def sql_type(self, dialect: DIALECT_LITERAL):
        if dialect == "postgres":
            if self.type in POSTGRES_SQL_TYPES:
                return (
                    f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else POSTGRES_SQL_TYPES[self.type]
                )
            else:
                types = POSTGRES_SQL_TYPES.keys()
            raise UnsupportedTypeException(
                f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
            )

        elif dialect == "mysql":
            if self.type in MYSQL_SQL_TYPES:
                if (self.unique or self.default) and self.type == "text":
                    return f"{MYSQL_SQL_TYPES['varchar']}({self.length if self.length is not None else 255})"
                return (
                    f"{MYSQL_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else MYSQL_SQL_TYPES[self.type]
                )
            else:
                types = MYSQL_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        elif dialect == "sqlite":
            if self.type in SQLITE3_SQL_TYPES:
                if self.length and self.type == "text":
                    return f"{SQLITE3_SQL_TYPES['varchar']}({self.length})"
                return (
                    f"{SQLITE3_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else SQLITE3_SQL_TYPES[self.type]
                )
            else:
                types = SQLITE3_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )


class PrimaryKeyColumn:
    """
    PrimaryKeyColumn
    --------

    Constructor method for the PrimaryKeyColumn class.

    Parameters
    ----------
    type : MYSQL_SQL_TYPES_LITERAL | POSTGRES_SQL_TYPES_LITERAL | SQLITE3_SQL_TYPES_LITERAL
        The SQL data type for the column.
    length : int | None, optional
        The length of the column for data types that require a length parameter. Default is None.
    auto_increment : bool, optional
        Indicates whether the column is auto-incrementing. Default is False.
    nullable : bool, optional
        Indicates whether the column can contain null values. Default is False.
    unique : bool, optional
        Indicates whether the column values must be unique across the table. Default is True.
    default : Any | None, optional
        The default value for the column. Default is None.

     See Also
    --------
    Column : Class for defining regular columns.
    CreatedAtColumn : Class for defining "created_at" timestamp columns.
    UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
    TableColumn : Class for defining table names in the database.
    ForeignKeyColumn : Class for defining foreign key columns.

    Examples
    --------
    >>> from dataloom import PrimaryKeyColumn, Model
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)

    """

    def __init__(
        self,
        type: MYSQL_SQL_TYPES_LITERAL
        | POSTGRES_SQL_TYPES_LITERAL
        | SQLITE3_SQL_TYPES_LITERAL,
        length: int | None = None,
        auto_increment: bool = False,
        nullable: bool = False,
        unique: bool = True,
        default=None,
    ):
        """
        PrimaryKeyColumn
        --------

        Constructor method for the PrimaryKeyColumn class.

        Parameters
        ----------
        type : MYSQL_SQL_TYPES_LITERAL | POSTGRES_SQL_TYPES_LITERAL | SQLITE3_SQL_TYPES_LITERAL
            The SQL data type for the column.
        length : int | None, optional
            The length of the column for data types that require a length parameter. Default is None.
        auto_increment : bool, optional
            Indicates whether the column is auto-incrementing. Default is False.
        nullable : bool, optional
            Indicates whether the column can contain null values. Default is False.
        unique : bool, optional
            Indicates whether the column values must be unique across the table. Default is True.
        default : Any | None, optional
            The default value for the column. Default is None.

         See Also
        --------
        Column : Class for defining regular columns.
        CreatedAtColumn : Class for defining "created_at" timestamp columns.
        UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
        TableColumn : Class for defining table names in the database.
        ForeignKeyColumn : Class for defining foreign key columns.

        Examples
        --------
        >>> from dataloom import PrimaryKeyColumn, Model
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)



        """
        self.type = type
        self.length = length
        self.auto_increment = auto_increment
        self.default = default
        self.nullable = nullable
        self.unique = unique

    @property
    def default_constraint(self):
        return (
            "DEFAULT {default}".format(
                default=(
                    self.default
                    if isinstance(self.default, bool)
                    else f"'{self.default}'"
                )
            )
            if self.default is not None
            else ""
        )

    @property
    def unique_constraint(self):
        return "UNIQUE" if self.unique else ""

    @property
    def nullable_constraint(self):
        return "NOT NULL" if not self.nullable else "NULL"

    def sql_type(self, dialect: DIALECT_LITERAL):
        if dialect == "postgres":
            if self.type in POSTGRES_SQL_TYPES:
                if self.auto_increment:
                    return "BIGSERIAL"
                return (
                    f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else POSTGRES_SQL_TYPES[self.type]
                )
            else:
                types = POSTGRES_SQL_TYPES.keys()
            raise UnsupportedTypeException(
                f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
            )

        elif dialect == "mysql":
            if self.type in MYSQL_SQL_TYPES:
                if (self.unique or self.default) and self.type == "text":
                    return f"{MYSQL_SQL_TYPES['varchar']}({self.length if self.length is not None else 255})"
                return (
                    f"{MYSQL_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else MYSQL_SQL_TYPES[self.type]
                )
            else:
                types = MYSQL_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        elif dialect == "sqlite":
            if self.type in SQLITE3_SQL_TYPES:
                return SQLITE3_SQL_TYPES[self.type]
            else:
                types = SQLITE3_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )


class Column:
    """
    Column
    ------

    Constructor method for the Column class.

    Parameters
    ----------
    type : MYSQL_SQL_TYPES_LITERAL | POSTGRES_SQL_TYPES_LITERAL
        The SQL data type for the column.
    nullable : bool, optional
        Indicates whether the column can contain null values. Default is True.
    unique : bool, optional
        Indicates whether the column values must be unique across the table. Default is False.
    length : int | None, optional
        The length of the column for data types that require a length parameter. Default is None.
    auto_increment : bool, optional
        Indicates whether the column is auto-incrementing. Default is False.
    default : Any | None, optional
        The default value for the column. Default is None.

    See Also
    --------
    PrimaryKeyColumn : Class for defining primary key columns.
    CreatedAtColumn : Class for defining "created_at" timestamp columns.
    UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
    TableColumn : Class for defining table names in the database.
    ForeignKeyColumn : Class for defining foreign key columns.

    Examples
    --------
    >>> from dataloom import Column, Model
    ...
    ... class User(Model):
    ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
    ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
    ...     name = Column(type="text", nullable=False)
    ...     username = Column(type="varchar", unique=True, length=255)

    """

    def __init__(
        self,
        type: MYSQL_SQL_TYPES_LITERAL
        | POSTGRES_SQL_TYPES_LITERAL
        | SQLITE3_SQL_TYPES_LITERAL,
        nullable: bool = True,
        unique: bool = False,
        length: int | None = None,
        auto_increment: bool = False,
        default=None,
    ):
        """
        Column
        ------

        Constructor method for the Column class.

        Parameters
        ----------
        type : MYSQL_SQL_TYPES_LITERAL | POSTGRES_SQL_TYPES_LITERAL
            The SQL data type for the column.
        nullable : bool, optional
            Indicates whether the column can contain null values. Default is True.
        unique : bool, optional
            Indicates whether the column values must be unique across the table. Default is False.
        length : int | None, optional
            The length of the column for data types that require a length parameter. Default is None.
        auto_increment : bool, optional
            Indicates whether the column is auto-incrementing. Default is False.
        default : Any | None, optional
            The default value for the column. Default is None.

        See Also
        --------
        PrimaryKeyColumn : Class for defining primary key columns.
        CreatedAtColumn : Class for defining "created_at" timestamp columns.
        UpdatedAtColumn : Class for defining "updated_at" timestamp columns.
        TableColumn : Class for defining table names in the database.
        ForeignKeyColumn : Class for defining foreign key columns.

        Examples
        --------
        >>> from dataloom import Column, Model
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type='int', auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)

        """
        self.type = type
        self.nullable = nullable
        self.unique = unique
        self.length = length
        self.auto_increment = auto_increment
        self.default = default

        self._data = {}

    def __str__(self) -> str:
        return ""

    @property
    def nullable_constraint(self):
        return "NOT NULL" if not self.nullable else ""

    @property
    def unique_constraint(self):
        return "UNIQUE" if self.unique else ""

    @property
    def default_constraint(self):
        return (
            "DEFAULT {default}".format(
                default=(
                    self.default
                    if isinstance(self.default, bool)
                    else f"'{self.default}'"
                )
            )
            if self.default is not None
            else ""
        )

    def sql_type(self, dialect: DIALECT_LITERAL):
        if dialect == "postgres":
            if self.type in POSTGRES_SQL_TYPES:
                return (
                    f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else POSTGRES_SQL_TYPES[self.type]
                )
            else:
                types = POSTGRES_SQL_TYPES.keys()
            raise UnsupportedTypeException(
                f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
            )

        elif dialect == "mysql":
            if self.type in MYSQL_SQL_TYPES:
                if (self.unique or self.default) and self.type == "text":
                    return f"{MYSQL_SQL_TYPES['varchar']}({self.length if self.length is not None else 255})"
                return (
                    f"{MYSQL_SQL_TYPES[self.type]}({self.length})"
                    if self.length
                    else MYSQL_SQL_TYPES[self.type]
                )
            else:
                types = MYSQL_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        elif dialect == "sqlite":
            if self.type in SQLITE3_SQL_TYPES:
                return SQLITE3_SQL_TYPES[self.type]
            else:
                types = SQLITE3_SQL_TYPES.keys()
                raise UnsupportedTypeException(
                    f"Unsupported column type: {self.type} for dialect '{dialect}' supported types are ({', '.join(types)})"
                )
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
