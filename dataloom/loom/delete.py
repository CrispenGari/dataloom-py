from dataloom.exceptions import InvalidArgumentsException
from dataloom.model import Model
from typing import Optional, Callable, Any
from dataloom.types import Filter, DIALECT_LITERAL, Order
from dataloom.utils import get_args


class delete:
    def __init__(
        self, dialect: DIALECT_LITERAL, _execute_sql: Callable[..., Any]
    ) -> None:
        self._execute_sql = _execute_sql
        self.dialect = dialect

    def delete_by_pk(self, instance: Model, pk):
        sql = instance._get_delete_by_pk_stm(dialect=self.dialect)
        affected_rows = self._execute_sql(
            sql, args=(pk,), affected_rows=True, fetchall=True
        )
        return affected_rows

    def delete_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = [],
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        sql, params = instance._get_delete_where_stm(
            dialect=self.dialect, filters=filters, offset=offset, order=order
        )

        args = [*get_args(params)]

        if offset is not None:
            args.append(offset)
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def delete_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[list[Order]] = [],
    ):
        if offset is not None and limit is None and self.dialect == "mysql":
            raise InvalidArgumentsException(
                f"You can not apply offset without limit on dialect '{self.dialect}'."
            )
        sql, params = instance._get_delete_bulk_where_stm(
            dialect=self.dialect,
            filters=filters,
            offset=offset,
            limit=limit,
            order=order,
        )
        args = [*get_args(params)]

        if limit is not None:
            args.append(limit)
        if offset is not None:
            args.append(offset)

        affected_rows = self._execute_sql(
            sql, args=args, affected_rows=True, fetchall=True
        )
        return affected_rows
