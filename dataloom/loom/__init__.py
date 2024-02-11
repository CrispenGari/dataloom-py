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
from dataloom.exceptions import UnsupportedDialectException
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
)
from dataloom.loom.interfaces import IDataloom


class Dataloom(IDataloom):
    def __init__(
        self,
        database: str,
        dialect: DIALECT_LITERAL,
        user: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        password: Optional[str] = None,
        sql_logger: Optional[SQL_LOGGER_LITERAL] = None,
        logs_filename: Optional[str] = "dataloom.sql",
    ) -> None:
        self.logger_index = 0
        self.database = database
        self.conn = None
        self.sql_logger = sql_logger
        self.dialect = dialect
        self.logs_filename = logs_filename

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

    def insert_one(self, instance: Model, values: ColumnValue | list[ColumnValue]):
        return insert(dialect=self.dialect, _execute_sql=self._execute_sql).insert_one(
            instance=instance, values=values
        )

    def insert_bulk(self, instance: Model, values: list[list[ColumnValue]]):
        return insert(dialect=self.dialect, _execute_sql=self._execute_sql).insert_bulk(
            instance=instance, values=values
        )

    def find_many(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        include: list[Model] = [],
        return_dict: bool = True,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> list:
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_many(
            instance=instance,
            limit=limit,
            select=select,
            include=include,
            offset=offset,
            filters=filters,
            return_dict=return_dict,
            order=order,
        )

    def find_all(
        self,
        instance: Model,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> list:
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_all(
            instance=instance,
            select=select,
            include=include,
            return_dict=return_dict,
            limit=limit,
            offset=offset,
            order=order,
        )

    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
    ):
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_by_pk(
            include=include,
            pk=pk,
            return_dict=return_dict,
            select=select,
            instance=instance,
        )

    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
        offset: Optional[int] = None,
    ):
        return query(dialect=self.dialect, _execute_sql=self._execute_sql).find_one(
            instance=instance,
            select=select,
            filters=filters,
            offset=offset,
            include=include,
            return_dict=return_dict,
        )

    def update_by_pk(
        self, instance: Model, pk, values: ColumnValue | list[ColumnValue]
    ):
        return update(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).update_by_pk(instance=instance, pk=pk, values=values)

    def update_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).update_one(
            instance=instance, filters=filters, values=values
        )

    def update_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        return update(dialect=self.dialect, _execute_sql=self._execute_sql).update_bulk(
            instance=instance, filters=filters, values=values
        )

    def delete_by_pk(self, instance: Model, pk):
        return delete(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).delete_by_pk(instance=instance, pk=pk)

    def delete_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = [],
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        return delete(dialect=self.dialect, _execute_sql=self._execute_sql).delete_one(
            instance=instance, offset=offset, order=order, filters=filters
        )

    def delete_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        return delete(dialect=self.dialect, _execute_sql=self._execute_sql).delete_bulk(
            instance=instance, offset=offset, order=order, filters=filters, limit=limit
        )

    def increment(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ):
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
    ):
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
        return inspect(
            dialect=self.dialect, database=self.database, _execute_sql=self._execute_sql
        ).inspect(instance=instance, fields=fields, print_table=print_table)

    @property
    def tables(self) -> list[str]:
        sql = GetStatement(self.dialect)._get_tables_command
        res = self._execute_sql(sql, fetchall=True)
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
    ) -> Any:
        return SQL(
            conn=self.conn,
            dialect=self.dialect,
            sql_logger=self.sql_logger,
            logs_filename=self.logs_filename,
        ).execute_sql(
            sql=sql,
            args=args,
            operation=operation,
            mutation=mutation,
            fetchall=fetchall,
            bulk=bulk,
            fetchone=fetchone,
            fetchmany=fetchmany,
            affected_rows=affected_rows,
        )

    def connect(
        self,
    ) -> Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection:
        if self.dialect == "postgres":
            options = ConnectionOptionsFactory.get_connection_options(
                **self.connection_options
            )
            with psycopg2.connect(**options) as conn:
                self.conn = conn
        elif self.dialect == "mysql":
            options = ConnectionOptionsFactory.get_connection_options(
                **self.connection_options
            )
            self.conn = connector.connect(**options)

        elif self.dialect == "sqlite":
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
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )
        return self.conn

    def connect_and_sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> tuple[
        Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection, list[str]
    ]:
        try:
            if self.dialect == "postgres":
                options = ConnectionOptionsFactory.get_connection_options(
                    **self.connection_options
                )
                with psycopg2.connect(**options) as conn:
                    self.conn = conn
            elif self.dialect == "mysql":
                options = ConnectionOptionsFactory.get_connection_options(
                    **self.connection_options
                )
                self.conn = connector.connect(**options)

            elif self.dialect == "sqlite":
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
                raise UnsupportedDialectException(
                    "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
                )
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql(dialect=self.dialect))
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
                elif alter:
                    pass
                else:
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
            return self.conn, self.tables
        except Exception as e:
            raise Exception(e)

    def sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> list[str]:
        try:
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql(dialect=self.dialect))
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
                elif alter:
                    pass
                else:
                    for sql in model._create_sql(dialect=self.dialect):
                        if sql is not None:
                            self._execute_sql(sql)
            return self.tables
        except Exception as e:
            raise Exception(e)
