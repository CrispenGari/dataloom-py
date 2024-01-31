from orm.types import POSTGRES_SQL_TYPES


class CreatedAtColumn:
    def __init__(self):
        pass

    @property
    def created_at(self):
        return "{type} DEFAULT {value}".format(
            type=POSTGRES_SQL_TYPES["timestamp"], value="CURRENT_TIMESTAMP"
        )


class UpdatedAtColumn:
    def __init__(self):
        pass

    @property
    def updated_at(self):
        return "{type} DEFAULT {value}".format(
            type=POSTGRES_SQL_TYPES["timestamp"], value="CURRENT_TIMESTAMP"
        )


class ForeignKeyColumn:
    def __init__(
        self,
        table,
        type: str | None = None,
        required: bool = True,
        onDelete: str = "NO ACTION",
        onUpdate: str = "NO ACTION",
    ):
        self.table = table
        self.required = required
        self.onDelete = onDelete
        self.onUpdate = onUpdate
        self.type = type

    @property
    def sql_type(self):
        if self.type in POSTGRES_SQL_TYPES:
            return POSTGRES_SQL_TYPES[self.type]
        else:
            raise ValueError(f"Unsupported column type: {self.type}")


class PrimaryKeyColumn:
    def __init__(
        self,
        type: str = "bigserial",
        length: int | None = None,
        auto_increment: bool = False,
        nullable: bool = False,
        unique: bool = True,
        default=None,
    ):
        self.type = type
        self.length = length
        self.auto_increment = auto_increment
        self.default = default
        self.nullable = nullable
        self.unique = unique

    @property
    def default_constraint(self):
        return (
            "DEFAULT '{default}'".format(default=self.default) if self.default else ""
        )

    @property
    def unique_constraint(self):
        return "UNIQUE" if self.unique else ""

    @property
    def nullable_constraint(self):
        return "NOT NULL" if not self.nullable else ""

    @property
    def sql_type(self):
        if self.type in POSTGRES_SQL_TYPES:
            if self.auto_increment:
                return "BIGSERIAL"
            return (
                f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                if self.length
                else POSTGRES_SQL_TYPES[self.type]
            )
        else:
            raise ValueError(f"Unsupported column type: {self.type}")


class Column:
    def __init__(
        self,
        type,
        nullable: bool = True,
        unique: bool = False,
        length: int | None = None,
        auto_increment: bool = False,
        default=None,
    ):
        self.type = type
        self.nullable = nullable
        self.unique = unique
        self.length = length
        self.auto_increment = auto_increment
        self.default = default

        self._data = {}

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
            return (
                f"{POSTGRES_SQL_TYPES[self.type]}({self.length})"
                if self.length
                else POSTGRES_SQL_TYPES[self.type]
            )
        else:
            raise ValueError(f"Unsupported column type: {self.type}")
