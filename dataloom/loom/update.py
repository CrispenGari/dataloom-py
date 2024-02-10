from dataloom.exceptions import InvalidColumnValuesException
from dataloom.model import Model
from typing import Optional, Callable, Any
from dataloom.types import ColumnValue, Filter, DIALECT_LITERAL
from dataloom.utils import get_args


class update:
    def __init__(
        self, dialect: DIALECT_LITERAL, _execute_sql: Callable[..., Any]
    ) -> None:
        self._execute_sql = _execute_sql
        self.dialect = dialect

    def increment(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ):
        if isinstance(column.value, float) or isinstance(column.value, int):
            sql, column_values, filter_values = instance._get_increment_decrement_stm(
                dialect=self.dialect,
                filters=filters,
                value=column,
                operator="increment",
            )
        else:
            raise InvalidColumnValuesException(
                "The increment operation only works with integer and float values."
            )
        args = [*column_values, *get_args(filter_values)]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def decrement(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        column: ColumnValue[int | float],
    ):
        if isinstance(column.value, float) or isinstance(column.value, int):
            sql, column_values, filter_values = instance._get_increment_decrement_stm(
                dialect=self.dialect,
                filters=filters,
                value=column,
                operator="decrement",
            )
        else:
            raise InvalidColumnValuesException(
                "The decrement operation only works with integer and float values."
            )
        args = [*column_values, *get_args(filter_values)]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def update_by_pk(
        self, instance: Model, pk, values: ColumnValue | list[ColumnValue]
    ):
        sql, args = instance._get_update_by_pk_stm(dialect=self.dialect, values=values)
        args.append(pk)
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def update_one(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        sql, new_values, filter_values = instance._get_update_one_stm(
            dialect=self.dialect, filters=filters, values=values
        )
        args = [*new_values, *get_args(filter_values)]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows

    def update_bulk(
        self,
        instance: Model,
        filters: Optional[Filter | list[Filter]],
        values: ColumnValue | list[ColumnValue],
    ):
        sql, new_values, filter_values = instance._get_update_bulk_where_stm(
            dialect=self.dialect, filters=filters, values=values
        )
        args = [*new_values, *get_args(filter_values)]
        affected_rows = self._execute_sql(sql, args=args, affected_rows=True)
        return affected_rows
