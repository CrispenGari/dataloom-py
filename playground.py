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
    createdAt = CreatedAtColumn()
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
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()
    userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "userId": self.userId,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


db = Database("hi", password="root", user="postgres")
conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)
user = User(name="Crispen", username="heyy")
userId = db.create(user)
posts = db.create_bulk([Post(userId=userId, title=f"Post {i}") for i in range(2)])
if __name__ == "__main__":
    conn.close()
