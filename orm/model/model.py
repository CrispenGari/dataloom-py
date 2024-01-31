from typing import Any
from orm.model.column import (
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
)
from orm.model.statements import Statements
from orm.exceptions import *
import inspect
from datetime import datetime
import re


# constants

current_time_stamp = datetime.now()


class Model:
    def __init__(self, **args) -> None:
        self._data = {}
        for k, v in args.items():
            self._data[k] = v

    def __getattribute__(self, key: str):
        _data = object.__getattribute__(self, "_data")
        if key in _data:
            return _data[key]
        return object.__getattribute__(self, key)

    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     if __name in self._data:
    #         self._data[__name] = __value

    @classmethod
    def _get_name(cls):
        __tablename__ = None
        for name, _ in inspect.getmembers(cls):
            if name == "__tablename__":
                __tablename__ = cls.__tablename__
        return (
            f'"{cls.__name__.lower()}"'
            if __tablename__ is None
            else f'"{__tablename__}"'
        )

    @classmethod
    def _get_pk_attributes(cls):
        pk = None
        pk_type = "BIGSERIAL"
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                pk = name
                pk_type = field.sql_type
        return pk, pk_type

    @classmethod
    def _drop_sql(cls):
        sql = Statements.DROP_TABLE.format(table_name=cls._get_name())
        return sql

    @classmethod
    def _create_sql(cls, ignore_exists=True):
        user_fields = list()
        predefined_fields = list()
        # is the primary key defined in this table?
        pks = list()
        for name, field in inspect.getmembers(cls):
            if isinstance(field, PrimaryKeyColumn):
                pks.append(f'"{name}"')
                _values = re.sub(
                    r"\s+",
                    " ",
                    "{_type} {unique} {nullable} {default} ".format(
                        _type=field.sql_type,
                        default=field.default_constraint,
                        nullable=field.nullable_constraint,
                        unique=field.unique_constraint,
                    ).strip(),
                )
                user_fields.append((f'"{name}"', _values))
            elif isinstance(field, Column):
                _values = re.sub(
                    r"\s+",
                    " ",
                    "{_type} {unique} {nullable} {default} ".format(
                        _type=field.sql_type,
                        unique=field.unique_constraint,
                        nullable=field.nullable_constraint,
                        default=field.default_constraint,
                    ).strip(),
                )
                user_fields.append((f'"{name}"', _values))
            elif isinstance(field, CreatedAtColumn):
                predefined_fields.append((f'"{name}"', field.created_at))
            elif isinstance(field, UpdatedAtColumn):
                predefined_fields.append((f'"{name}"', field.updated_at))
            elif isinstance(field, ForeignKeyColumn):
                # qns:
                # 1. what is the pk in the parent table?
                # 2. what is the type of the parent table pk?
                # 3. what is the name of the parent table?
                pk, pk_type = field.table._get_pk_attributes()
                parent_table_name = field.table._get_name()
                predefined_fields.append(
                    (
                        f'"{name}"',
                        '{pk_type} {nullable} REFERENCES {parent_table_name}("{pk}") ON DELETE {onDelete} ON UPDATE {onUpdate}'.format(
                            onDelete=field.onDelete,
                            onUpdate=field.onUpdate,
                            pk_type=pk_type,
                            parent_table_name=parent_table_name,
                            pk=pk,
                            nullable="NOT NULL" if field.required else "NULL",
                        ),
                    )
                )

        # do we have a single primary key or not?
        if len(pks) == 0:
            raise PkNotDefinedException(
                "Your table does not have a primary key column."
            )
        if len(pks) > 1:
            raise TooManyPkException(
                f"You have defined many field as primary keys which is not allowed. Fields ({', '.join(pks)}) are primary keys."
            )
        fields = [*user_fields, *predefined_fields]
        fields_name = ", ".join(f for f in [" ".join(field) for field in fields])
        sql = (
            Statements.CREATE_NEW_TABLE.format(
                table_name=cls._get_name(), fields_name=fields_name
            )
            if not ignore_exists
            else Statements.CREATE_NEW_TABLE_IF_NOT_EXITS.format(
                table_name=cls._get_name(), fields_name=fields_name
            )
        )
        return sql

    def _get_insert_bulk_attrs(self):
        fields = []
        placeholders = []
        values = []
        for _name, field in inspect.getmembers(self.__class__):
            if isinstance(field, Column):
                fields.append(_name)
                value = getattr(self, _name)
                values.append(value)
                placeholders.append("%s")
            elif isinstance(field, ForeignKeyColumn):
                fields.append(_name)
                value = getattr(self, _name)
                values.append(value)
                placeholders.append("%s")

        column_names = ", ".join([f'"{f}"' for f in fields])
        placeholder_values = ", ".join(placeholders)
        return column_names, placeholder_values, values

    def _get_insert_one_stm(self):
        fields = []
        placeholders = []
        values = []
        pk = None
        for _name, field in inspect.getmembers(self.__class__):
            if isinstance(field, Column):
                fields.append(_name)
                value = getattr(self, _name)
                values.append(value)
                placeholders.append("%s")
            elif isinstance(field, ForeignKeyColumn):
                fields.append(_name)
                value = getattr(self, _name)
                values.append(value)
                placeholders.append("%s")
            elif isinstance(field, PrimaryKeyColumn):
                pk = f'"{_name}"'
        sql = Statements.INSERT_COMMAND_ONE.format(
            table_name=self.__class__._get_name(),
            column_name=", ".join([f'"{f}"' for f in fields]),
            placeholder_values=", ".join(placeholders),
            pk=pk,
        )
        return sql, values

    @classmethod
    def _get_select_by_pk_stm(cls, pk, pk_name: str = "id", fields: list = []):
        for name, field in inspect.getmembers(cls):
            if (
                isinstance(field, Column)
                or isinstance(field, ForeignKeyColumn)
                or isinstance(field, UpdatedAtColumn)
                or isinstance(field, CreatedAtColumn)
                or isinstance(field, PrimaryKeyColumn)
            ) and name not in fields:
                fields.append(name)
        sql = Statements.SELECT_BY_PK.format(
            column_names=", ".join([f'"{f}"' for f in fields]),
            table_name=cls._get_name(),
            pk=pk,
            pk_name=pk_name,
        )
        return sql, fields

    @classmethod
    def _get_delete_by_pk_stm(cls, pk, pk_name: str = "id"):
        sql = Statements.DELETE_BY_PK.format(
            table_name=cls._get_name(),
            pk="%s",  # mask it to avoid SQL Injection
            pk_name=pk_name,
        )
        return sql, pk

    @classmethod
    def _get_insert_bulk_smt(cls, placeholders, columns, data):
        column_names = columns
        placeholders = placeholders
        sql = Statements.INSERT_COMMAND_MANY.format(
            column_names=column_names,
            table_name=cls._get_name(),
            placeholder_values=placeholders,
        )
        return sql, data

    @classmethod
    def _get_select_one_stm(cls, pk, pk_name: str = "id", fields: list = []):
        for name, field in inspect.getmembers(cls):
            if (
                isinstance(field, Column)
                or isinstance(field, ForeignKeyColumn)
                or isinstance(field, UpdatedAtColumn)
                or isinstance(field, CreatedAtColumn)
                or isinstance(field, PrimaryKeyColumn)
            ) and name not in fields:
                fields.append(name)
        sql = Statements.SELECT_BY_PK.format(
            column_names=", ".join([f'"{f}"' for f in fields]),
            table_name=cls._get_name(),
            pk=pk,
            pk_name=pk_name,
        )
        return sql, fields

    @classmethod
    def _get_select_where_stm(cls, fields: list = [], args: dict = {}):
        params = []
        filters = []
        for name, field in inspect.getmembers(cls):
            if (
                isinstance(field, Column)
                or isinstance(field, ForeignKeyColumn)
                or isinstance(field, UpdatedAtColumn)
                or isinstance(field, CreatedAtColumn)
                or isinstance(field, PrimaryKeyColumn)
            ) and name not in fields:
                fields.append(name)

        for key, value in args.items():
            filters.append(f"{key} = %s")
            params.append(value)
        if len(filters) == 0:
            sql = Statements.SELECT_COMMAND.format(
                column_names=", ".join([f'"{f}"' for f in fields]),
                table_name=cls._get_name(),
            )
        else:
            sql = Statements.SELECT_WHERE_COMMAND.format(
                column_names=", ".join([f'"{f}"' for f in fields]),
                table_name=cls._get_name(),
                filters=" AND ".join(filters),
            )
        return sql, fields, params

    @classmethod
    def _get_delete_where_stm(cls, pk: str = "id", args: dict = {}):
        params = []
        filters = []
        for key, value in args.items():
            filters.append(f"{key} = %s")
            params.append(value)
        if len(filters) == 0:
            sql = Statements.DELETE_ALL_COMMAND.format(
                table_name=cls._get_name(),
            )
        else:
            sql = Statements.DELETE_ONE_WHERE_COMMAND.format(
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
            sql = Statements.DELETE_ALL_COMMAND.format(
                table_name=cls._get_name(),
            )
        else:
            sql = Statements.DELETE_BULK_WHERE_COMMAND.format(
                table_name=cls._get_name(),
                filters=" AND ".join(filters),
            )
        return sql, params

    @classmethod
    def _get_update_by_pk_stm(cls, pk_name: str = "id", args: dict = {}):
        updatedAtColumName = None
        for name, field in inspect.getmembers(cls):
            if isinstance(field, UpdatedAtColumn):
                updatedAtColumName = name

        values = list()
        placeholders = list()
        for key, value in args.items():
            placeholders.append(f'"{key}" = %s')
            values.append(value)

        if updatedAtColumName is not None:
            placeholders.append(f'"{updatedAtColumName}" = %s')
            values.append(current_time_stamp)

        sql = Statements.UPDATE_BY_PK_COMMAND.format(
            table_name=cls._get_name(),
            pk="%s",
            pk_name=pk_name,
            placeholder_values=", ".join(placeholders),
        )
        return sql, values

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

        sql = Statements.UPDATE_BY_ONE_COMMAND.format(
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


        sql = Statements.UPDATE_BULK_WHERE_COMMAND.format(
            table_name=cls._get_name(),
            placeholder_values=", ".join(placeholder_values),
            placeholder_filters=", ".join([i[0] for i in placeholder_filters]),
        )
        return sql, values, [i[1] for i in placeholder_filters]
