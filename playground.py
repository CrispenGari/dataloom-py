from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    Order,
    Include,
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
cate = Category(name="general")
userId = pg_loom.insert_one(user)
categoryId = pg_loom.insert_one(cate)
post = Post(title="What are you doing?", userId=userId, categoryId=categoryId)
post_id = pg_loom.insert_bulk([post for i in range(5)])
posts = pg_loom.find_by_pk(
    Post,
    1,
    select=["id", "completed", "title", "createdAt"],
    # limit=3,
    # offset=1,
    # order=[
    #     Order(column="createdAt", order="ASC"),
    #     Order(column="id", order="DESC"),
    # ],
    include=[
        Include(
            model=User,
            select=["id", "username", "name"],
            limit=1,
            offset=0,
        ),
    ],
    return_dict=True,
)

print(posts)


print(posts)

# if __name__ == "__main__":
#     conn.close()


# class Order:
