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
)
from typing import Optional


pg_loom = Dataloom(
    dialect="postgres", database="hi", password="root", user="postgres", logging=True
)
mysql_loom = Dataloom(
    dialect="mysql",
    database="hi",
    password="root",
    user="root",
    host="localhost",
    logging=True,
    logs_filename="logs.sql",
    port=3306,
)
sqlite_loom = Dataloom(
    dialect="sqlite", database="hi.db", logs_filename="sqlite-logs.sql", logging=True
)


class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)


class Category(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="categories")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    name = Column(type="varchar", length=255, nullable=False)


class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
    )
    categoryId = ForeignKeyColumn(
        Category, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
    )


conn, tables = pg_loom.connect_and_sync([Post, User, Category], drop=True, force=True)
print(tables)
user = User(username="@miller")
userId = pg_loom.insert_one(user)

pg_loom.increment(
    User,
    filters=Filter(column="id", value=1),
    column=ColumnValue(name="tokenVersion", value=2),
)


# cate = Category(name="general")
# categoryId = pg_loom.insert_one(cate)
# post = Post(title="What are you doing?", userId=userId, categoryId=categoryId)
# post_id = pg_loom.insert_bulk([post for i in range(5)])

# post = pg_loom.find_one(
#     Post,
#     filters=[
#         Filter(column="id", operator="eq", value=4, join_next_filter_with="AND"),
#         Filter(column="userId", operator="eq", value=1),
#     ],
#     offset=2,
#     select=["id", "completed", "title", "createdAt"],
#     include=[
#         Include(
#             model=User,
#             select=["id", "username", "name"],
#             limit=1,
#             offset=0,
#         ),
#     ],
#     return_dict=True,
# )
# print(post)

# post = pg_loom.find_by_pk(
#     Post,
#     pk=1,
#     select=["id", "completed", "title", "createdAt"],
#     include=[
#         Include(
#             model=User,
#             select=["id", "username", "name"],
#             limit=1,
#             offset=0,
#         ),
#     ],
#     return_dict=True,
# )

# re = pg_loom.update_one(
#     Post,
#     values=[
#         ColumnValue(name="title", value="Hey"),
#         ColumnValue(name="completed", value=True),
#     ],
#     filters=[
#         Filter(column="id", value=1, join_next_filter_with="AND"),
#         Filter(column="userId", value=1, join_next_filter_with="AND"),
#     ],
# )
# print(post)
# print(post)


# posts = pg_loom.find_one(
#     Post,
#     filters=[
#         Filter(column="id", operator="eq", value=1, join_next_filter_with="AND"),
#         Filter(column="userId", operator="eq", value=1),
#     ],
#     select=["id", "completed", "title", "createdAt"],
#     include=[
#         Include(
#             model=User,
#             select=["id", "username", "name"],
#             limit=1,
#             offset=0,
#         ),
#     ],
#     return_dict=True,
# )
# print(posts)

# posts = pg_loom.find_all(
#     Post,
#     select=["id", "completed", "title", "createdAt"],
#     limit=3,
#     offset=0,
#     order=[
#         Order(column="createdAt", order="ASC"),
#         Order(column="id", order="DESC"),
#     ],
#     include=[
#         Include(
#             model=User,
#             select=["id", "username", "name"],
#             limit=1,
#             offset=0,
#         ),
#     ],
#     return_dict=True,
# )
# print(posts)
# posts = pg_loom.find_many(
#     Post,
#     filters=[
#         Filter(column="id", operator="eq", value=1, join_next_filter_with="AND"),
#         Filter(column="userId", operator="eq", value=1),
#     ],
#     select=["id", "completed", "title", "createdAt"],
#     limit=10,
#     offset=0,
#     order=[
#         Order(column="createdAt", order="ASC"),
#         Order(column="id", order="DESC"),
#     ],
#     include=[
#         Include(
#             model=User,
#             select=["id", "username", "name"],
#             limit=1,
#             offset=0,
#         ),
#     ],
#     return_dict=True,
# )
# print(posts)


if __name__ == "__main__":
    conn.close()
