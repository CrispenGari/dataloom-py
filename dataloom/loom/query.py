from dataloom.model import Model
from dataloom.types import Filter, Order, Include, Group, DIALECT_LITERAL
from typing import Callable, Any, Optional
from dataloom.utils import get_args, is_collection
from abc import ABC, abstractclassmethod
from dataloom.loom.subqueries import subquery


class Query(ABC):
    @abstractclassmethod
    def find_many(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: list[Model] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ) -> list:
        raise NotImplementedError("The find_many method was not implemented.")

    @abstractclassmethod
    def find_all(
        self,
        instance: Model,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
    ) -> list:
        raise NotImplementedError("The find_all method was not implemented.")

    @abstractclassmethod
    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
    ) -> dict | None:
        raise NotImplementedError("The find_by_pk method was not implemented.")

    @abstractclassmethod
    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        offset: Optional[int] = None,
    ) -> dict | None:
        raise NotImplementedError("The find_one method was not implemented.")


class query(Query):
    def __init__(
        self, dialect: DIALECT_LITERAL, _execute_sql: Callable[..., Any]
    ) -> None:
        self._execute_sql = _execute_sql
        self.dialect = dialect

    def find_many(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: list[Model] = [],
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ) -> list:
        data = []

        if not is_collection(include):
            include = [include]
        if not is_collection(group):
            group = [group]

        if len(include) == 0:
            sql, params, fields, having_values = instance._get_select_where_stm(
                dialect=self.dialect,
                filters=filters,
                select=select,
                limit=limit,
                offset=offset,
                order=order,
                group=group,
            )
            args = list(get_args(params)) + having_values
            rows = self._execute_sql(sql, fetchall=True, args=args)
            for row in rows:
                d = dict(zip(fields, row))
                data.append(d)
        else:
            # run sub queries instead
            data = subquery(
                dialect=self.dialect, _execute_sql=self._execute_sql
            ).get_find_many_relations(
                parent=instance,
                includes=include,
                filters=filters,
                select=select,
                limit=limit,
                order=order,
                offset=offset,
                group=group,
            )
        return data

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
        data = []
        if not is_collection(include):
            include = [include]
        if not is_collection(group):
            group = [group]

        if len(include) == 0:
            sql, params, fields, having_values = instance._get_select_where_stm(
                dialect=self.dialect,
                select=select,
                limit=limit,
                offset=offset,
                order=order,
                group=group,
            )
            args = list(get_args(params)) + having_values
            rows = self._execute_sql(sql, fetchall=True, args=args)
            for row in rows:
                data.append(dict(zip(fields, row)))
        else:
            # run sub queries instead
            data = subquery(
                dialect=self.dialect, _execute_sql=self._execute_sql
            ).get_find_all_relations(
                parent=instance,
                includes=include,
                select=select,
                limit=limit,
                order=order,
                offset=offset,
                group=group,
            )
        return data

    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
    ) -> dict | None:
        # what is the name of the primary key column? well we will find out
        sql, fields, _includes = instance._get_select_by_pk_stm(
            dialect=self.dialect, select=select, include=[]
        )
        rows = self._execute_sql(sql, args=(pk,), fetchone=True)
        if rows is None:
            return None
        result = dict(zip(fields, rows))
        relations = subquery(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).get_find_by_pk_relations(parent=instance, includes=include, pk=pk)
        return {**result, **relations}

    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: Optional[list[str] | str] = [],
        include: Optional[list[Include] | Include] = [],
        offset: Optional[int] = None,
    ) -> dict | None:
        sql, params, fields, having_values = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=select,
            offset=offset,
        )

        args = get_args(params)
        row = self._execute_sql(sql, args=args, fetchone=True)
        if row is None:
            return None
        result = dict(zip(fields, row))
        relations = subquery(
            dialect=self.dialect, _execute_sql=self._execute_sql
        ).get_find_one_relations(
            parent=instance,
            includes=include,
            filters=filters,
            offset=offset,
        )
        return {**result, **relations}
