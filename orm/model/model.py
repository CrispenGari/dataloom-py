from orm.model.column import Column
from orm.model.statements import Statements
import inspect
import re


class Model:
    def __init__(self, **args) -> None:
        self._data = {id: None}
        for k, v in args.items():
            self._data[k] = v

    @classmethod
    def _get_name(cls):
        return cls.__name__.lower()

    @classmethod
    def _drop_sql(cls):
        sql = Statements.DROP_TABLE.format(table_name=cls._get_name)
        return sql

    @classmethod
    def _create_sql(cls, ignore_exists=True):
        fields = [("id", "BIGSERIAL NOT NULL")]
        fields_name = [" ".join(field) for field in fields]
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                _values = re.sub(
                    r"\s+",
                    " ",
                    "{_type} {primary_key} {unique} {nullable} {default} ".format(
                        _type=field.sql_type,
                        primary_key=field.primary_key_constraint,
                        unique=field.unique_constraint,
                        nullable=field.nullable_constraint,
                        default=field.default_constraint,
                    ).strip(),
                )

                fields.append((name, _values))
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
