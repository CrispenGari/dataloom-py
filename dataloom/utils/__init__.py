from datetime import datetime
import inspect
from dataloom.columns import (
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
)
from dataloom.types import (
    Include,
    DIALECT_LITERAL,
    OPERATOR_LITERAL,
    SLQ_OPERATORS,
    Filter,
    ColumnValue,
)
from dataloom.exceptions import InvalidOperatorException, UnknownColumnException
from typing import Optional
from dataloom.statements import MySqlStatements, PgStatements, Sqlite3Statements


class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"


def get_table_filters(
    table_name: str,
    dialect: DIALECT_LITERAL,
    filters: Optional[Filter | list[Filter]],
    fields: list[str],
):
    placeholder_filter_values = []
    placeholder_filters = []
    if filters is not None:
        if isinstance(filters, list):
            for idx, filter in enumerate(filters):
                key = filter.column
                if key not in fields:
                    raise UnknownColumnException(
                        f"Table {table_name} does not have column '{key}'."
                    )
                op = get_operator(filter.operator)
                join = (
                    ""
                    if len(filters) == idx + 1
                    else f" {filter.join_next_filter_with}"
                )
                _key = (
                    f'"{key}" {op} %s {join}'
                    if dialect == "postgres"
                    else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'} {join}"
                )
                placeholder_filter_values.append(filter.value)
                placeholder_filters.append(_key)
        else:
            filter = filters
            key = filter.column
            if key not in fields:
                raise UnknownColumnException(
                    f"Table {table_name} does not have column '{key}'."
                )
            op = get_operator(filter.operator)
            _key = (
                f'"{key}" {op} %s'
                if dialect == "postgres"
                else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'}"
            )
            placeholder_filter_values.append(filter.value)
            placeholder_filters.append(_key)
    return placeholder_filters, placeholder_filter_values


