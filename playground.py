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

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
        }


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

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "completed": self.completed,
            "title": self.title,
            "userId": self.userId,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


conn, tables = pg_loom.connect_and_sync([Post, User], drop=True, force=True)
print(tables)


user = User(username="@miller")
userId = pg_loom.insert_one(user)
post = Post(title="What are you doing?", userId=userId)
post_id = pg_loom.insert_bulk([post for i in range(5)])

posts = pg_loom.find_all(Post)

print(user.to_dict)

print([p.to_dict for p in posts])


if __name__ == "__main__":
    conn.close()

# instance = [*db, dataloom.logging]

# Post = Model[TypePost](TypePost, instance=instance)
# Post.create(TypePost(title="Hi"))


# dataloom.connect("mysql", database="hi", password="root", user="root")
# dataloom.connect("sqlite", database="hi.db")


# from dataloom.db import Database
# from dataloom.model.column import (
#     Column,
#     CreatedAtColumn,
#     UpdatedAtColumn,
#     ForeignKeyColumn,
#     PrimaryKeyColumn,
# )
# from dataloom.model.model import Model


# class User(Model):
#     __tablename__ = "users"
#     id = PrimaryKeyColumn(type="bigint", auto_increment=True)
#     username = Column(type="text", nullable=False)
#     name = Column(type="varchar", unique=False, length=255)
#     createdAt = CreatedAtColumn()
#     updatedAt = UpdatedAtColumn()

#     def __str__(self) -> str:
#         return f"User<{self.id}>"

#     def __repr__(self) -> str:
#         return f"User<{self.id}>"

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "username": self.username,
#             "createdAt": self.createAt,
#             "updatedAt": self.updatedAt,
#         }


# class Post(Model):
#     __tablename__ = "posts"
#     id = PrimaryKeyColumn(type="bigint", auto_increment=True)
#     title = Column(type="text", nullable=False, default="Hello there!!")
#     createdAt = CreatedAtColumn()
#     updatedAt = UpdatedAtColumn()
#     userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "userId": self.userId,
#             "createdAt": self.createdAt,
#             "updatedAt": self.updatedAt,
#         }


# db = Database("hi", password="root", user="postgres")
# conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)
# user = User(name="Crispen", username="heyy")
# userId = db.create(user)
# posts = db.create_bulk([Post(userId=userId, title=f"Post {i}") for i in range(2)])

# post = db.find_by_pk(Post, 1, options={"include": [User]})

# print(post.to_dict())
# if __name__ == "__main__":
#     conn.close()
