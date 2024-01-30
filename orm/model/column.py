from typing import Any
from orm.types import POSTGRES_SQL_TYPES


class ForeignKey:
    pass


class Column:
    def __init__(
        self,
        type,
        primary_key: bool = False,
        nullable: bool = True,
        unique: bool = False,
        length: int | None = None,
        auto_increment: bool = False,
        default=None,
    ):
        self.type = type
        self.primary_key = primary_key
        self.nullable = nullable
        self.unique = unique
        self.length = length
        self.auto_increment = (auto_increment,)
        self.default = default

        self._data = {}

    @property
    def primary_key_constraint(self):
        return "PRIMARY KEY" if self.primary_key else ""

    @property
    def nullable_constraint(self):
        return "NOT NULL" if not self.nullable else ""

    @property
    def unique_constraint(self):
        return "UNIQUE" if self.unique else ""

    @property
    def default_constraint(self):
        return (
            "DEFAULT '{default}'".format(default=self.default) if self.default else ""
        )

    @property
    def sql_type(self):
        if self.type in POSTGRES_SQL_TYPES:
            if self.auto_increment and self.primary_key:
                return "BIGSERIAL"
            return (
                f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                if self.length
                else POSTGRES_SQL_TYPES[self.type]
            )
        else:
            raise ValueError(f"Unsupported column type: {self.type}")
