from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
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


conn, tables = mysql_loom.connect_and_sync([Post, User], drop=True, force=True)
print(tables)


user = User(username="@miller")
userId = mysql_loom.insert_one(user)
post = Post(title="What are you doing?", userId=userId)
post_id = mysql_loom.insert_bulk([post for i in range(5)])
posts = mysql_loom.find_many(
    Post, filters={"userId": 1}, select=["id", "completed"], limit=3, offset=3
)

print(posts)


print(posts)

if __name__ == "__main__":
    conn.close()
