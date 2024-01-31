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

### `Model` Class

A model is just a top level class that allows you to build some complicated SQL tables from regular python classes. You can define a table `User` as an class that inherits from `Model` class as follows:

```py
class User(Model):
    __tablename__ = "users"
    id = PrimaryKeyColumn(type="bigint", auto_increment=True)
    username = Column(type="text", nullable=False, default="Hello there!!")
    name = Column(type="varchar", unique=True, length=255)

    def __str__(self) -> str:
        return f"User<{self.id}>"

    def __repr__(self) -> str:
        return f"User<{self.id}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "username": self.username}

```

- We are defining a model called `User` and we are specifying the table name using the property `__tablename__` to `"users"`. This will tell `dataloom` that don't infer the table name from the class use the one that I have provided. If you don't pass the `__tablename__` then the class name will be used as your table name upon syncing tables.

### `Column` Class

Every table has a column. Each property that is set to column in a model is considered 1. Let's have a look at how we can define a column in a table.

```py
username = Column(type="text", nullable=False, default="Hello there!!")
```

We are defining a column that is called `id`. And we are specifying the type of this column and some other options. Here are some other options that can be passed to the

<table border="1">
  <thead>
    <tr><th>Argument</th><th>Description</th>
      <th>Type</th><th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>type</td><td>Required datatype of a column</td>
      <td>any datatype supported</td><td></td>
    </tr>
    <tr>
      <td>nullable</td><td>Optional to specify if the column will allow null values or not.</td>
      <td>bool</td><td>False</td>
    </tr>
    <tr>
      <td>length</td><td>Optional to specify if the length of the type that. eg if this argument is passed as <b>N</b> with a <b>T</b> type, this will yield an sql statement with type <b>T(N)</b>.</td>
      <td>int|None</td><td>None</td>
    </tr>
      <tr>
      <td>auto_increment</td><td>Optional to specify if the column will automatically increment or not.</td>
      <td>bool</td><td>False</td>
    </tr>
       <tr>
      <td>default</td><td>Optional to specify if the default value in a column.</td>
      <td>any</td><td>None</td>
    </tr>
     <tr>
      <td>unique</td><td>Optional to specify if the column will contain unique values or not.</td>
      <td>bool</td><td>False</td>
    </tr>
  </tbody>
</table>

> Note: Every table is required to have a primary key column and this column should be 1. Let's talk about the `PrimaryKeyColumn`

### `PrimaryKeyColumn` Class

This create a unique index in every table that you create. Every table that you create and that inherits from the `Model` class is required to have exactly 1 `PrimaryKeyColumn`. Here is how you can create a `id` column as a primary key in your table:

```py
class Post(Model):
    __tablename__ = "posts"
    id = PrimaryKeyColumn(type="bigint", auto_increment=True)
    #...rest of your tables
```

The `PrimaryKeyColumn` takes the following arguments:

<table border="1">
  <thead>
    <tr><th>Argument</th><th>Description</th>
      <th>Type</th><th>Default</th>
    </tr>
  </thead>
  <tbody>
     <tr>
      <td>type</td><td>The datatype of your primary key.</td>
      <td>str</td><td>"bigserial"</td>
    </tr>
    <tr>
      <td>length</td><td>Optional to specify if the length of the type that. eg if this argument is passed as <b>N</b> with a <b>T</b> type, this will yield an sql statement with type <b>T(N)</b>.</td>
      <td>int|None</td><td>None</td>
    </tr>
      <tr>
      <td>auto_increment</td><td>Optional to specify if the column will automatically increment or not.</td>
      <td>bool</td><td>False</td>
    </tr>
       <tr>
      <td>default</td><td>Optional to specify if the default value in a column.</td>
      <td>any</td><td>None</td>
    </tr>
     <tr>
      <td>nullable</td><td>Optional to specify if the column will allow null values or not.</td>
      <td>bool</td><td>False</td>
    </tr>
     <tr>
      <td>unique</td><td>Optional to specify if the column will contain unique values or not.</td>
      <td>bool</td><td>True</td>
    </tr>
  </tbody>
</table>

### `ForeignKeyColumn` Class

This Column is used when we are telling `dataloom` that the column has a relationship with a primary key in another table. Let's consider the following model definition of a `Post`:

```py
class Post(Model):
    __tablename__ = "posts"

    id = PrimaryKeyColumn(type="bigint", auto_increment=True)
    title = Column(type="text", nullable=False, default="Hello there!!")
    createAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()
    userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")
```

- `userId` is a foreign key in the table `posts` which means it has a relationship with a primary key in the `users` table. This column takes in some arguments which are:

<table border="1">
  <thead>
    <tr><th>Argument</th><th>Description</th>
      <th>Type</th><th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>table</td><td>Required, this is the table that the current model reference as it's parent. In our toy example this is called `User`.</td>
      <td>Model</td><td></td>
    </tr>
     <tr>
      <td>type</td><td>You can specify the type of the foreign key, which is optional as dataloom can infer it from the parent table.</td>
      <td>str|None</td><td>None</td>
    </tr>
     <tr>
      <td>required</td><td>Specifying if the foreign key is required or not.</td>
      <td>bool</td><td>False</td>
    </tr>
    <tr>
      <td>onDelete</td><td>Specifying the action that will be performed when the parent table is deleted</td>
      <td>str ["NO ACTION", "SET NULL", "CASCADE"]</td><td>"NO ACTION"</td>
    </tr>
    <tr>
      <td>onDelete</td><td>Specifying the action that will be performed when the parent table is updated</td>
      <td>str ["NO ACTION", "SET NULL", "CASCADE"]</td><td>"NO ACTION"</td>
    </tr>
  </tbody>
