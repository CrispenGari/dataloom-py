from dataloom import (
    Loom,
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

sqlite_loom = Loom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)

pg_loom = Loom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    sql_logger="console",
)

mysql_loom = Loom(
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

aff = mysql_loom.delete_bulk(
    instance=User,
    filters=Filter(column="id", value=1),
)
print(aff)


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

posts = mysql_loom.find_many(
    Post,
    select="id",
    filters=Filter(column="id", operator="gt", value=1),
    group=Group(
        column="id",
        function="MAX",
        having=Having(column="id", operator="in", value=(2, 3, 4)),
        return_aggregation_column=False,
    ),
)

print(posts)
