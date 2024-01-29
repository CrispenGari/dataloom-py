### dataloom

An `orm` for python.

### Usage

```py
from dataloom import Database, Model, Column

database = Database("hi", password="root", user="postgres")
database.connect()

class Users(Model):
    _id = Column(type="bigint", primary_key=True, nullable=False, auto_increment=True)
    username = Column(type="text", nullable=False, default="Hello there!!")
    name = Column(type="int", unique=True)

database.sync([Users])
```
