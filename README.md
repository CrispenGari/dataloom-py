### dataloom

An `orm` for python.

### Usage

In this section we are going to go through how you can use our `orm` package in your project.

### Connection

A database connection is required. In this example a connection will be set on a `postgres` database instance that have a database name `hi.

```py
from dataloom import Database, Model, Column

db = Database("hi", password="root", user="postgres")
conn = db.connect()

if __name__ == "__main__":
    conn.close()
```

The database class takes in the following options:

<table border="1">
  <thead>
    <tr>
      <th>Option</th>
      <th>Value Type</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>database</td><td>str</td>
      <td>This is the name of the database. It is required upon connection creation.</td>
      <td></td>
    </tr>
     <tr><td>dialect</td><td>str|None</td>
      <td>The user to connect to the database instance.</td><td>postgres</td>
    </tr>
    <tr><td>password</td><td>str|None</td>
      <td>The password to connect to the database instance of the specified user.</td><td>postgres</td>
    </tr>
    <tr><td>host</td><td>str|None</td>
      <td>The database host. </td><td>localhost|127.0.0.1</td>
    </tr>
    <tr><td>port</td><td>int|None</td>
      <td>The database port number. </td><td>4532</td>
    </tr>
     <tr><td>logs</td><td>bool</td>
      <td>Specify wether you want to see sql statements as you perform operations on the database in the logs or not.</td><td>True</td>
    </tr>
  </tbody>
</table>

### Model

A model is just a top level class that allows you to build some complicated SQL tables from regular python classes. You can define a table `User` as an class that inherits from `Model` class as follows:

```py
class User(Model):
    __tablename__ = "users"
    id = Column(type="bigint", primary_key=True, nullable=False, auto_increment=True)
    username = Column(type="text", nullable=False, default="Hello there!!")
    name = Column(type="varchar", unique=True, length=255)

    def __str__(self) -> str:
        return f"User<{self.id}>"

    def __repr__(self) -> str:
        return f"User<{self.id}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "username": self.username}

```

You will need to `sync` your database tables. To Syn

```py
db.sync([User], drop=True, force=True)
```

1. Creating a Record

```py
user = User(name="Crispen", username="heyy")
userId = db.commit(user)
print(userId)
```

2. Getting records

To get the records in the database you use `find_all()` and `find_many()`

```py
users = db.find_all(User)
print([u.to_dict() for u in users])
```

Here is an example of the `find_many()` function with some filters.

```py
many = db.find_many(User, {"id": 5})
print([u.to_dict() for u in many])
```

3. Getting a single record

The find `find_by_pk` and the `find_one` methods are used to find a single record in the database.

```py
user = User(name="Crispen", username="heyy")
me = db.find_by_pk(User, 1)
print(me.to_dict())

```

Using the `find_one` you can specify the filters of your query as follows:

```py
him = db.find_one(User, filters={"id": 1})
print(him.to_dict())
```
