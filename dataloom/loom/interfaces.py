from abc import abstractclassmethod, ABC
from dataloom.model import Model
from dataloom.types import ColumnValue, Order, Filter, Include
from typing import Any, Optional
from mysql.connector.pooling import PooledMySQLConnection
from sqlite3 import Connection
from mysql.connector.connection import MySQLConnectionAbstract


class ILoom(ABC):
    @abstractclassmethod
    def increment(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ) -> int:
        raise NotImplementedError("The increment method was not implemented.")

    @abstractclassmethod
    def decrement(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ) -> int:
        raise NotImplementedError("The decrement method was not implemented.")

    @abstractclassmethod
    def update_by_pk(
        self, instance: Model, pk, values: ColumnValue | list[ColumnValue]
    ) -> int:
        raise NotImplementedError("The update_by_pk was not implemented")

    @abstractclassmethod
    def update_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        raise NotImplementedError("The update_one method was not implemented")

    @abstractclassmethod
    def update_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ) -> int:
        raise NotImplementedError("The update_bulk method was not implemented.")

    @abstractclassmethod
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
        raise NotImplementedError("The execute_sql method was not implemented.")

    @abstractclassmethod
    def find_many(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        include: list[Model] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> list:
        raise NotImplementedError("The find_many method was not implemented.")

    @abstractclassmethod
    def find_all(
        self,
        instance: Model,
        select: list[str] = [],
        include: list[Include] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> list:
        raise NotImplementedError("The find_all method was not implemented.")

    @abstractclassmethod
    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: list[str] = [],
        include: list[Include] = [],
    ) -> dict | None:
        raise NotImplementedError("The find_by_pk method was not implemented.")

    @abstractclassmethod
    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        include: list[Include] = [],
        offset: Optional[int] = None,
    ) -> dict | None:
        raise NotImplementedError("The find_one method was not implemented.")

    @abstractclassmethod
    def inspect(
        self,
        instance: Model,
        fields: list[str] = ["name", "type", "nullable", "default"],
        print_table: bool = True,
    ) -> list[dict] | None:
        raise NotImplementedError("The inspect method was not implemented.")

    @abstractclassmethod
    def insert_one(
        self, instance: Model, values: ColumnValue | list[ColumnValue]
    ) -> Any:
        raise NotImplementedError("The insert_one method was not implemented.")

    @abstractclassmethod
    def insert_bulk(self, instance: Model, values: list[list[ColumnValue]]) -> int:
        raise NotImplementedError("The insert_bulk method was not implemented.")

    @abstractclassmethod
    def delete_by_pk(self, instance: Model, pk) -> int:
        raise NotImplementedError("The delete_by_pk function not implemented.")

    @abstractclassmethod
    def delete_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = [],
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> int:
        raise NotImplementedError("The delete_one function not implemented.")

    @abstractclassmethod
    def delete_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> int:
        raise NotImplementedError("The delete_one function not implemented.")

    @property
    @abstractclassmethod
    def tables(self):
        raise NotImplementedError("The tables property was not implemented")

    @abstractclassmethod
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
        raise NotImplementedError("The _execute_sql method was not implemented.")

    def connect(
        self,
    ) -> Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection:
        raise NotImplementedError("The connect method was not implemented.")

    def connect_and_sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> tuple[
        Any | PooledMySQLConnection | MySQLConnectionAbstract | Connection, list[str]
    ]:
        raise NotImplementedError("The connect_and_sync method was not created.")

    @abstractclassmethod
    def sync(
        self, models: list[Model], drop=False, force=False, alter=False
    ) -> list[str]:
        raise NotImplementedError("The sync method was not implemented.")
