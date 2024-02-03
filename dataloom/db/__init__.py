import psycopg2
from mysql import connector
import sqlite3
from dataloom.constants import instances

from dataloom.exceptions import UnsupportedDialectException
from dataloom.model import Model
from dataloom.statements import GetStatement
from dataloom.conn import ConnectionOptionsFactory
from dataloom.utils import logger_function
from typing import Optional


class Dataloom:
    def __init__(
        self,
        database: str,
        dialect: str,
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
                    cursor.executemany(sql, __parameters=args)
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


# class Database:


#     def create_bulk(self, instances: list[Model]):
#         columns = None
#         placeholders = None
#         data = list()
#         for instance in instances:
#             (
#                 column_names,
#                 placeholder_values,
#                 _values,
#             ) = instance._get_insert_bulk_attrs()
#             if columns is None:
#                 columns = column_names
#             if placeholders is None:
#                 placeholders = placeholder_values

#             data.append(_values)
#         sql, values = instance._get_insert_bulk_smt(placeholders, columns, data)
#         row_count = self._execute_sql(sql, args=tuple(values), fetchall=True, bulk=True)
#         return row_count

#     def find_all(self, instance: Model):
#         fields = list()
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, Column):
#                 fields.append(name)
#         sql, _, __ = instance._get_select_where_stm(fields)
#         data = list()
#         rows = self._execute_sql(sql, fetchall=True)
#         for row in rows:
#             res = dict(zip(fields, row))
#             data.append(instance(**res))
#         return data

#     def find_many(self, instance: Model, filters: dict = {}):
#         fields = list()
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, Column):
#                 fields.append(name)
#         sql, _, params = instance._get_select_where_stm(fields, filters)
#         data = list()
#         rows = self._execute_sql(sql, args=params, fetchall=True)
#         for row in rows:
#             res = dict(zip(fields, row))
#             data.append(instance(**res))
#         return data

#     def find_by_pk(self, instance: Model, pk, options: dict = {}):
#         # what is the name of the primary key column?
#         """
#         SELECT
#             posts.post_id,
#             posts.content,
#             posts.created_at,
#             users.user_id,
#             users.username
#         FROM
#             posts
#         JOIN
#             users ON posts.user_id = users.user_id
#         WHERE
#             posts.post_id = 1;  -- Replace 1 with the specific post_id you are interested in
#         """
#         pk_name = "id"
#         fields = list()
#         for name, field in inspect.getmembers(instance):
#             if (
#                 isinstance(field, Column)
#                 or isinstance(field, ForeignKeyColumn)
#                 or isinstance(field, CreatedAtColumn)
#                 or isinstance(field, UpdatedAtColumn)
#             ):
#                 fields.append(name)
#             elif isinstance(field, PrimaryKeyColumn):
#                 pk_name = name
#                 fields.append(name)
#         sql, fields = instance._get_select_by_pk_stm(pk, pk_name, fields=fields)
#         row = self._execute_sql(sql, fetchone=True)
#         return None if row is None else instance(**dict(zip(fields, row)))

#     def find_one(self, instance: Model, filters: dict = {}):
#         fields = list()
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, Column):
#                 fields.append(name)
#         sql, _, params = instance._get_select_where_stm(fields, filters)
#         row = self._execute_sql(sql, args=params, fetchone=True)
#         return None if row is None else instance(**dict(zip(fields, row)))

#     def delete_bulk(self, instance: Model, filters: dict = {}):
#         sql, params = instance._get_delete_bulk_where_stm(filters)
#         affected_rows = self._execute_sql(
#             sql, args=params, affected_rows=True, fetchall=True
#         )
#         return affected_rows

#     def delete_one(self, instance: Model, filters: dict = {}):
#         pk = None
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, PrimaryKeyColumn):
#                 pk = name
#         sql, params = instance._get_delete_where_stm(pk=pk, args=filters)
#         affected_rows = self._execute_sql(sql, args=params, affected_rows=True)
#         return affected_rows

#     def delete_by_pk(self, instance: Model, pk):
#         # what is the name of the primary key column?
#         pk_name = "id"
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, PrimaryKeyColumn):
#                 pk_name = name

#         sql, pk = instance._get_delete_by_pk_stm(pk, pk_name)
#         affected_rows = self._execute_sql(
#             sql, args=(pk,), affected_rows=True, fetchall=True
#         )
#         return affected_rows

#     def update_by_pk(self, instance: Model, pk, values: dict = {}):
#         pk_name = "id"
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, PrimaryKeyColumn):
#                 pk_name = name
#         sql, values = instance._get_update_by_pk_stm(pk_name, values)
#         values.append(pk)
#         affected_rows = self._execute_sql(sql, args=values, affected_rows=True)
#         return affected_rows

#     def update_one(self, instance: Model, filters: dict = {}, values: dict = {}):
#         pk_name = "id"
#         for name, field in inspect.getmembers(instance):
#             if isinstance(field, PrimaryKeyColumn):
#                 pk_name = name
#         sql, new_values, filter_values = instance._get_update_one_stm(
#             pk_name, filters, values
#         )
#         args = [*new_values, *filter_values]
#         affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
#         return affected_rows

#     def update_bulk(self, instance: Model, filters: dict = {}, values: dict = {}):
#         sql, new_values, filter_values = instance._get_update_bulk_where_stm(
#             filters, values
#         )
#         args = [*new_values, *filter_values]
#         affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
#         return affected_rows
