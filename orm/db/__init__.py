import psycopg2
from orm.constants import instances
from orm.model.statements import Statements
from orm.model.model import Model


class Database:
    def __init__(
        self,
        database: str,
        dialect: str = "postgres",
        user: str | None = None,
        host: str | None = None,
        port: int | None = None,
        password: str | None = None,
    ) -> None:
        config = instances[dialect]
        self.user = user if user else config["user"]
        self.password = password if password else config["password"]
        self.port = port if port else config["port"]
        self.host = host if host else config["host"]
        self.database = database
        self.conn = None

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
    ):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            if fetchmany:
                row = cursor.fetchmany()
            elif fetchall:
                row = cursor.fetchall()
            elif fetchone:
                row = cursor.fetchone()
            else:
                row = None
            if mutation:
                self.conn.commit()
        return row

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

    def connect_and_sync(self, drop=False):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            with self.conn.cursor() as cursor:
                cursor.execute("")

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

        except Exception as e:
            raise Exception(e)


class ForeignKey:
    pass
