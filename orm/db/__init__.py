import psycopg2
import inspect
from orm.constants import instances
from orm.model.statements import Statements
from orm.model.model import Model
from orm.model.column import (
    Column,
    UpdatedAtColumn,
    PrimaryKeyColumn,
    CreatedAtColumn,
    ForeignKeyColumn,
)
from functools import partial


class Database:
    def __init__(
        self,
        database: str,
        dialect: str = "postgres",
        user: str | None = None,
        host: str | None = None,
        port: int | None = None,
        password: str | None = None,
        logs: bool = True,
    ) -> None:
        config = instances[dialect]
        self.user = user if user else config["user"]
        self.password = password if password else config["password"]
        self.port = port if port else config["port"]
        self.host = host if host else config["host"]
        self.database = database
        self.conn = None
        self.logs = logs

    @property
    def tables(self):
        res = self._execute_sql(
            Statements.GET_TABLES.format(schema_name="public"), fetchall=True
        )
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
    ):
        # do we need to log the executed SQL?
        if self.logs:
            print(sql)

        with self.conn.cursor() as cursor:
            if args is None:
                cursor.execute(sql)
            else:
                cursor.executemany(sql, vars_list=args) if bulk else cursor.execute(
                    sql, vars=args
                )
            # options
            if bulk:
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

        return result

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            return self.conn
        except Exception as e:
            raise Exception(e)

    def connect_and_sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql())
                    self._execute_sql(model._create_sql())
                elif alter:
                    pass
                else:
                    self._execute_sql(model._create_sql(ignore_exists=True))
            return self.conn, self.tables

        except Exception as e:
            raise Exception(e)

    def sync(self, models: list[Model], drop=False, force=False, alter=False):
        try:
            for model in models:
                if drop or force:
                    self._execute_sql(model._drop_sql())
                    self._execute_sql(model._create_sql())
                elif alter:
                    pass
                else:
                    self._execute_sql(model._create_sql(ignore_exists=True))

            return self.tables
        except Exception as e:
            raise Exception(e)

    def commit(self, instance: Model):
        sql, values = instance._get_insert_one_stm()
        row = self._execute_sql(sql, args=tuple(values), fetchone=True)
        return row[0]

    def commit_bulk(self, instances: list[Model]):
        columns = None
        placeholders = None
        data = list()
        for instance in instances:
            (
                column_names,
                placeholder_values,
                _values,
            ) = instance._get_insert_bulk_attrs()
            if columns is None:
                columns = column_names
            if placeholders is None:
                placeholders = placeholder_values

            data.append(_values)
        sql, values = instance._get_insert_bulk_smt(placeholders, columns, data)
        row_count = self._execute_sql(sql, args=tuple(values), fetchall=True, bulk=True)
        return row_count

    def find_all(self, instance: Model):
        fields = list()
        for name, field in inspect.getmembers(instance):
            if isinstance(field, Column):
                fields.append(name)
        sql, _, __ = instance._get_select_where_stm(fields)
        data = list()
        rows = self._execute_sql(sql, fetchall=True)
        print(len(rows))
        for row in rows:
            res = dict(zip(fields, row))
            data.append(instance(**res))
        return data

    def find_many(self, instance: Model, filters: dict = {}):
        fields = list()
        for name, field in inspect.getmembers(instance):
            if isinstance(field, Column):
                fields.append(name)
        sql, _, params = instance._get_select_where_stm(fields, filters)
        data = list()
        rows = self._execute_sql(sql, args=params, fetchall=True)
        for row in rows:
            res = dict(zip(fields, row))
            data.append(instance(**res))
        return data

    def find_by_pk(self, instance: Model, pk):
        # what is the name of the primary key column?
        pk_name = "id"
        fields = list()
        for name, field in inspect.getmembers(instance):
            if (
                isinstance(field, Column)
                or isinstance(field, ForeignKeyColumn)
                or isinstance(field, CreatedAtColumn)
                or isinstance(field, UpdatedAtColumn)
            ):
                fields.append(name)
            elif isinstance(field, PrimaryKeyColumn):
                pk_name = name
                fields.append(name)

        print(fields)
        sql, fields = instance._get_select_by_pk_stm(pk, pk_name, fields=fields)
        row = self._execute_sql(sql, fetchone=True)
        return None if row is None else instance(**dict(zip(fields, row)))

    def find_one(self, instance: Model, filters: dict = {}):
        fields = list()
        for name, field in inspect.getmembers(instance):
            if isinstance(field, Column):
                fields.append(name)
        sql, _, params = instance._get_select_where_stm(fields, filters)
        row = self._execute_sql(sql, args=params, fetchone=True)
        return None if row is None else instance(**dict(zip(fields, row)))

    def delete_one(self, instance: Model, filters: dict = {}):
        fields = list()
        for name, field in inspect.getmembers(instance):
            if isinstance(field, Column):
                fields.append(name)
        sql, _, params = instance._get_select_where_stm(fields, filters)
        row = self._execute_sql(sql, args=params, fetchone=True)
        return None if row is None else instance(**dict(zip(fields, row)))

    def delete_by_pk(self, instance: Model, pk):
        # what is the name of the primary key column?
        pk_name = "id"
        fields = list()
        for name, field in inspect.getmembers(instance):
            if isinstance(field, Column):
                if field.primary_key:
                    pk_name = name
                fields.append(name)
        sql, fields = instance._get_select_by_pk_stm(pk, pk_name, fields=fields)
        row = self._execute_sql(sql, fetchone=True)
        return None if row is None else instance(**dict(zip(fields, row)))
