from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    ColumnValue,
    Include,
    Filter,
    Order,
)
from typing import Optional


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
sqlite_loom = Dataloom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)


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
        required=False,
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
    updatedAt = UpdatedAtColumn()
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


conn, tables = mysql_loom.connect_and_sync(
    [Post, User, Category, Profile], drop=True, force=True
)
userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)
categories = ["general", "education", "sport", "culture"]
cats = []
for cat in categories:
    pId = mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="title", value=f"What are you doing {cat}?"),
            ColumnValue(name="userId", value=userId),
        ],
    )
#     cats.append(
#         [ColumnValue(name="type", value=cat), ColumnValue(name="postId", value=pId)]
#     )

# rows = sqlite_loom.insert_bulk(Category, values=cats)
# print(rows)


# res = mysql_loom.delete_bulk(
#     instance=User,
#     offset=3,
#     order=[Order(column="id", order="DESC")],
#     filters=[Filter(column="id", value=1)],
# )

res2 = res3 = mysql_loom.delete_one(
    instance=Post,
    offset=0,
    order=[Order(column="id", order="DESC")],
    filters=[Filter(column="id", value=1, operator="gt")],
)

print(6, res2)

# post = mysql_loom.find_by_pk(
#     Post,
#     pk=1,
#     include=[Include(model=User, select=["id", "username"], maps_to="N-1")],
#     select=["title", "completed"],
# )
# print("---- post", post)


# if __name__ == "__main__":
#     conn.close()
