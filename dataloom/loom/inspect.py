from dataloom.model import Model
from dataloom.exceptions import UnknownColumnException
from dataloom.utils import print_pretty_table
from dataloom.types import DIALECT_LITERAL
from typing import Callable, Any
from abc import ABC, abstractclassmethod


class Inspect(ABC):
    @abstractclassmethod
    def inspect(
        self,
        instance: Model,
        fields: list[str] = ["name", "type", "nullable", "default"],
        print_table: bool = True,
    ) -> list[dict] | None:
        raise NotImplementedError("The inspect method was not implemented.")


class inspect(Inspect):
    def __init__(
        self, dialect: DIALECT_LITERAL, database: str, _execute_sql: Callable[..., Any]
    ) -> None:
        self.dialect = dialect
        self.database = database
        self._execute_sql = _execute_sql

    def inspect(
        self,
        instance: Model,
        fields: list[str] = ["name", "type", "nullable", "default"],
        print_table: bool = True,
    ) -> list[dict] | None:
        # The column name should be first and required.
        allowed = {
            "name": "column_name",
            "type": "data_type",
            "nullable": "is_nullable",
            "default": "column_default",
        }
        modified_fields = ["column_name"]
        for field in fields:
            if field not in allowed.keys():
                raise UnknownColumnException(
                    f"You can not select '{field}' when inspecting table '{instance._get_table_name()}' allowed fields are ({', '.join(allowed.keys())})."
                )
            else:
                cl_name = allowed.get(field)
                if cl_name not in modified_fields:
                    modified_fields.append(cl_name)

        sql = instance._get_describe_stm(dialect=self.dialect, fields=modified_fields)
        args = None
        if self.dialect == "mysql":
            args = (self.database, instance._get_table_name())
        elif self.dialect == "postgres":
            args = ("public", instance._get_table_name())
        elif self.dialect == "sqlite":
            args = ()

        rows = self._execute_sql(sql, args=args, fetchall=True)

        if print_table:
            headers = ["name"]
            for header in fields:
                if header not in headers:
                    headers.append(header)
            if self.dialect == "sqlite":
                _rows = [row[1 : 1 + len(headers)] for row in rows]
                print_pretty_table(headers, _rows)
            else:
                print_pretty_table(headers, rows)
            return None
        description = []
        for row in rows:
            if self.dialect == "sqlite":
                column_name = row[1]
                val = dict(zip(fields[1:], row[2:]))
            else:
                val = dict(zip(fields[1:], row[1:]))
                column_name = row[0]
            obj = {column_name: val}
            description.append(obj)
        return description
