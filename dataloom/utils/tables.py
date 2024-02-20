import inspect
from dataloom.utils.helpers import is_collection
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
from dataloom.exceptions import (
    InvalidOperatorException,
    UnknownColumnException,
    InvalidFilterValuesException,
)
from typing import Optional


def get_table_filters(
    table_name: str,
    dialect: DIALECT_LITERAL,
    filters: Optional[Filter | list[Filter]],
    fields: list[str],
):
    placeholder_filter_values = []
    placeholder_filters = []
    if filters is not None:
        if is_collection(filters):
            for idx, filter in enumerate(filters):
                key = filter.column
                if key not in fields:
                    raise UnknownColumnException(
                        f"Table {table_name} does not have column '{key}'."
                    )
                op = get_operator(filter.operator)
                join = "" if len(filters) == idx + 1 else f" {filter.join_next_with}"

                if op == "IN" or op == "NOT IN":
                    if is_collection(filter.value):
                        _list = ", ".join(
                            ["?" if dialect == "sqlite" else "%s" for i in filter.value]
                        )
                        _key = (
                            f'"{key}" {op} ({_list}) {join}'
                            if dialect == "postgres"
                            else f"`{key}` {op} ({_list}) {join}"
                        )
                    else:
                        raise InvalidFilterValuesException(
                            f'The column "{filter.column}" value can only be a list, tuple or dictionary but got {type(filter.value)} .'
                        )
                else:
                    if not is_collection(filter.value):
                        _key = (
                            f'"{key}" {op} %s {join}'
                            if dialect == "postgres"
                            else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'} {join}"
                        )
                    else:
                        raise InvalidFilterValuesException(
                            f'The column "{filter.column}" value can not be a collection.'
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
            if op == "IN" or op == "NOT IN":
                if is_collection(filter.value):
                    _list = ", ".join(
                        ["?" if dialect == "sqlite" else "%s" for i in filter.value]
                    )
                    _key = (
                        f'"{key}" {op} ({_list})'
                        if dialect == "postgres"
                        else f"`{key}` {op} ({_list})"
                    )
                else:
                    raise InvalidFilterValuesException(
                        f'The column "{filter.column}" value can only be a list, tuple or dictionary but got {type(filter.value)} .'
                    )
            else:
                if not is_collection(filter.value):
                    _key = (
                        f'"{key}" {op} %s'
                        if dialect == "postgres"
                        else f"`{key}` {op} {'%s' if dialect == 'mysql' else '?'}"
                    )
                else:
                    raise InvalidFilterValuesException(
                        f'The column "{filter.column}" value can not be a collection.'
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
    column_names = []

    if values is not None:
        if is_collection(values):
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
                    column_names.append(key)
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
                column_names.append(key)
                column_values.append(v)
            else:
                raise UnknownColumnException(
                    f"Table {table_name} does not have column '{key}'."
                )
    return placeholders_of_column_values, column_values, column_names


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


def get_table_fields(model, dialect: DIALECT_LITERAL):
    pk_name = None
    updatedAtColumName = None
    fields = []
    fks = []
    for name, field in inspect.getmembers(model):
        if isinstance(field, Column):
            fields.append(name)
        elif isinstance(field, ForeignKeyColumn):
            fields.append(name)
            table_name = field.table._get_table_name()
            fks.append({table_name: name, "mapped_to": field.maps_to})
        elif isinstance(field, PrimaryKeyColumn):
            fields.append(name)
            pk_name = f'"{name}"' if dialect == "postgres" else f"`{name}`"
        elif isinstance(field, CreatedAtColumn):
            fields.append(name)
        elif isinstance(field, UpdatedAtColumn):
            fields.append(name)
            updatedAtColumName = f'"{name}"' if dialect == "postgres" else f"`{name}`"

    return fields, pk_name, fks, updatedAtColumName


def get_relationships(
    includes: list[dict], fks: dict, parent_table_name: str | None = None
):
    relationships = []
    for include in includes:
        if parent_table_name is not None:
            fks = include["foreign_keys"]
            table = include["table"]
            relationships.append(
                {
                    "table_name": table,
                    "fk": fks[parent_table_name],
                    "pk_name": include["pk_name"],
                    "alias": "child_" + include["alias"],
                    "columns": include["fields"]
                    if len(include["select"]) == 0
                    else include["select"],
                }
            )

        else:
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
    table_name = include.model._get_table_name()
    alias = include.model.__name__.lower()
    fields, pk_name, fks, _ = get_table_fields(include.model, dialect=dialect)

    for column in select:
        if column not in fields:
            raise UnknownColumnException(
                f'The table "{table_name}" does not have a column "{column}".'
            )

    return {
        "alias": alias,
        "fields": fields,
        "filters": filters,
        "offset": offset,
        "limit": limit,
        "orders": orders,
        "select": select,
        "table": table_name,
        "pk_name": pk_name,
        "foreign_keys": fks,
        "maps_to": include.maps_to,
    }


def get_null_field_placeholder(
    column: str,
    dialect: DIALECT_LITERAL,
    table_name: str,
    pk_name: str,
) -> str:
    if dialect == "mysql":
        value = f"IFNULL(%s, DEFAULT(`{column}`))"
    if dialect == "sqlite":
        value = "?"
    if dialect == "postgres":
        value = f"""COALESCE(%s, DEFAULT("{column}"))"""
    return value


def get_insert_bulk_attrs(
    instance,
    dialect: DIALECT_LITERAL,
    values: list[ColumnValue] | ColumnValue,
):
    fields, pk_name, fks, updatedAtColumName = get_table_fields(
        instance, dialect=dialect
    )

    placeholders, column_values, column_names = get_column_values(
        table_name=instance._get_table_name(),
        dialect=dialect,
        fields=fields,
        values=values,
    )

    _placeholders = ", ".join(
        ["?" if dialect == "sqlite" else "%s" for f in column_names]
    )
    _column_names = ", ".join(
        [f'"{f}"' if dialect == "postgres" else f"`{f}`" for f in column_names]
    )
    return (_column_names, _placeholders, column_values)