</table>

It is very important to specify the actions on `onDelete` and `onUpdate` so that `dataloom` will take care of your models relationships actions as. The actions that are available are:

1. `"NO ACTION"` - Meaning if you `delete` or `update` the parent table nothing will happen to the child table.
2. `"SET NULL"` - Meaning if you `delete` or `update` the parent table, then in the child table the value will be set to `null`
3. `"CASCADE"` - Meaning if you `delete` or `update` the table also the same action will happen on the child table.

### `CreatedAtColumn` Class

When a column is marked as `CreatedAtColumn` it's value will automatically get generated every time when you `create` a new record in a database as a timestamp.

### `UpdatedAtColumn` Class

When a column is marked as `UpdatedAtColumn` it's value will automatically get generated every time when you `create` a new record or `update` an existing record in a database table as a timestamp.

### Syncing Tables

This is the process of creating tables from models and save them to a database.
After defining your tables you will need to `sync` your database tables. To Sync a database you call the method called `sync`. This method allows you to create and commit tables into the database. Let's say we have two models `User` and `Post` and you want to create commit them to the database you can do it as follows:

```py
tables = db.sync([User, Post], drop=True, force=True)
```

The method returns a list of table names that have been created or the table names that are in your database. The `sync` method accepts the following arguments:

<table border="1">
  <thead>
    <tr><th>Argument</th><th>Description</th><th>Type</th><th>Default</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>models</td><td>A list of your table class that are inheriting from the Model class.</td>
      <td>list</td><td>[]</td>
    </tr>
     <tr>
      <td>drop</td><td>Weather to drop tables during syncing or not.</td>
      <td>bool</td><td>False</td>
    </tr>
     <tr>
      <td>force</td><td>Force to drop tables during syncing or not.</td>
      <td>bool</td><td>False</td>
    </tr>
     <tr>
      <td>alter</td><td>Alter tables rather than dropping them during syncing or not.</td>
      <td>bool</td><td>False</td>
    </tr>
  </tbody>
</table>

> We have noticed that there are two steps that we are doing here to start working with our `orm`. First you need to create a connection and then `sync` the tables in another steps. The `connect_and_sync` is very handy as it does the database connection and also does the `sync` of tables. Here is an example on how you can use it:

```py
db = Database("hi", password="root", user="postgres")
conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)

if __name__ == "__main__":
    conn.close()
```

Returns a `conn` and `tablenames` that are in the database. The method accepts the same arguments as the `sync` method.

1. Creating a Record

The `commit` method let you create save a single row in a particular table. When you save this will return the `id` of the inserted document

```py
user = User(name="Crispen", username="heyy")
userId = db.commit(user)
print(userId)
```

Using the `commit_bulk` you will be able to save in bulk as the method explains itself. The following is an example showing how we can add `3` post to the database table at the same time.

```py
posts = [
    Post(userId=userId, title="What are you thinking"),
    Post(userId=userId, title="What are you doing?"),
    Post(userId=userId, title="What are we?"),
]
row_count = db.commit_bulk(posts)
```

> Unlike the `commit`, `commit_bulk` method returns the row count of the inserted documents rather that individual `id` of those document.

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

4. Deleting a record

With the `delete_by_pk` method you can delete a record in a database based on the primary-key value:

```py
affected_rows = db.delete_by_pk(User, userId)
```

You cal also use `filters` to delete a record in a database. The `delete_one` function allows you to delete a single record in a database that matches a filter.

```py
affected_rows = db.delete_one(User, {"name": "Crispen"})
```

You can also the `delete_bulk` which delete a lot of records that matches a filter:

```py
affected_rows = db.delete_bulk(User, {"name": "Crispen"})
```

### Associations

With `dataloom` you can define models that have relationships. Let's say we have a model called `Post` and every post should belong to a single `User`. Here is how you can define model mappings between a `Post` and a `User` using the `ForeignKeyColumn()`

```py

from dataloom import Column, CreatedAtColumn, UpdatedAtColumn, ForeignKeyColumn

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

```

So to insert a single post you first need to have a user that will create a post. Here is an example on how it is done:

```py
user = User(name="Crispen", username="heyy")
userId = db.commit(user)

post = Post(userId=userId, title="What are you thinking")
db.commit(post)
post = Post(userId=userId, title="What are you thinking")
db.commit(post)
post = Post(userId=userId, title="What are we?")
db.commit(post)
```

> We have created `3` posts that belongs to `Crispen`.

<table border="1">
  <thead>
    <tr><th>Argument</th><th>Description</th>
      <th>Type</th><th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td><td></td>
      <td></td><td></td>
    </tr>
  </tbody>
</table>
