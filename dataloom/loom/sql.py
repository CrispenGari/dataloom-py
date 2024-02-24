from typing import Any, Optional
from dataloom.types import DIALECT_LITERAL, SQL_LOGGER_LITERAL
from dataloom.exceptions import UnsupportedDialectException
from sqlite3 import Connection
from mysql.connector.connection import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from dataloom.utils import (
    file_logger,
    console_logger,
)
from abc import ABC, abstractclassmethod


class SQL(ABC):
    @abstractclassmethod
    def execute_sql(
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
        raise NotImplementedError("The execute_sql method was not implemented.")


class sql(SQL):
    __logger_index: int = 0

    def __init__(
        self,
        conn: Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection,
        dialect: DIALECT_LITERAL,
        sql_logger: Optional[SQL_LOGGER_LITERAL] = None,
        logs_filename: Optional[str] = "dataloom.sql",
    ) -> None:
        self.conn = conn
        self.dialect = dialect
        self.sql_logger = sql_logger
        self.logs_filename = logs_filename

        if self.__logger_index == 0:
            self.__logger_index = 0
        else:
            pass

    def execute_sql(
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
        # do we need to log the executed SQL?
        if self.sql_logger is not None and _verbose > 0:
            if self.sql_logger == "console":
                index = console_logger(
                    index=self.__logger_index,
                    sql_statement=sql.strip(),
                    dialect=self.dialect,
                )
                self.__logger_index = index + 1
            else:
                file_logger(
                    dialect=self.dialect,
                    file_name=self.logs_filename,
                    sql_statement=sql.strip(),
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
                        result = [res for res in cursor.fetchmany()]
                    elif fetchall:
                        result = [res for res in cursor.fetchall()]
                    elif fetchone:
                        result = cursor.fetchone()
                    else:
                        result = None
                if mutation:
                    self.conn.commit()
        elif self.dialect == "mysql":
            with self.conn.cursor(buffered=True) as cursor:
                if _is_script:
                    for part in sql.split(";"):
                        try:
                            cursor.execute(part + ";")
                        except Exception:
                            pass
                    return None

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
            if _is_script:
                cursor.executescript(sql)
            else:
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
