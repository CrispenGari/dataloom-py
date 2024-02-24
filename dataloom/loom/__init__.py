import psycopg2
from mysql import connector
import sqlite3
from dataloom.constants import instances
from dataloom.loom.inspect import inspect
from dataloom.loom.update import update
from dataloom.loom.delete import delete
from dataloom.loom.query import query
from dataloom.loom.insert import insert
from dataloom.loom.sql import sql as SQL
from dataloom.exceptions import UnsupportedDialectException, InvalidConnectionURI
from dataloom.model import Model
from dataloom.statements import GetStatement
from dataloom.conn import ConnectionOptionsFactory
from typing import Optional, Any
from mysql.connector.pooling import PooledMySQLConnection
from sqlite3 import Connection
from mysql.connector.connection import MySQLConnectionAbstract
from dataloom.types import (
    Order,
    Include,
    DIALECT_LITERAL,
    Filter,
    ColumnValue,
    SQL_LOGGER_LITERAL,
    Group,
)
from dataloom.loom.interfaces import ILoom


class Loom(ILoom):
    """
    Loom
    --------

    This class allows you to define a loom object for your database connection.

    Parameters
    ----------
    connection_uri : str, optional
        The connection string uri that you can use to connect to the database per dialect. Examples are 'postgresql://user:password@host:port/dbname', 'sqlite:///database.db', 'mysql://user:password@host:port/dbname' for postgres, sqlite and mysql respectively.
    database : str, optional
        The name of the database to which you will connect, for PostgreSQL or MySQL, and the file name for SQLite.
    dialect : "mysql" | "postgres" | "sqlite"
        The database dialect to which you want to connect; it is required.
    user : str, optional
        The database username with which you want to connect. It defaults to the dialect's default values.
    host : str, optional
        The database host to which you will connect. It defaults to the dialect's default values.
    port : int, optional
        The database port to which you will connect. It defaults to the dialect's default values.
    password : str, optional
        The database password for the specified user. It defaults to the dialect's default value.
    sql_logger : "console" | "file"
        The default logging platform for SQL statements. It defaults to None for no logs on either file or console.
    logs_filename : str, optional
        The logging file name for SQL statement logs if the sql_logger is set to "file"; otherwise, it defaults to "dataloom.sql".

    Examples
    --------
    >>> from dataloom import Loom
    ... loom = Loom(
    ...    dialect="postgres",
    ...    database="hi",
    ...    password="root",
    ...    user="postgres",
    ...    sql_logger="console",
    ... )

    """

    def __get_database_name(self, uri: str) -> str | None:
        if self.dialect == "postgres" or self.dialect == "mysql":
            from urllib.parse import urlparse

            components = urlparse(uri)
            db = components.path.lstrip("/")
            return db
        return None

    def __init__(
        self,
        dialect: DIALECT_LITERAL,
        connection_uri: Optional[str] = None,
        database: Optional[str] = None,
        user: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        password: Optional[str] = None,
        sql_logger: Optional[SQL_LOGGER_LITERAL] = None,
        logs_filename: Optional[str] = "dataloom.sql",
    ) -> None:
        self.conn = None
        self.sql_logger = sql_logger
        self.dialect = dialect
        self.logs_filename = logs_filename
        self.connection_uri = connection_uri
        self.database = (
            database
            if self.connection_uri is None
            else self.__get_database_name(self.connection_uri)
        )

        try:
            config = instances[dialect]
        except KeyError:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )

        if dialect != "sqlite":
            self.connection_options = {
                "database": self.database,
                "dialect": self.dialect,
                "user": user if user else config["user"],
                "host": host if host else config["host"],
                "port": port if port else config["port"],
                "password": password if password else config["password"],
            }
        else:
            self.connection_options = {
                "database": self.database,
                "dialect": self.dialect,
            }
        self.sql_obj = None

    def insert_one(
        self, instance: Model, values: ColumnValue | list[ColumnValue]
    ) -> Any:
        """
        insert_one
        ----------

        Inserts a single row into the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table into which the row needs to be inserted.
        values : ColumnValue | list[ColumnValue]
            A single ColumnValue object or a list of ColumnValue objects representing the values to insert into the row.

        Returns
        -------
        rows : Any
            A primary key value of the inserted column

        See Also
        --------
        insert_bulk : Inserts multiple rows into the database.

        Examples
        --------
        >>> from dataloom import Loom, Model, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Inserting a single user
        ... values = [ColumnValue(name="name", value="Alice"), ColumnValue(name="username", value="alice123")]
        ... inserted_id = loom.insert_one(User, values)
        ... print(inserted_id)

        """
        return insert(dialect=self.dialect, _execute_sql=self._execute_sql).insert_one(
            instance=instance, values=values
        )

    def insert_bulk(self, instance: Model, values: list[list[ColumnValue]]):
        """
        insert_bulk
        -----------

        Inserts multiple rows into the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table into which the rows need to be inserted.
        values : list[list[ColumnValue]]
            A list of lists, where each inner list contains ColumnValue objects representing the values to insert into each row.

        Returns
        -------
        rows : int
            The number of rows successfully inserted.

        See Also
        --------
        insert_one : Inserts a single row into the database.

        Examples
        --------
        >>> from dataloom import Loom, Model, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False)
        ...     username = Column(type="varchar", unique=True, length=255)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Inserting multiple users
        ... values = [
        ...     [ColumnValue(name="name", value="Alice"), ColumnValue(name="username", value="alice123")],
        ...     [ColumnValue(name="name", value="Bob"), ColumnValue(name="username", value="bob456")],
        ... ]
        ... num_rows_inserted = loom.insert_bulk(User, values)
        ... print(num_rows_inserted)

        """
        return insert(dialect=self.dialect, _execute_sql=self._execute_sql).insert_bulk(
            instance=instance, values=values
        )

    def find_many(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ) -> list:
        """
        find_many
        ---------

        Retrieves multiple rows from the database based on specified filters and options.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the rows need to be retrieved.
        filters : Filter | list[Filter] | None, optional
            Filters to apply when selecting the rows. It can be a single Filter object, a list of Filter objects, or None to apply no filters. Default is None.
        select : list[str] | str, optional
            Columns to select in the query. Default is an empty list, which selects all columns.
        include : list[Include] | Include, optional
            Include instances that contain Models to include in the query (e.g., for JOIN operations).
        limit : int | None, optional
            The maximum number of rows to retrieve. Default is None.
        offset : int | None, optional
            The offset of the rows to retrieve, useful for pagination. Default is None.
        order : list[Order] | Order, optional
            The order in which to retrieve rows. Default is an empty list.
        group : list[Group] | Group, optional
            The grouping of the retrieved rows. Default is an empty list.

        Returns
        -------
        rows : list
            A list of retrieved rows.

        See Also
        --------
        find_all : Retrieves all rows from the database without applying any filters.
        find_one : Retrieves a single row from the database based on specified filters.
        find_by_pk : Retrieves a row from the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, TableColumn, PrimaryKeyColumn, Column
        >>> from typing import Optional
        >>>
        >>> class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        >>> loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        >>> # Retrieving users where id is greater than 2
        >>> users = loom.find_many(User, filters=[Filter(column="id", value=2, operator="gt")])
        >>> print(users)
        """
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_many(
            instance=instance,
            limit=limit,
            select=select,
            include=include,
            offset=offset,
            filters=filters,
            order=order,
            group=group,
        )

    def find_all(
        self,
        instance: Model,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ) -> list:
        """
        find_all
        --------

        Retrieves all rows from the database without applying any filters.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the rows need to be retrieved.
        select : list[str], optional
            Columns to select in the query. Default is an empty list, which selects all columns.
        include : list[Include], optional
            Models to include in the query (e.g., for JOIN operations).
        limit : int | None, optional
            The maximum number of rows to retrieve. Default is None.
        offset : int | None, optional
            The offset of the rows to retrieve, useful for pagination. Default is None.
        order : list[Order] | None, optional
            The order in which to retrieve rows. Default is an empty list.

        Returns
        -------
        rows : list
            A list of retrieved rows.

        See Also
        --------
        find_many : Retrieves multiple rows from the database based on specified filters and options.
        find_one : Retrieves a single row from the database based on specified filters.
        find_by_pk : Retrieves a row from the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Retrieving all users
        ... all_users = loom.find_all(User)
        ... print(all_users)

        """
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_all(
            instance=instance,
            select=select,
            include=include,
            limit=limit,
            offset=offset,
            order=order,
            group=group,
        )

    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
    ):
        """
        find_by_pk
        ----------

        Retrieves a row from the database by primary key.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the row needs to be retrieved.
        pk : Any
            The primary key value of the row to be retrieved.
        select : list[str] | str, optional
            Columns to select in the query. Default is an empty list, which selects all columns.
        include : list[Include] | Include, optional
            Models to include in the query (e.g., for JOIN operations).

        Returns
        -------
        row : dict | None
            A dictionary representing the retrieved row, or None if no row is found.

        See Also
        --------
        find_many : Retrieves multiple rows from the database based on specified filters and options.
        find_one : Retrieves a single row from the database based on specified filters.
        find_all : Retrieves all rows from the database without applying any filters.

        Examples
        --------
        >>> from dataloom import Loomdel, TableColumn, PrimaryKeyColumn, Column
        >>> from typing import Optional
        >>>
        >>> class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        >>> loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        >>> # Retrieving the user with id=1
        >>> user = loom.find_by_pk(User, pk=1)
        >>> print(user)
        """

        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_by_pk(
            include=include,
            pk=pk,
            select=select,
            instance=instance,
        )

    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        offset: Optional[int] = None,
    ):
        """
        find_one
        --------

        Retrieves a single row from the database based on specified filters.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the row needs to be retrieved.
        filters : Filter | list[Filter] | None, optional
            Filters to apply when selecting the row. It can be a single Filter object, a list of Filter objects, or None to apply no filters. Default is None.
        select : list[str] | str, optional
            Columns to select in the query. Default is an empty list, which selects all columns.
        include : list[Include] | Include, optional
            Models to include in the query (e.g., for JOIN operations).
        offset : int | None, optional
            The offset of the row to retrieve, useful for pagination. Default is None.

        Returns
        -------
        row : dict | None
            A dictionary representing the retrieved row, or None if no row is found.

        See Also
        --------
        find_many : Retrieves multiple rows from the database based on specified filters and options.
        find_all : Retrieves all rows from the database without applying any filters.
        find_by_pk : Retrieves a row from the database by primary key.

        Examples
        --------
        >>> from dataloom import Loomter, TableColumn, PrimaryKeyColumn, Column
        >>> from typing import Optional
        >>>
        >>> class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        >>> loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        >>> # Retrieving a single user based on filters
        >>> user = loom.find_one(User, filters=[Filter(column="id", value=1, operator="eq")])
        >>> print(user)
        """
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_one(
            instance=instance,
            select=select,
            filters=filters,
            offset=offset,
            include=include,
        )

    def update_by_pk(
        self, instance: Model, pk, values: ColumnValue | list[ColumnValue]
    ):
        """
        update_by_pk
        ------------

        Updates a row in the database by primary key.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table in which the row needs to be updated.
        pk : Any
            The primary key value of the row to be updated.
        values : ColumnValue | list[ColumnValue]
            The column values to be updated. It can be a single ColumnValue object or a list of ColumnValue objects.

        Returns
        -------
        affected_rows: int
            The number of rows updated.

        See Also
        --------
        decrement : Decrements the value of a column in the database.
        increment : Increments the value of a column in the database.
        update_one : Updates a single row in the database.
        update_bulk : Updates multiple rows in the database.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column, ColumnValue
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Updating the username and tokenVersion for the user with id=1
        ... num_rows_updated = loom.update_by_pk(
        ...     User,
        ...     pk=1,
        ...     values=[
        ...         ColumnValue(name="username", value="new_username"),
        ...         ColumnValue(name="tokenVersion", value=2),
        ...     ]
        ... )
        ... print(num_rows_updated)

        """
        return update(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).update_by_pk(instance=instance, pk=pk, values=values)

    def update_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ) -> int:
        """
        update_one
        ----------

        Updates a single row in the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table in which the row needs to be updated.
        filters : Filter | list[Filter] | None
            Filters to apply when selecting the row to be updated. It can be a single Filter object, a list of Filter objects, or None to apply no filters.
        values : ColumnValue | list[ColumnValue]
            The column values to be updated. It can be a single ColumnValue object or a list of ColumnValue objects.

        Returns
        -------
        affected_rows: int
            The updated row count.

        See Also
        --------
        decrement : Decrements the value of a column in the database.
        increment : Increments the value of a column in the database.
        update_bulk : Updates multiple rows in the database.
        update_by_pk : Updates a row in the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Updating the username and tokenVersion for the user where id is 1
        ... updated_row = loom.update_one(
        ...     User,
        ...     filters=[Filter(column="id", value=1, operator="eq")],
        ...     values=[
        ...         ColumnValue(name="username", value="new_username"),
        ...         ColumnValue(name="tokenVersion", value=2),
        ...     ]
        ... )
        ... print(updated_row)

        """
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).update_one(
            instance=instance, filters=filters, values=values
        )

    def update_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ) -> int:
        """
        update_bulk
        -----------

        Updates multiple rows in the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table in which the rows need to be updated.
        filters : Filter | list[Filter] | None
            Filters to apply when selecting the rows to be updated. It can be a single Filter object, a list of Filter objects, or None to apply no filters.
        values : ColumnValue | list[ColumnValue]
            The column values to be updated. It can be a single ColumnValue object or a list of ColumnValue objects.

        Returns
        -------
        affected_rows: int
            The number of rows updated.

        See Also
        --------
        decrement : Decrements the value of a column in the database.
        increment : Increments the value of a column in the database.
        update_one : Updates a single row in the database.
        update_by_pk : Updates a row in the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Updating the username for users with tokenVersion less than 2
        ... num_rows_updated = loom.update_bulk(
        ...     User,
        ...     filters=[Filter(column="tokenVersion", value=2, operator="lt")],
        ...     values=ColumnValue(name="username", value="new_username"),
        ... )
        ... print(num_rows_updated)

        """
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).update_bulk(
            instance=instance, filters=filters, values=values
        )

    def delete_by_pk(self, instance: Model, pk) -> int:
        """
        delete_by_pk
        ------------

        Deletes a row from the database by primary key.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the row needs to be deleted.
        pk : Any
            The primary key value of the row to be deleted.

        Returns
        -------
        deleted_rows: int
            The number of rows deleted (0 or 1).

        See Also
        --------
        delete_one : Deletes a single row from the database.
        delete_bulk : Deletes multiple rows from the database.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Deleting the user with id=1
        ... num_rows_deleted = loom.delete_by_pk(User, pk=1)
        ... print(num_rows_deleted)

        """
        return delete(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).delete_by_pk(instance=instance, pk=pk)

    def delete_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = [],
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ) -> int:
        """
        delete_one
        ----------

        Deletes a single row from the database based on specified filters.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the row needs to be deleted.
        filters : Filter | list[Filter] | None, optional
            Filters to apply when selecting the row to be deleted. It can be a single Filter object, a list of Filter objects, or None to apply no filters. Default is an empty list.
        offset : int | None, optional
            The offset of the row to delete, useful for pagination. Default is None.
        order : list[Order] | None, optional
            The order in which to delete rows. Default is an empty list.

        Returns
        -------
        deleted_rows : int
            The number of rows deleted (0 or 1).

        See Also
        --------
        delete_by_pk : Deletes a row from the database by primary key.
        delete_bulk : Deletes multiple rows from the database.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, TableColumn, PrimaryKeyColumn, Column
        >>> from typing import Optional
        >>>
        >>> class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        >>> loom = Loom
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        >>> # Deleting a user based on filters
        >>> num_rows_deleted = loom.delete_one(User, filters=[Filter(column="id", value=1, operator="eq")])
        >>> print(num_rows_deleted)
        """
        return delete(dialect=self.dialect, _execute_sql=self._execute_sql).delete_one(
            instance=instance, offset=offset, order=order, filters=filters
        )

    def delete_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ) -> int:
        """
        delete_bulk
        -----------

        Deletes multiple rows from the database based on specified filters.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table from which the rows need to be deleted.
        filters : Filter | list[Filter] | None, optional
            Filters to apply when selecting the rows to be deleted. It can be a single Filter object, a list of Filter objects, or None to apply no filters. Default is None.
        limit : int | None, optional
            The maximum number of rows to delete. Default is None.
        offset : int | None, optional
            The offset of the rows to delete, useful for pagination. Default is None.
        order : list[Order] | None, optional
            The order in which to delete rows. Default is an empty list.

        Returns
        -------
        affected_rows : int
            The number of rows deleted.

        See Also
        --------
        delete_by_pk : Deletes a row from the database by primary key.
        delete_one : Deletes a single row from the database based on specified filters.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, TableColumn, PrimaryKeyColumn, Column
        >>> from typing import Optional
        >>>
        >>> class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        >>> loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        >>> # Deleting users based on filters
        >>> num_rows_deleted = loom.delete_bulk(User, filters=[Filter(column="tokenVersion", value=2, operator="eq")])
        >>> print(num_rows_deleted)
        """
        return delete(dialect=self.dialect, _execute_sql=self._execute_sql).delete_bulk(
            instance=instance, offset=offset, order=order, filters=filters, limit=limit
        )

    def increment(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ) -> int:
        """
        increment
        ---------

        Increments the value of a column in the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table in which the value needs to be incremented.
        filters : Filter | list[Filter] | None
            Filters to apply when selecting the rows to increment. It can be a single Filter object, a list of Filter objects, or None to apply no filters.
        column : ColumnValue[int | float]
            The column whose value needs to be incremented. It should be of type int or float.

        Returns
        -------
        affected_rows: int
            The number of rows updated with the increment operation.

        See Also
        --------
        decrement : Decrements the value of a column in the database.
        update_one : Updates a single row in the database.
        update_bulk : Updates multiple rows in the database.
        update_by_pk : Updates a row in the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom Filter, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Incrementing the tokenVersion column by 2 where id is 1
        ... affected_rows = loom.increment(
        ...     User,
        ...     filters=[Filter(column="id", value=1, operator="eq")],
        ...     column=ColumnValue(name="tokenVersion", value=2),
        ... )
        ... print(affected_rows)

        """
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).increment(
            column=column,
            filters=filters,
            instance=instance,
        )

    def decrement(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ) -> int:
        """
        decrement
        ---------

        Decrements the value of a column in the database.

        Parameters
        ----------
        instance : Model
            An instance of a Model class representing the table in which the value needs to be decremented.
        filters : Filter | list[Filter] | None
            Filters to apply when selecting the rows to decrement. It can be a single Filter object, a list of Filter objects, or None to apply no filters.
        column : ColumnValue[int | float]
            The column whose value needs to be decremented. It should be of type int or float.

        Returns
        -------
        affected_rows: int
            The number of rows updated with the decrement operation.

        See Also
        --------
        increment : Increments the value of a column in the database.
        update_one : Updates a single row in the database.
        update_bulk : Updates multiple rows in the database.
        update_by_pk : Updates a row in the database by primary key.

        Examples
        --------
        >>> from dataloom import Loom, Model, Filter, ColumnValue, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class User(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="users")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True)
        ...     name = Column(type="text", nullable=False, default="Bob")
        ...     username = Column(type="varchar", unique=True, length=255)
        ...     tokenVersion = Column(type="int", default=0)
        ...
        ... loom = Loom
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... # Decrementing the tokenVersion column by 2 where id is 1
        ... affected_rows = loom.decrement(
        ...     User,
        ...     filters=[Filter(column="id", value=1, operator="eq")],
        ...     column=ColumnValue(name="tokenVersion", value=2),
        ... )
        ... print(affected_rows)

        """
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).decrement(
            column=column,
            filters=filters,
            instance=instance,
        )

    def inspect(
        self,
        instance: Model,
        fields: list[str] = ["name", "type", "nullable", "default"],
        print_table: bool = True,
    ):
        """
        inspect
        -------

        Inspects the fields of a model instance.

        Parameters
        ----------
        instance : Model
            An instance of a Model class to inspect.
        fields : list[str], optional
            A list of field attributes to inspect. Defaults to ["name", "type", "nullable", "default"].
        print_table : bool, optional
            Whether to print the inspection results as a table. Defaults to True. Setting this option to false = leads to print of results as a list of table fields.

        Returns
        -------
        list[dict] | None
            A list of dictionaries containing the inspection results, or None if print_table is True.

        See Also
        --------
        tables : Lists the tables in the database.
        connect_and_sync : Establishes a connection to the database and synchronizes tables, returning a connection and a list of table names.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ...
        ... class Category(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="categories")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
        ...     type = Column(type="varchar", length=255, nullable=False)
        ...
        ... loom = Loom
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ... # inspecting the instance
        ... inspection_results = loom.inspect(Category)
        +------+---------+----------+---------+
        | name | type    | nullable | default |
        +------+---------+----------+---------+
        | id   | int     | NO       | None    |
        | type | varchar | NO       | None    |
        +------+---------+----------+---------+
        """
        return inspect(
            dialect=self.dialect, database=self.database, _execute_sql=self._execute_sql
        ).inspect(instance=instance, fields=fields, print_table=print_table)

    @property
    def tables(self) -> list[str]:
        """
        tables
        ------

        Property that lists the tables in the database.

        Returns
        -------
        tables: list[str]
            A list of table names in the database.

        See Also
        --------
        connect_and_sync : Establishes a connection to the database and synchronizes tables, returning a connection and a list of table names.
        connect : Establishes a connection to the database.
        sync : Synchronizes tables in the database based on provided models.

        Examples
        --------
        >>> from dataloom import Loom
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ... # listing tables in the database
        ... table_names = loom.tables

        """
        sql = GetStatement(self.dialect)._get_tables_command
        res = self._execute_sql(sql, fetchall=True, _verbose=0)
        if self.dialect == "sqlite":
            return [t[0] for t in res if not str(t[0]).lower().startswith("sqlite_")]
        return [t[0] for t in res]

    def _execute_sql(
        self,
        sql: str,
        args=None,
        fetchone=False,
        fetchmany=False,
        fetchall=False,
        mutation=True,
        bulk: bool = False,
        affected_rows: bool = False,
        operation: Optional[str] = None,
        _verbose: int = 1,
        _is_script: bool = False,
    ) -> Any:
        return self.sql_obj.execute_sql(
            sql=sql,
            args=args,
            operation=operation,
            mutation=mutation,
            fetchall=fetchall,
            bulk=bulk,
            fetchone=fetchone,
            fetchmany=fetchmany,
            affected_rows=affected_rows,
            _verbose=_verbose,
            _is_script=_is_script,
        )

    def connect(
        self,
    ) -> Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection:
        """
        connect
        -------

        Establishes a connection to the database.

        Returns
        -------
        conn: Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection
            A connection object to the database.

        See Also
        --------
        tables : Lists the tables in the database.
        connect_and_sync : Establishes a connection to the database and synchronizes tables, returning a connection and a list of table names.
        sync : Synchronizes tables in the database based on provided models.

        Examples
        --------
        >>> from dataloom import Loom
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ... # connecting to the database
        ... conn = loom.connect()
        ...
        ... # Closing the connection
        ... if __name__ == "__main__":
        ...     conn.close()

        """
        if self.dialect == "postgres":
            if self.connection_uri is None:
                options = ConnectionOptionsFactory.get_connection_options(
                    **self.connection_options
                )
                with psycopg2.connect(**options) as conn:
                    self.conn = conn
            else:
                if not self.connection_uri.startswith("postgresql:"):
                    raise InvalidConnectionURI(
                        f"Invalid connection uri for the dialect '{self.dialect}' valid examples are ('postgresql://user:password@localhost:5432/dbname')."
                    )
                with psycopg2.connect(self.connection_uri) as conn:
                    self.conn = conn
        elif self.dialect == "mysql":
            if self.connection_uri is None:
                options = ConnectionOptionsFactory.get_connection_options(
                    **self.connection_options
                )
            else:
                if self.connection_uri.startswith("mysql:"):
                    options = ConnectionOptionsFactory.get_mysql_uri_connection_options(
                        self.connection_uri
                    )
                else:
                    raise InvalidConnectionURI(
                        f"Invalid connection uri for the dialect '{self.dialect}' valid examples are ('mysql://user:password@localhost:3306/dbname')."
                    )
            self.conn = connector.connect(**options)

        elif self.dialect == "sqlite":
            if self.connection_uri is None:
                options = ConnectionOptionsFactory.get_connection_options(
                    **self.connection_options
                )
                if "database" in options:
                    with sqlite3.connect(options.get("database")) as conn:
                        self.conn = conn
                else:
                    with sqlite3.connect(**options) as conn:
                        self.conn = conn
            else:
                import os
                import re

                if not self.connection_uri.startswith("sqlite:"):
                    raise InvalidConnectionURI(
                        f"Invalid connection uri for the dialect '{self.dialect}' valid examples are ('sqlite:///db.db', 'sqlite://db.db', 'sqlite:///path/to/database/db.db')."
                    )
                cwd = os.getcwd()
                dbName = os.path.basename(self.connection_uri)
                path = os.path.join(re.sub(r"sqlite:(/{2,})", "", self.connection_uri))
                directory = os.path.join(cwd, path).replace(dbName, "")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                with sqlite3.connect(os.path.join(directory, dbName)) as conn:
                    self.conn = conn
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        self.sql_obj = SQL(
            conn=self.conn,
            dialect=self.dialect,
            sql_logger=self.sql_logger,
            logs_filename=self.logs_filename,
        )
        return self.conn

    def connect_and_sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> tuple[
        Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection, list[str]
    ]:
        """
        connect_and_sync
        ----------------

        This method is responsible for establishing a connection to your database and synchronizing your database tables.

        Parameters
        ----------
        models : list[Model]
            A list of Python classes that inherit from a Model class with some Column fields defined as the column names of the table.
        drop : bool, optional
            Whether or not to drop existing tables when the method is called again. Defaults to False.
        force : bool, optional
            Force dropping and syncing of tables when the method is called. Defaults to False.
        alter : bool, optional
            Whether to alter tables or not while syncing them. Defaults to False if not passed.

        Returns
        -------
        tuple: [ Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection, list[str] ]
            This method returns a tuple with the connection as the first value and a list of table names in the database as the second value.

        See Also
        --------
        sync : Synchronize tables without returning a connection and does not return the list of table names that are in the database.
        connect : Connect to a database without syncing tables and does not return a list of tables; rather, it returns a connection object only.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... class Category(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="categories")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
        ...     type = Column(type="varchar", length=255, nullable=False)
        ... # connecting and syncing tables
        ... conn, tables = mysql_loom.connect_and_sync(
        ...     [Category], drop=True, force=True
        ... )
        ... # closing the connection
        ... if __name__ == "__main__":
        ...     conn.close()

        """
        try:
            self.conn = self.connect()
            self.sql_obj = SQL(
                conn=self.conn,
                dialect=self.dialect,
                sql_logger=self.sql_logger,
                logs_filename=self.logs_filename,
            )
            tables = self.sync(models=models, drop=drop, force=force, alter=alter)
            return self.conn, tables
        except Exception as e:
            raise Exception(e)

    def sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> list[str]:
        """
        sync
        ----

        Synchronize tables in the database based on the provided models.

        Parameters
        ----------
        models : list[Model]
            A list of Python classes that inherit from a Model class with some Column fields defined as the column names of the table.
        drop : bool, optional
            Whether or not to drop existing tables before synchronization. Defaults to False.
        force : bool, optional
            Force synchronization of tables, even if they already exist. Defaults to False.
        alter : bool, optional
            Whether to alter existing tables while synchronizing. Defaults to False.

        Returns
        -------
        list[str]
            A list of table names that were synchronized in the database.

        See Also
        --------
        tables : Lists the tables in the database.
        connect_and_sync : Establishes a connection to the database and synchronizes tables, returning a connection and a list of table names.

        Examples
        --------
        >>> from dataloom import Loom, Model, TableColumn, PrimaryKeyColumn, Column
        ... from typing import Optional
        ... loom = Loom(
        ...    dialect="postgres",
        ...    database="hi",
        ...    password="root",
        ...    user="postgres",
        ...    sql_logger="console",
        ... )
        ...
        ... class Category(Model):
        ...     __tablename__: Optional[TableColumn] = TableColumn(name="categories")
        ...     id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
        ...     type = Column(type="varchar", length=255, nullable=False)
        ... # synchronizing tables
        ... tables = loom.sync(
        ...     [Category], drop=True, force=True
        ... )

        """
        try:
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql(dialect=self.dialect))
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
                elif alter:
                    # 1. we only alter the table if it does exists
                    # 2. if not we just have to create a new table
                    if model._get_table_name() in self.tables:
                        sql1 = model._get_describe_stm(
                            dialect=self.dialect, fields=["column_name"]
                        )
                        args = None
                        if self.dialect == "mysql":
                            args = (self.database, model._get_table_name())
                        elif self.dialect == "postgres":
                            args = ("public", model._get_table_name())
                        elif self.dialect == "sqlite":
                            args = ()
                        cols = self._execute_sql(
                            sql1, _verbose=0, args=args, fetchall=True
                        )
                        if cols is not None:
                            if self.dialect == "mysql":
                                old_columns = [col for (col,) in cols]
                            elif self.dialect == "postgres":
                                old_columns = [col for (col,) in cols]
                            else:
                                old_columns = [col[1] for col in cols]
                        sql = model._alter_sql(
                            dialect=self.dialect, old_columns=old_columns
                        )
                        self._execute_sql(sql, _is_script=True)
                    else:
                        for sql in model._create_sql(dialect=self.dialect):
                            if sql is not None:
                                self._execute_sql(sql)
                else:
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
            return self.tables
        except Exception as e:
            raise Exception(e)
