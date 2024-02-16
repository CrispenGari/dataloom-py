from dataloom.model import Model
from dataloom.types import Filter, Order, Include
from dataloom.types import DIALECT_LITERAL
from typing import Callable, Any, Optional
from dataloom.utils import get_child_table_columns, get_args
from abc import ABC, abstractclassmethod
from dataloom.loom.subqueries import subquery


class Query(ABC):
    @abstractclassmethod
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
        raise NotImplementedError("The find_many method was not implemented.")

    @abstractclassmethod
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
        raise NotImplementedError("The find_all method was not implemented.")

    @abstractclassmethod
    def find_by_pk(
        self,
        instance: Model,
        pk,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
    ) -> dict | None:
        raise NotImplementedError("The find_by_pk method was not implemented.")

    @abstractclassmethod
    def find_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
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
        select: list[str] = [],
        include: list[Model] = [],
        return_dict: bool = True,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ) -> list:
        return_dict = True
        include = []
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
        args = get_args(params)
        rows = self._execute_sql(sql, fetchall=True, args=args)
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
        include = []
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
        include: list[dict] = [],
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
    ) -> dict | None:
        # """
        # This part will be added in the future version.
        # """
        return_dict = True

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
        select: list[str] = [],
        include: list[Include] = [],
        return_dict: bool = True,
        offset: Optional[int] = None,
    ) -> dict | None:
        return_dict = True
        sql, params, fields = instance._get_select_where_stm(
            dialect=self.dialect,
            filters=filters,
            select=select,
            offset=offset,
            include=[],
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
