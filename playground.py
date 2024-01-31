from orm.db import Database
from orm.model.column import (
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    ForeignKeyColumn,
    PrimaryKeyColumn,
)
from orm.model.model import Model


class User(Model):
    __tablename__ = "users"
    id = PrimaryKeyColumn(type="bigint", auto_increment=True)
    username = Column(type="text", nullable=False)
    name = Column(type="varchar", unique=False, length=255)
    createAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()

    def __str__(self) -> str:
        return f"User<{self.id}>"

    def __repr__(self) -> str:
        return f"User<{self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "createdAt": self.createAt,
            "updatedAt": self.updatedAt,
        }


class Post(Model):
    __tablename__ = "posts"
    id = PrimaryKeyColumn(type="bigint", auto_increment=True)
    title = Column(type="text", nullable=False, default="Hello there!!")
    createAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()
    userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "userId": self.userId,
            "createdAt": self.createAt,
            "updatedAt": self.updatedAt,
        }


db = Database("hi", password="root", user="postgres")
conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)
user = [
    User(name="Crispen", username="heyy"),
    User(name="Crispen", username="heyy"),
    User(name="Crispen", username="heyy"),
]
userId = db.commit_bulk(user)
# postId = db.commit(
#     Post(userId=1, title="What are you thinking"),
# )

now = db.delete_one(User, {"name": "Crispen"})
print(now)


# print(f"now: {now}")
# now = db.delete_one(Post, {"id": 8})
# print(now.userId)
# print(postId)


# post = Post(userId=userId, title="What are you thinking")
# db.commit(post)


# posts = db.find_all(Post)
# print([u.to_dict() for u in posts])
me = db.find_by_pk(User, 1)
print(me.to_dict())

# him = db.find_one(User, filters={"id": 1})
# print(him.to_dict())

# many = db.find_many(User, {"id": 5})
# print([u.to_dict() for u in many])


if __name__ == "__main__":
    conn.close()
