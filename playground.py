from orm.db import Database
from orm.model.column import Column
from orm.model.model import Model

db = Database("hi", password="root", user="postgres")
conn = db.connect()


class User(Model):
    __tablename__ = "users"
    id = Column(type="bigint", primary_key=True, nullable=False, auto_increment=True)
    username = Column(type="text", nullable=False, default="Hello there!!")
    name = Column(
        type="varchar",
        unique=True,
        length=255,
    )

    def __str__(self) -> str:
        return f"User<{self.id}>"

    def __repr__(self) -> str:
        return f"User<{self.id}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "username": self.username}


db.sync([User], drop=True, force=True)

user = User(name="Crispen", username="heyy")
db.commit(user)
users = db.find_all(User)
print([u.to_dict() for u in users])
me = db.find_by_pk(User, 1)
print(me.to_dict())

him = db.find_one(User, filters={"id": 1})
print(him.to_dict())

many = db.find_many(User, {"id": 5})
print([u.to_dict() for u in many])


if __name__ == "__main__":
    conn.close()
