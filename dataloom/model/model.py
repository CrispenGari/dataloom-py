from typing import Any
from dataloom.model.column import (
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
)
from dataloom.model.statements import PgStatements
from dataloom.exceptions import *
import inspect
from datetime import datetime
import re


class Model:

    @classmethod
    def _get_delete_by_pk_stm(cls, pk, pk_name: str = "id"):
        sql = PgStatements.DELETE_BY_PK.format(
            table_name=cls._get_name(),
            pk="%s",  # mask it to avoid SQL Injection
            pk_name=pk_name,
        )
        return sql, pk

    @classmethod
    def _get_delete_where_stm(cls, pk: str = "id", args: dict = {}):
        params = []
        filters = []
        for key, value in args.items():
            filters.append(f"{key} = %s")
            params.append(value)
        if len(filters) == 0:
            sql = PgStatements.DELETE_ALL_COMMAND.format(
                table_name=cls._get_name(),
            )
        else:
            sql = PgStatements.DELETE_ONE_WHERE_COMMAND.format(
                table_name=cls._get_name(), filters=" AND ".join(filters), pk_name=pk
            )
        return sql, params

    @classmethod
    def _get_delete_bulk_where_stm(cls, args: dict = {}):
        params = []
        filters = []
        for key, value in args.items():
            filters.append(f"{key} = %s")
            params.append(value)
        if len(filters) == 0:
            sql = PgStatements.DELETE_ALL_COMMAND.format(
                table_name=cls._get_name(),
            )
        else:
            sql = PgStatements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=cls._get_name(),
                filters=" AND ".join(filters),
            )
        return sql, params

    @classmethod
    def _get_update_one_stm(
        cls, pk_name: str = "", filters: dict = {}, args: dict = {}
    ):
        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, UpdatedAtColumn):
                updatedAtColumName = name

        values = list()
        placeholder_values = list()
        placeholder_filters = list()

        for key, value in args.items():
            placeholder_values.append(f'"{key}" = %s')
            values.append(value)

        for key, value in filters.items():
            placeholder_filters.append([f"{key} = %s", value])

        if updatedAtColumName is not None:
            placeholder_values.append(f'"{updatedAtColumName}" = %s')
            values.append(current_time_stamp)

        sql = PgStatements.UPDATE_BY_ONE_COMMAND.format(
            table_name=cls._get_name(),
            pk_name=pk_name,
            placeholder_values=", ".join(placeholder_values),
            placeholder_filters=", ".join([i[0] for i in placeholder_filters]),
        )
        return sql, values, [i[1] for i in placeholder_filters]

    @classmethod
    def _get_update_bulk_where_stm(cls, filters: dict = {}, args: dict = {}):
        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, UpdatedAtColumn):
                updatedAtColumName = name

        values = list()
        placeholder_values = list()
        placeholder_filters = list()

        for key, value in args.items():
            placeholder_values.append(f'"{key}" = %s')
            values.append(value)

        for key, value in filters.items():
            placeholder_filters.append([f"{key} = %s", value])

        if updatedAtColumName is not None:
            placeholder_values.append(f'"{updatedAtColumName}" = %s')
            values.append(current_time_stamp)

        sql = PgStatements.UPDATE_BULK_WHERE_COMMAND.format(
            table_name=cls._get_name(),
            placeholder_values=", ".join(placeholder_values),
            placeholder_filters=", ".join([i[0] for i in placeholder_filters]),
        )
        return sql, values, [i[1] for i in placeholder_filters]
