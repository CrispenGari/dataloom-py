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
)
from typing import Optional

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

# mysql_loom = Dataloom(
#     dialect="mysql",
#     database="hi",
#     password="root",
#     user="root",
#     host="localhost",
#     logs_filename="logs.sql",
#     port=3306,
#     sql_logger="console",
# )


class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)


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


conn, tables = pg_loom.connect_and_sync([User, Profile, Post], drop=True, force=True)


userId = pg_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)

profileId = pg_loom.insert_one(
    instance=Profile,
    values=[
        ColumnValue(name="userId", value=userId),
        ColumnValue(name="avatar", value="hello.jpg"),
    ],
)
for title in ["Hey", "Hello", "What are you doing", "Coding"]:
    pg_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )

# profile = pg_loom.find_by_pk(
#     instance=Profile,
#     pk=profileId,
#     include=[
#         Include(model=User, select=["id", "username", "tokenVersion"], has='one')
#     ],
# )

# user = pg_loom.find_by_pk(
#     instance=User,
#     pk=userId,
#     include=[Include(model=Profile, select=["id", "avatar"], has='one')],
# )

user = pg_loom.find_by_pk(
    instance=User,
    pk=userId,
    include=[
        Include(
            model=Post,
            select=["id", "title"],
            has="many",
            offset=0,
            limit=2,
            order=[
                Order(column="createdAt", order="DESC"),
                Order(column="id", order="DESC"),
            ],
        ),
        Include(model=Profile, select=["id", "avatar"], has="one"),
    ],
)
print(user)

post = pg_loom.find_by_pk(
    instance=Post,
    pk=1,
    include=[Include(model=User, select=["id", "username"], has="one")],
)

print(post)
