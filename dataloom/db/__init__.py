import psycopg2
from mysql import connector
import sqlite3
import inspect
from dataloom.constants import instances
from dataloom.model.statements import PgStatements
from dataloom.exceptions import UnsupportedDialectException
from dataloom.model import Model
from dataloom.statements import GetStatement
from dataloom.conn import ConnectionOptionsFactory
from dataloom.model.column import (
    Column,
    UpdatedAtColumn,
    PrimaryKeyColumn,
    CreatedAtColumn,
    ForeignKeyColumn,
)
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
    ) -> None:
        self.database = database
        self.conn = None
        self.logging = logging
        self.dialect = dialect
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
    ):
        # do we need to log the executed SQL?
        if self.logging:
            print(sql)
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
                cursor.execute(sql)
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
        elif self.dialect == "sqlite":
            cursor = self.conn.cursor()
            cursor.execute(sql)
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


# class Database:
#     def __init__(
#         self,
#         database: str,
#         dialect: str = "postgres",
#         user: str | None = None,
#         host: str | None = None,
#         port: int | None = None,
#         password: str | None = None,
#         logs: bool = True,
#     ) -> None:
#         config = instances[dialect]
#         self.user = user if user else config["user"]
#         self.password = password if password else config["password"]
#         self.port = port if port else config["port"]
#         self.host = host if host else config["host"]
#         self.database = database
#         self.conn = None
#         self.logs = logs

#     @property
#     def tables(self):
#         res = self._execute_sql(
#             PgStatements.GET_TABLES.format(schema_name="public"), fetchall=True
#         )
#         return [t[0] for t in res]

#     def _execute_sql(
#         self,
#         sql,
#         args=None,
#         fetchone=False,
#         fetchmany=False,
#         fetchall=False,
#         mutation=True,
#         bulk: bool = False,
#         affected_rows: bool = False,
#     ):
#         # do we need to log the executed SQL?
#         if self.logs:
#             print(sql)

#         with self.conn.cursor() as cursor:
#             if args is None:
#                 cursor.execute(sql)
#             else:
#                 (
#                     cursor.executemany(sql, vars_list=args)
#                     if bulk
#                     else cursor.execute(sql, vars=args)
#                 )
#             # options
#             if bulk or affected_rows:
#                 result = cursor.rowcount
#             else:
#                 if fetchmany:
#                     result = cursor.fetchmany()
#                 elif fetchall:
#                     result = cursor.fetchall()
#                 elif fetchone:
#                     result = cursor.fetchone()
#                 else:
#                     result = None
#             if mutation:
#                 self.conn.commit()

#         return result

#     def connect(self):
#         try:
#             self.conn = psycopg2.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password,
#                 port=self.port,
#             )
#             return self.conn
#         except Exception as e:
#             raise Exception(e)

#     def connect_and_sync(
#         self, models: list[Model], drop=False, force=False, alter=False
#     ):
#         try:
#             self.conn = psycopg2.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password,
#                 port=self.port,
#             )
#             for model in models:
#                 if drop or force:
#                     self._execute_sql(model._drop_sql())
#                     self._execute_sql(model._create_sql())
#                 elif alter:
#                     pass
#                 else:
#                     self._execute_sql(model._create_sql(ignore_exists=True))
#             return self.conn, self.tables

#         except Exception as e:
#             raise Exception(e)

#     def sync(self, models: list[Model], drop=False, force=False, alter=False):
#         try:
#             for model in models:
#                 if drop or force:
#                     self._execute_sql(model._drop_sql())
#                     self._execute_sql(model._create_sql())
#                 elif alter:
#                     pass
#                 else:
#                     self._execute_sql(model._create_sql(ignore_exists=True))

#             return self.tables
#         except Exception as e:
#             raise Exception(e)

#     def create(self, instance: Model):
#         sql, values = instance._get_insert_one_stm()
#         row = self._execute_sql(sql, args=tuple(values), fetchone=True)
#         return row[0]

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