def get_column_values(
    table_name: str,
    dialect: DIALECT_LITERAL,
    values: ColumnValue | list[ColumnValue],
    fields: list[str],
):
    column_values = []
    placeholders_of_column_values = []

    if values is not None:
        if isinstance(values, list):
            for value in values:
                key = value.name
                v = value.value
                if key in fields:
                    _key = (
                        f'"{key}" = %s'
                        if dialect == "postgres"
                        else f"`{
                key}` = {'%s' if dialect == 'mysql' else '?'}"
                    )
                    placeholders_of_column_values.append(_key)
                    column_values.append(v)
                else:
                    raise UnknownColumnException(
                        f"Table {table_name} does not have column '{key}'."
                    )
        else:
            value = values
            key = value.name
            v = value.value
            if key in fields:
                _key = (
                    f'"{key}" = %s'
                    if dialect == "postgres"
                    else f"`{
            key}` = {'%s' if dialect == 'mysql' else '?'}"
                )
                placeholders_of_column_values.append(_key)
                column_values.append(v)
            else:
                raise UnknownColumnException(
                    f"Table {table_name} does not have column '{key}'."
                )
    return placeholders_of_column_values, column_values


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


class logger:
    @staticmethod
    def file(fn):
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

    @staticmethod
    def console(fn):
        def wrapper(*args, **kwargs):
            index, sql_statement, dialect = fn(*args, **kwargs)
            if index % 2 == 0:
                print(
                    Colors.BOLD
                    + Colors.CYAN
                    + f"[{dialect}:log_{index}] "
                    + Colors.RESET
                    + Colors.BOLD
                    + Colors.BLUE
                    + f"{sql_statement}"
                    + Colors.RESET
                )
            else:
                print(
                    Colors.BOLD
                    + Colors.CYAN
                    + f"[{dialect}:log_{index}] "
                    + Colors.RESET
                    + Colors.BOLD
                    + Colors.GREEN
                    + f"{sql_statement}"
                    + Colors.RESET
                )

            print()
            return index

        return wrapper


@logger.file
def file_logger(file_name: str, dialect: DIALECT_LITERAL, sql_statement: str) -> None:
    return sql_statement, file_name, dialect


@logger.console
def console_logger(
    index: int,
    sql_statement: str,
    dialect: DIALECT_LITERAL,
):
    return index, sql_statement, dialect


def get_table_fields(model, dialect: DIALECT_LITERAL):
    pk_name = None
    updatedAtColumName = None
    fields = []
    fks = dict()
    for name, field in inspect.getmembers(model):
        if isinstance(field, Column):
            fields.append(name)
        elif isinstance(field, ForeignKeyColumn):
            fields.append(name)
            table_name = field.table._get_table_name()
            fks[table_name] = name
        elif isinstance(field, PrimaryKeyColumn):
            fields.append(name)
            pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
        elif isinstance(field, CreatedAtColumn):
            fields.append(name)
        elif isinstance(field, UpdatedAtColumn):
            fields.append(name)
            updatedAtColumName = f'"{name}"' if dialect == "postgres" else f"`{name}`"

    return fields, pk_name, fks, updatedAtColumName


def get_relationships(includes, fks):
    relationships = []
    for include in includes:
        table = include["table"]
        relationships.append(
            {
                "table_name": table,
                "fk": fks[table],
                "pk_name": include["pk_name"],
                "alias": "child_" + include["alias"],
                "columns": include["fields"]
                if len(include["select"]) == 0
                else include["select"],
            }
        )
    return relationships


def get_child_table_params(include: Include, dialect: DIALECT_LITERAL):
    fields = []
    filters = []
    limit = include.limit
    offset = include.offset
    orders = None
    select = include.select
    pk_name = None
    table__name = include.model._get_table_name()
    alias = include.model.__name__.lower()
    fields, pk_name, fks, _ = get_table_fields(include.model, dialect=dialect)

    for column in select:
        if column not in fields:
            raise UnknownColumnException(
                f'The table "{table__name}" does not have a column "{column}".'
            )

    return {
        "alias": alias,
        "fields": fields,
        "filters": filters,
        "offset": offset,
        "limit": limit,
        "orders": orders,
        "select": select,
        "table": table__name,
        "pk_name": pk_name,
    }


def get_formatted_query(
    dialect=str,
    table_names: dict = {},
    relationships: list = [],
    filters: list[str] = [],
    options: list[str] = [],
):
    joins = []
    parent_columns = ", ".join(
        [
            f'parent.{f'"{col}"' if dialect== 'postgres' else f'`{col}`' } AS {f"`{table_names['parent_table_name']}_{col}`" if dialect != "postgres" else f"\"{table_names['parent_table_name']}_{col}\""}'
            for col in table_names["parent_columns"]
        ]
    )
    child_columns = []
    for rel in relationships:
        joins.append(
            f'JOIN {rel['table_name']} {rel['alias']} ON parent.{f'"{rel['fk']}"' if dialect=='postgres' else f'`{rel['fk']}`'  } = {rel['alias']}.{rel['pk_name']} '
        )
        child_columns.append(
            ", ".join(
                [
                    f'{rel['alias']}.{f'"{col}"' if dialect== 'postgres' else f'`{col}`'} AS {f"`{rel['table_name']}_{col}`" if dialect != "postgres" else f"\"{rel['table_name']}_{col}\""}'
                    for col in rel["columns"]
                ]
            )
        )
    if len(options) == 0:
        if dialect == "postgres":
            sql = PgStatements.SELECT_BY_PK_INCLUDE_COMMAND.format(
                parent_columns=parent_columns,
                child_columns=", ".join(child_columns),
                parent_table_name=table_names["parent_table_name"],
                joins="".join(joins),
                parent_pk_name=table_names["parent_pk_name"],
                parent_pk=table_names["parent_pk"],
            )
        elif dialect == "mysql":
            sql = MySqlStatements.SELECT_BY_PK_INCLUDE_COMMAND.format(
                parent_columns=parent_columns,
                child_columns=", ".join(child_columns),
                parent_table_name=table_names["parent_table_name"],
                joins="".join(joins),
                parent_pk_name=table_names["parent_pk_name"],
                parent_pk=table_names["parent_pk"],
            )
        elif dialect == "sqlite":
            sql = Sqlite3Statements.SELECT_BY_PK_INCLUDE_COMMAND.format(
                parent_columns=parent_columns,
                child_columns=", ".join(child_columns),
                parent_table_name=table_names["parent_table_name"],
                joins="".join(joins),
                parent_pk_name=table_names["parent_pk_name"],
                parent_pk=table_names["parent_pk"],
            )
    else:
        if len(filters) == 0:
            if dialect == "postgres":
                sql = PgStatements.SELECT_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    options=" ".join(options),
                )
            elif dialect == "mysql":
                sql = MySqlStatements.SELECT_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    options=" ".join(options),
                )
            elif dialect == "sqlite":
                sql = Sqlite3Statements.SELECT_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    options=" ".join(options),
                )
        else:
            if dialect == "postgres":
                sql = PgStatements.SELECT_WHERE_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    filters=" ".join([f"parent.{f}" for f in filters]),
                    options=" ".join(options),
                )
            elif dialect == "mysql":
                sql = MySqlStatements.SELECT_WHERE_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    filters=" ".join([f"parent.{f}" for f in filters]),
                    options=" ".join(options),
                )
            elif dialect == "sqlite":
                sql = Sqlite3Statements.SELECT_WHERE_INCLUDE_COMMAND.format(
                    parent_columns=parent_columns,
                    child_columns=", ".join(child_columns),
                    parent_table_name=table_names["parent_table_name"],
                    joins="".join(joins),
                    filters=" ".join([f"parent.{f}" for f in filters]),
                    options=" ".join(options),
                )

    return sql
