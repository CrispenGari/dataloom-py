from datetime import datetime
import inspect
from dataloom.columns import (
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
)
from dataloom.types import Include, DIALECT_LITERAL, OPERATOR_LITERAL, SLQ_OPERATORS
from dataloom.exceptions import InvalidOperatorException


def get_operator(op: OPERATOR_LITERAL) -> str:
    if op not in SLQ_OPERATORS:
        raise InvalidOperatorException(
            f"The operator '{op}' is not supported by dataloom, suported operators are ({', '.join(SLQ_OPERATORS.keys())})."
        )
    return SLQ_OPERATORS[op]


def get_child_table_columns(include: Include) -> dict:
    fields = []
    alias = include.model.__name__.lower()
    select = include.select
    for (
        name,
        field,
    ) in inspect.getmembers(include.model):
        if isinstance(field, Column):
            fields.append(name)
        elif isinstance(field, ForeignKeyColumn):
            fields.append(name)
        elif isinstance(field, PrimaryKeyColumn):
            fields.append(name)

        elif isinstance(field, CreatedAtColumn):
            fields.append(name)
        elif isinstance(field, UpdatedAtColumn):
            fields.append(name)
    return {alias: field if len(select) == 0 else select}


def logger(fn):
    def wrapper(*args, **kwargs):
        sql_statement, file_name, dialect = fn(*args, **kwargs)
        with open(file_name, "a+") as f:
            f.write(
                "[{time}] : Dataloom[{dialect}]: {sql_statement}\n".format(
                    dialect=dialect,
                    time=datetime.now(),
                    sql_statement=sql_statement,
                )
            )
        return sql_statement

    return wrapper


@logger
def logger_function(
    file_name: str, dialect: DIALECT_LITERAL, sql_statement: str
) -> None:
    return sql_statement, file_name, dialect
