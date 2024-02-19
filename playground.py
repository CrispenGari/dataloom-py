from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    Filter,
    ColumnValue,
    Include,
    Order,
    Group,
    Having,
)
from dataloom.decorators import initialize
import json, time
from typing import Optional
from dataclasses import dataclass

sqlite_loom = Dataloom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)

pg_loom = Dataloom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    sql_logger="console",
)

mysql_loom = Dataloom(
    dialect="mysql",
    database="hi",
    password="root",
    user="root",
    host="localhost",
    logs_filename="logs.sql",
    port=3306,
    sql_logger="console",
)


class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)


@initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
class Profile(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    avatar = Column(type="text", nullable=False)
    userId = ForeignKeyColumn(
        User,
        maps_to="1-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )

    def __init__(self, id: int | None, avatar: str | None, userId: int | None) -> None:
        self.id = id
        self.avatar = avatar
        self.userId = userId

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:id={self.id}>"

    @property
    def to_dict(self):
        return {"id": self.id, "avatar": self.avatar, "userId": self.userId}


class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User,
        maps_to="1-N",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


class Category(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="categories")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    type = Column(type="varchar", length=255, nullable=False)

    postId = ForeignKeyColumn(
        Post,
        maps_to="N-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


conn, tables = mysql_loom.connect_and_sync(
    [User, Profile, Post, Category], drop=True, force=True
)


userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)

userId2 = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="bob"),
)

profileId = mysql_loom.insert_one(
    instance=Profile,
    values=[
        ColumnValue(name="userId", value=userId),
        ColumnValue(name="avatar", value="hello.jpg"),
    ],
)
for title in ["Hello", "Hello", "What are you doing", "Coding"]:
    mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )


for cat in ["general", "education", "tech", "sport"]:
    mysql_loom.insert_one(
        instance=Category,
        values=[
            ColumnValue(name="postId", value=1),
            ColumnValue(name="type", value=cat),
        ],
    )


profile = mysql_loom.find_all(
    Post,
    select=["title", "id"],
    # filters=Filter(column="id", operator="gt", value=1),
    group=[
        Group(
            column="id",
            function="MAX",
            having=[
                Having(column="id", operator="in", value=(2, 3, 4)),
                Having(column="id", operator="lt", value=10, join_next_with="OR"),
            ],
            return_aggregation_column=True,
        ),
        Group(
            column="title",
            function="COUNT",
            having=Having(column="title", operator="eq", value=1),
            return_aggregation_column=True,
        ),
    ],
)
print(profile)
