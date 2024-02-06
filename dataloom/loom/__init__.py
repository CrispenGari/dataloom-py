import psycopg2
from mysql import connector
import sqlite3
from dataloom.constants import instances

from dataloom.exceptions import UnsupportedDialectException
from dataloom.model import Model
from dataloom.statements import GetStatement
from dataloom.conn import ConnectionOptionsFactory
from dataloom.utils import logger_function, get_child_table_columns
from typing import Optional
from dataloom.types import Order, Include, DIALECT_LITERAL, Filter, ColumnValue


class Dataloom:
    def __init__(
        self,
        database: str,
        dialect: DIALECT_LITERAL,
        user: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        password: Optional[str] = None,
        logging: bool = True,
        logs_filename: Optional[str] = "dataloom.sql",
    ) -> None:
        self.database = database
        self.conn = None
        self.logging = logging
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

    @property
    def tables(self):
        sql = GetStatement(self.dialect)._get_tables_command
        res = self._execute_sql(sql, fetchall=True)
        if self.dialect == "sqlite":
            return [t[0] for t in res if not str(t[0]).lower().startswith("sqlite_")]
        return [t[0] for t in res]

    def _execute_sql(
        self,
        sql,
        args=None,
        fetchone=False,
        fetchmany=False,
        fetchall=False,
        mutation=True,
        bulk: bool = False,
        affected_rows: bool = False,
        operation: Optional[str] = None,
    ):
        # do we need to log the executed SQL?
        if self.logging:
            print(sql)
            if self.logs_filename is not None:
                logger_function(
                    dialect=self.dialect,
                    file_name=self.logs_filename,
                    sql_statement=sql,
                )
        if self.dialect == "postgres":
            with self.conn.cursor() as cursor:
                if args is None:
                    cursor.execute(sql)
                else:
                    if bulk:
                        cursor.executemany(sql, vars_list=args)
                    else:
                        cursor.execute(sql, vars=args)
                # options
                if bulk or affected_rows:
                    result = cursor.rowcount
                else:
                    if fetchmany:
                        result = cursor.fetchmany()
                    elif fetchall:
                        result = cursor.fetchall()
                    elif fetchone:
                        result = cursor.fetchone()
                    else:
                        result = None
                if mutation:
                    self.conn.commit()
        elif self.dialect == "mysql":
            with self.conn.cursor(buffered=True) as cursor:
                if args is None:
                    cursor.execute(sql)
                else:
                    if bulk:
                        cursor.executemany(sql, args)
                    else:
                        cursor.execute(sql, args)
                # options
                if bulk or affected_rows:
                    result = cursor.rowcount
                else:
                    if fetchmany:
                        result = cursor.fetchmany()
                    elif fetchall:
                        result = cursor.fetchall()
                    elif fetchone:
                        result = cursor.fetchone()
                    else:
                        result = None
                if mutation:
                    self.conn.commit()

                if operation is not None:
                    result = cursor.lastrowid
        elif self.dialect == "sqlite":
            cursor = self.conn.cursor()
            if args is None:
                cursor.execute(sql)
            else:
                if bulk:
                    cursor.executemany(sql, args)
                else:
                    cursor.execute(sql, args)
            # options
            if bulk or affected_rows:
                result = cursor.rowcount
            else:
                if fetchmany:
                    result = cursor.fetchmany()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
                else:
                    result = None
            if mutation:
                self.conn.commit()
            if operation is not None:
                result = cursor.lastrowid
        else:
            raise UnsupportedDialectException(
                "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
            )

        return result

    def connect(self):
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
    ):
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
                    self._execute_sql(model._create_sql(dialect=self.dialect))
                elif alter:
                    pass
                else:
                    self._execute_sql(
                        model._create_sql(dialect=self.dialect, ignore_exists=True)
                    )
            return self.conn, self.tables
        except Exception as e:
            raise Exception(e)

    def sync(self, models: list[Model], drop=False, force=False, alter=False):
        try:
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql(dialect=self.dialect))
                    self._execute_sql(model._create_sql(dialect=self.dialect))
                elif alter:
                    pass
                else:
                    self._execute_sql(
                        model._create_sql(dialect=self.dialect, ignore_exists=True)
                    )
            return self.tables
        except Exception as e:
            raise Exception(e)

    def insert_one(self, instance: Model):
        sql, values = instance._get_insert_one_stm(dialect=self.dialect)
        row = self._execute_sql(
            sql,
            args=tuple(values),
            fetchone=self.dialect == "postgres",
            operation="insert",
        )
        return row[0] if type(row) in [list, tuple] else row

    def insert_bulk(self, instances: list[Model]):
        columns = None
        placeholders = None
        data = list()
        for instance in instances:
            (
                column_names,
                placeholder_values,
                _values,
            ) = instance._get_insert_bulk_attrs(dialect=self.dialect)
            if columns is None:
                columns = column_names
            if placeholders is None:
                placeholders = placeholder_values

            data.append(_values)
        sql, values = instance._get_insert_bulk_smt(
            dialect=self.dialect,
            placeholders=placeholder_values,
            columns=columns,
            data=data,
        )
        row_count = self._execute_sql(sql, args=tuple(values), fetchall=True, bulk=True)
        return row_count

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
        sql, params, fields = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=select,
            limit=limit,
            offset=offset,
            order=order,
            include=include,
        )
        data = []
        rows = self._execute_sql(sql, fetchall=True, args=params)
        for row in rows:
            res = self.__map_relationships(
                instance=instance,
                row=row,
                parent_fields=fields,
                include=include,
                return_dict=return_dict,
            )
            data.append(res)
        return data

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
        return_dict = True
        sql, params, fields = instance._get_select_where_stm(
            dialect=self.dialect,
            select=select,
            limit=limit,
            offset=offset,
            order=order,
            include=include,
        )
        data = []
        rows = self._execute_sql(sql, fetchall=True)
        for row in rows:
            res = self.__map_relationships(
                instance=instance,
                row=row,
                parent_fields=fields,
                include=include,
                return_dict=return_dict,
            )
            data.append(res)
        return data

    def __map_relationships(
        self,
        instance: Model,
        row: tuple,
        parent_fields: list,
        include: list[Include] = [],
        return_dict: bool = True,
    ):
        # how are relations are mapped?
        json = dict(zip(parent_fields, row[: len(parent_fields)]))
        result = json if return_dict else instance(**json)
        row = row[len(parent_fields) :]
        for _include in include:
            alias, selected = [v for v in get_child_table_columns(_include).items()][0]
            child_json = dict(zip(selected, row[: len(selected)]))
            row = row[len(selected) :]
            if return_dict:
                result[alias] = child_json
            else:
                result[alias] = _include.model(**child_json)
        return result

    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
    ):
        return_dict = True
        # what is the name of the primary key column? well we will find out
        sql, fields = instance._get_select_by_pk_stm(
            dialect=self.dialect, select=select, include=include
        )
        row = self._execute_sql(sql, args=(pk,), fetchone=True)
        if row is None:
            return None
        return self.__map_relationships(
            instance=instance,
            row=row,
            parent_fields=fields,
            include=include,
            return_dict=return_dict,
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
        return_dict = True
        sql, params, fields = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=select,
            offset=offset,
            include=include,
        )
        row = self._execute_sql(sql, args=params, fetchone=True)
        if row is None:
            return None
        return self.__map_relationships(
            instance=instance,
            row=row,
            parent_fields=fields,
            include=include,
            return_dict=return_dict,
        )

    def update_by_pk(
        self, instance: Model, pk, values: ColumnValue | list[ColumnValue]
    ):
        sql, args = instance._get_update_by_pk_stm(dialect=self.dialect, values=values)
        args.append(pk)
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def update_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        sql, new_values, filter_values = instance._get_update_one_stm(
            dialect=self.dialect, filters=filters, values=values
        )
        args = [*new_values, *filter_values]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def update_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        sql, new_values, filter_values = instance._get_update_bulk_where_stm(
            dialect=self.dialect, filters=filters, values=values
        )
        args = [*new_values, *filter_values]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def delete_by_pk(self, instance: Model, pk):
        sql = instance._get_delete_by_pk_stm(dialect=self.dialect)
        affected_rows = self._execute_sql(
            sql, args=(pk,), affected_rows=True, fetchall=True
        )
        return affected_rows

    def delete_one(
        self, instance: Model, filters: Optional[Filter | list[Filter]] = None
    ):
        sql, params = instance._get_delete_where_stm(
            dialect=self.dialect,
            filters=filters,
        )
        affected_rows = self._execute_sql(sql, args=params, affected_rows=True)
        return affected_rows

    def delete_bulk(
        self, instance: Model, filters: Optional[Filter | list[Filter]] = None
    ):
        sql, params = instance._get_delete_bulk_where_stm(
            dialect=self.dialect,
            filters=filters,
        )
        affected_rows = self._execute_sql(
            sql, args=params, affected_rows=True, fetchall=True
        )
        return affected_rows

    def increment(self):
        pass

    def decrement(self):
        pass
