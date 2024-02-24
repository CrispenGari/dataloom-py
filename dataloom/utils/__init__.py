from dataloom.statements import MySqlStatements, PgStatements, Sqlite3Statements

from dataloom.utils.logger import console_logger, file_logger
from dataloom.utils.create_table import get_create_table_params
from dataloom.utils.alter_table import AlterTable
from dataloom.utils.aggregations import get_groups
from dataloom.utils.helpers import is_collection
from dataloom.utils.tables import (
    get_child_table_columns,
    get_child_table_params,
    get_insert_bulk_attrs,
    get_null_field_placeholder,
    get_operator,
    get_table_fields,
    get_table_filters,
    get_relationships,
    get_column_values,
)
from dataloom.utils.loom import get_args
from dataloom.utils.table import print_pretty_table


def get_formatted_query(
    dialect=str,
    table_names: dict = {},
    relationships: list = [],
    filters: list[str] = [],
    options: list[str] = [],
    from_parent: bool = False,
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
        if not from_parent:
            joins.append(
                f"""
                JOIN {rel['table_name']} {rel['alias']} 
                    ON parent.{f'"{rel['fk']}"' if dialect=='postgres' else f'`{rel['fk']}`'  } = {rel['alias']}.{rel["pk_name"]}
                """.strip()
            )
        else:
            joins.append(
                f"""
                LEFT JOIN {rel['table_name']} {rel['alias']} 
                    ON parent.{f'"{rel['pk_name']}"' if dialect=='postgres' else f'{rel['pk_name']}'  } = {rel['alias']}.{f'"{rel["fk"]}"' if dialect == 'postgres' else f'`{rel["fk"]}`' }
                """.strip()
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


__all__ = [
    get_child_table_columns,
    get_child_table_params,
    get_insert_bulk_attrs,
    get_null_field_placeholder,
    get_operator,
    get_table_fields,
    get_table_filters,
    get_relationships,
    get_column_values,
    console_logger,
    file_logger,
    get_create_table_params,
    get_args,
    print_pretty_table,
    is_collection,
    get_groups,
    AlterTable,
]
