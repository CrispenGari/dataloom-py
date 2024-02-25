from dataloom.model import Model
from dataloom.types import Filter, DIALECT_LITERAL
from typing import Callable, Any, Optional
from dataloom.utils import get_args
from abc import ABC, abstractclassmethod


class Math(ABC):
    @abstractclassmethod
    def sum(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int | float:
        raise NotImplementedError("The sum method was not implemented.")

    @abstractclassmethod
    def max(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int | float:
        raise NotImplementedError("The max method was not implemented.")

    @abstractclassmethod
    def min(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int | float:
        raise NotImplementedError("The min method was not implemented.")

    def count(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int:
        raise NotImplementedError("The count method was not implemented.")

    def avg(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int | float:
        raise NotImplementedError("The count method was not implemented.")


class math(Math):
    def __init__(
        self, dialect: DIALECT_LITERAL, _execute_sql: Callable[..., Any]
    ) -> None:
        self._execute_sql = _execute_sql
        self.dialect = dialect

    def sum(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> float | int:
        sql, params, _, _ = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=column,
            offset=offset,
            distinct=distinct,
            limit=limit,
            function="sum",
        )
        args = list(get_args(params))
        row = self._execute_sql(sql, fetchone=True, args=args)
        return 0 if row is None else row[0]

    def count(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> int:
        sql, params, _, _ = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=column,
            offset=offset,
            distinct=distinct,
            limit=limit,
            function="count",
        )
        args = list(get_args(params))
        row = self._execute_sql(sql, fetchone=True, args=args)
        return 0 if row is None else row[0]

    def avg(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> float:
        sql, params, _, _ = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=column,
            offset=offset,
            distinct=distinct,
            limit=limit,
            function="avg",
        )
        args = list(get_args(params))
        row = self._execute_sql(sql, fetchone=True, args=args)
        return 0.0 if row is None else row[0]

    def max(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> float | int:
        sql, params, _, _ = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=column,
            offset=offset,
            distinct=distinct,
            limit=limit,
            function="max",
        )
        args = list(get_args(params))
        row = self._execute_sql(sql, fetchone=True, args=args)
        return 0 if row is None else row[0]

    def min(
        self,
        instance: Model,
        column: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        distinct: bool = False,
        filters: Optional[Filter | list[Filter]] = None,
    ) -> float | int:
        sql, params, _, _ = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=column,
            offset=offset,
            distinct=distinct,
            limit=limit,
            function="min",
        )
        args = list(get_args(params))
        row = self._execute_sql(sql, fetchone=True, args=args)
        return 0 if row is None else row[0]
