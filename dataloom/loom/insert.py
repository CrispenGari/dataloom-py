from dataloom.model import Model
from dataloom.types import ColumnValue
from dataloom.types import DIALECT_LITERAL
from typing import Callable, Any
from dataloom.exceptions import InvalidColumnValuesException
from dataloom.utils import get_insert_bulk_attrs, is_collection
from abc import ABC, abstractclassmethod


class Insert(ABC):
    @abstractclassmethod
    def insert_one(
        self, instance: Model, values: ColumnValue | list[ColumnValue]
    ) -> Any:
        raise NotImplementedError("The insert_one method was not implemented.")

    @abstractclassmethod
    def insert_bulk(self, instance: Model, values: list[list[ColumnValue]]) -> int:
        raise NotImplementedError("The insert_bulk method was not implemented.")


class insert(Insert):
    def __init__(
        self, dialect: DIALECT_LITERAL, _execute_sql: Callable[..., Any]
    ) -> None:
        self._execute_sql = _execute_sql
        self.dialect = dialect

    def insert_one(
        self, instance: Model, values: ColumnValue | list[ColumnValue]
    ) -> Any:
        sql, values = instance._get_insert_one_stm(dialect=self.dialect, values=values)
        row = self._execute_sql(
            sql,
            args=tuple(values),
            fetchone=self.dialect == "postgres",
            operation="insert",
        )
        return row[0] if type(row) in [list, tuple] else row

    def insert_bulk(self, instance: Model, values: list[list[ColumnValue]]) -> int:
        # ? ensure that the values that are passed is a list of a list and they inner list have the same length
        if not is_collection(values):
            raise InvalidColumnValuesException(
                "The insert_bulk method takes in values as lists of lists."
            )
        all_list = [is_collection(v) for v in values]
        if not all(all_list):
            raise InvalidColumnValuesException(
                "The insert_bulk method takes in values as lists of lists."
            )
        lengths = [len(v) for v in values]
        _max = max(lengths)
        if not all([_max == v for v in lengths]):
            raise InvalidColumnValuesException(
                "The insert_bulk method takes in values as lists of lists with equal ColumnValues."
            )

        columns = None
        placeholders = None
        data = []
        for _value in values:
            (column_names, placeholder_values, _values) = get_insert_bulk_attrs(
                dialect=self.dialect, instance=instance, values=_value
            )
            if columns is None:
                columns = column_names
            if placeholders is None:
                placeholders = placeholder_values
            data.append(_values)

        sql = instance._get_insert_bulk_smt(
            dialect=self.dialect, column_names=columns, placeholder_values=placeholders
        )

        row_count = self._execute_sql(sql, args=tuple(data), fetchall=True, bulk=True)
        return row_count
