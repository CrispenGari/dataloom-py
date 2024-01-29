from orm.db import Database
from orm.model.column import Column
from orm.model.model import Model

database = Database("hi", password="root", user="postgres")
conn = database.connect()


class Users(Model):
    _id = Column(type="bigint", primary_key=True, nullable=False, auto_increment=True)
    username = Column(type="text", nullable=False, default="Hello there!!")
    name = Column(type="int", unique=True)


Users(name="Crispen", age=20, id=5)

# database.sync([Users])
# print(database.tables)
