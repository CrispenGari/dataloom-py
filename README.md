### dataloom

**`dataloom`** is a lightweight and versatile Object-Relational Mapping (ORM) library for Python. With support for `PostgreSQL`, `MySQL`, and `SQLite3` databases, `dataloom` simplifies database interactions, providing a seamless experience for developers.

<p align="center">
<img src="/dataloom.png" alt="dataloom" width="200">
</p>

### Table of Contents

- [dataloom](#dataloom)
- [Table of Contents](#table-of-contents)
- [Key Features:](#key-features)
- [Installation](#installation)
- [Python Version Compatibility](#python-version-compatibility)
- [Usage](#usage)
- [Connection](#connection)
- [Dataloom Classes](#dataloom-classes)
  - [`Model` Class](#model-class)
  - [`Column` Class](#column-class)
  - [`PrimaryKeyColumn` Class](#primarykeycolumn-class)
  - [`ForeignKeyColumn` Class](#foreignkeycolumn-class)
  - [`CreatedAtColumn` Class](#createdatcolumn-class)
  - [`UpdatedAtColumn` Class](#updatedatcolumn-class)
- [Syncing Tables](#syncing-tables)
- [CRUD Operations with Dataloom](#crud-operations-with-dataloom)
  - [1. Creating a Record](#1-creating-a-record)
  - [2. Getting records](#2-getting-records)
  - [3. Getting a single record](#3-getting-a-single-record)
  - [4. Deleting a record](#4-deleting-a-record)
  - [5. Updating a record](#5-updating-a-record)
- [Associations](#associations)

### Key Features:

- **Lightweight**: `dataloom` is designed to be minimalistic and easy to use, ensuring a streamlined `ORM` experience without unnecessary complexities.

- **Database Support**: `dataloom` supports popular relational databases such as `PostgreSQL`, `MySQL`, and `SQLite3`, making it suitable for a variety of projects.

- **Simplified Querying**: The `ORM` simplifies the process of database querying, allowing developers to interact with the database using Python classes and methods rather than raw SQL queries.

- **Intuitive Syntax**: `dataloom`'s syntax is intuitive and `Pythonic`, making it accessible for developers familiar with the Python language.

- **Flexible Data Types**: The `ORM` seamlessly handles various data types, offering flexibility in designing database schemas.

### Installation

To install `dataloom`, you just need to run the following command using `pip`:

```bash
pip install dataloom
```

### Python Version Compatibility

`dataloom` supports **`Python`** version **`3.12`** and above. Ensure that you are using a compatible version of **`Python`** before installing or using `dataloom`.

You can check your **`Python`** version by running:

```bash
python --version
```

### Usage

In this section we are going to go through how you can use our `orm` package in your project.

### Connection

To use Dataloom, you need to establish a connection with a specific database dialect. The available dialect options are `mysql`, `postgres`, and `sqlite`. In this example, we'll demonstrate how to set up a connection to a PostgreSQL database named "hi" using the `postgres` dialect. The following is an example of how you can establish a connection with postgres database.

```python
from dataloom import Dataloom

# Create a Dataloom instance with PostgreSQL configuration
pg_loom = Dataloom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    host="localhost",
    logging=True,
    logs_filename="logs.sql",
    port=5432,
)

# Connect to the PostgreSQL database
conn = pg_loom.connect()


# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

To establish a connection with a `MySQL` database using Dataloom, you can use the following example:

```python
from dataloom import Dataloom

# Create a Dataloom instance with MySQL configuration
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

# Connect to the MySQL database
conn = mysql_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()

```

To establish a connection with an `SQLite` database using Dataloom, you can use the following example:

```python
from dataloom import Dataloom

# Create a Dataloom instance with SQLite configuration
sqlite_loom = Dataloom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    logging=True
)

# Connect to the SQLite database
conn = sqlite_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

The `Dataloom` class takes in the following options:
| Parameter | Description | Value Type | Default Value | Required |
| --------------- | --------------------------------------------------------------------------------- | --------------- | -------------- | -------- |
| `dialect` | Dialect for the database connection. Options are `mysql`, `postgres`, or `sqlite` | `str` or `None` | `None` | `Yes` |
| `database` | Name of the database for `mysql` and `postgres`, filename for `sqlite` | `str` or `None` | `None` | `Yes` |
| `password` | Password for the database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `user` | Database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `host` | Database host (only for `mysql` and `postgres`) | `str` or `None` | `localhost` | `No` |
| `logging` | Enable logging for the database queries | `bool` | `True` | `No` |
| `logs_filename` | Filename for the query logs | `str` or `None` | `dataloom.sql` | `No` |
| `port` | Port number for the database connection (only for `mysql` and `postgres`) | `int` or `None` | `None` | `No` |

### Dataloom Classes

#### `Model` Class

A model in Dataloom is a top-level class that facilitates the creation of complex SQL tables using regular Python classes. This example demonstrates how to define two tables, `User` and `Post`, by creating classes that inherit from the `Model` class.

```py
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

class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)

    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(
        type="varchar",
        length=255,
        nullable=False,
    )
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

```

- Within the `User` model definition, the table name is explicitly specified using the `__tablename__` property, set to `"users"`. This informs `dataloom` to use the provided name instead of automatically deriving it from the class name. If `__tablename__` is not specified, the class name becomes the default table name during the synchronization of tables. To achieve this, the `TableColumn` class is used, accepting the specified table name as an argument.
- Every table must include exactly one primary key column. To define this, the `PrimaryKeyColumn` class is employed, signaling to `dataloom` that the specified field is a primary key.
- The `Column` class represents a regular column, allowing the inclusion of various options such as type and whether it is required.
- The `CreatedAtColumn` and `UpdatedAt` column types are automatically generated by the database as timestamps. If timestamps are unnecessary or only one of them is needed, they can be omitted.
- The `ForeignKeyColumn` establishes a relationship between the current (child) table and a referenced (parent) table.
- A `to_dict` property has been created, providing a convenient way to retrieve the data in the form of a Python dictionary when invoked.

#### `Column` Class

In the context of a database table, each property marked as a column in a model is treated as an individual attribute. Here's an example of how to define a column in a table using the `Column` class:

```python
username = Column(type="text", nullable=False, default="Hello there!!")
```

Here are some other options that you can pass to the `Column`:
| Argument | Description | Type | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------- | ------- |
| `type` | Required datatype of a column | any `datatype` | |
| `nullable` | Optional to specify if the column will allow null values or not. | `bool` | `False` |
| `length` | Optional to specify the length of the type. If passed as `N` with type `T`, it yields an SQL statement with type `T(N)`. | `int` \| `None` | `None` |
| `auto_increment` | Optional to specify if the column will automatically increment or not. | `bool` | `False` |
| `default` | Optional to specify the default value in a column. | `any` | `None` |
| `unique` | Optional to specify if the column will contain unique values or not. | `bool` | `False` |

> Talking about data types, each `dialect` has its own accepted values. Here is a list of types supported by each and every `dialect`:

1. `mysql`

   - `"int"` - Integer data type.
   - `"smallint"` - Small integer data type.
   - `"bigint"` - Big integer data type.
   - `"float"` - Floating-point number data type.
   - `"double"` - Double-precision floating-point number data type.
   - `"numeric"` - Numeric or decimal data type.
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"blob"` - Binary Large Object (BLOB) data type.

2. `postgres`

   - `"int"` - Integer data type (Alias: `"INTEGER"`).
   - `"smallint"` - Small integer data type (Alias: `"SMALLINT"`).
   - `"bigint"` - Big integer data type (Alias: `"BIGINT"`).
   - `"serial"` - Auto-incrementing integer data type (Alias: `"SERIAL"`).
   - `"bigserial"` - Auto-incrementing big integer data type (Alias: `"BIGSERIAL"`).
   - `"smallserial"` - Auto-incrementing small integer data type (Alias: `"SMALLSERIAL"`).
   - `"float"` - Real number data type (Alias: `"REAL"`).
   - `"double precision"` - Double-precision floating-point number data type (Alias: `"DOUBLE PRECISION"`).
   - `"numeric"` - Numeric data type (Alias: `"NUMERIC"`).
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"interval"` - Time interval data type.
   - `"uuid"` - UUID (Universally Unique Identifier) data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"jsonb"` - Binary JSON (JavaScript Object Notation) data type.
   - `"bytea"` - Binary data type (Array of bytes).
   - `"array"` - Array data type.
   - `"inet"` - IP network address data type.
   - `"cidr"` - Classless Inter-Domain Routing (CIDR) address data type.
   - `"macaddr"` - MAC (Media Access Control) address data type.
   - `"tsvector"` - Text search vector data type.
   - `"point"` - Geometric point data type.
   - `"line"` - Geometric line data type.
   - `"lseg"` - Geometric line segment data type.
   - `"box"` - Geometric box data type.
   - `"path"` - Geometric path data type.
   - `"polygon"` - Geometric polygon data type.
   - `"circle"` - Geometric circle data type.
   - `"hstore"` - Key-value pair store data type.

3. `sqlite`
   - `"int"` - Integer data type (Alias: `"INTEGER"`).
   - `"smallint"` - Small integer data type (Alias: `"SMALLINT"`).
   - `"bigint"` - Big integer data type (Alias: `"BIGINT"`).
   - `"float"` - Real number data type (Alias: `"REAL"`).
   - `"double precision"` - Double-precision floating-point number data type (Alias: `"DOUBLE"`).
   - `"numeric"` - Numeric data type (Alias: `"NUMERIC"`).
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"blob"` - Binary Large Object (BLOB) data type.

> Note: Every table is required to have a primary key column and this column should be 1. Let's talk about the `PrimaryKeyColumn`

#### `PrimaryKeyColumn` Class

This class is used to create a unique index in every table you create. In the context of a table that inherits from the `Model` class, exactly one `PrimaryKeyColumn` is required. Below is an example of creating an `id` column as a primary key in a table named `Post`:

```python
class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    #...rest of your columns

```

The following are the arguments that the `PrimaryKeyColumn` class accepts.
| Argument | Description | Type | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------- |
| `type` | The datatype of your primary key. | `str` | `"bigserial`" |
| `length` | Optional to specify the length of the type. If passed as `N` with type `T`, it yields an SQL statement with type `T(N)`. | `int` \| `None` | `None` |
| `auto_increment`| Optional to specify if the column will automatically increment or not. |`bool` |`False` |
|`default` | Optional to specify the default value in a column. |`any` |`None` |
|`nullable` | Optional to specify if the column will allow null values or not. |`bool` |`False` |
|`unique` | Optional to specify if the column will contain unique values or not. |`bool` |`True` |

#### `ForeignKeyColumn` Class

This class is utilized when informing `dataloom` that a column has a relationship with a primary key in another table. Consider the following model definition of a `Post`:

```py
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

```

- `userId` is a foreign key in the table `posts`, indicating it has a relationship with a primary key in the `users` table.

This column accepts the following arguments:
| Argument | Description | Type | Default |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------- |
| `table` | Required. This is the parent table that the current model references. In our example, this is referred to as `User`. | `Model` | |
| `type` | Optional. Specifies the data type of the foreign key. If not provided, dataloom can infer it from the parent table. | `str` \| `None` | `None` |
| `required` | Optional. Indicates whether the foreign key is required or not. | `bool` | `False` |
| `onDelete` | Optional. Specifies the action to be taken when the associated record in the parent table is deleted. | `str` [`"NO ACTION"`, `"SET NULL"`, `"CASCADE"`] | `"NO ACTION"` |
| `onUpdate` | Optional. Specifies the action to be taken when the associated record in the parent table is updated. | str [`"NO ACTION"`, `"SET NULL"`, `"CASCADE"`] | `"NO ACTION"` |

It is crucial to specify the actions for `onDelete` and `onUpdate` to ensure that `dataloom` manages your model's relationship actions appropriately. The available actions are:

1. `"NO ACTION"` - If you delete or update the parent table, no changes will occur in the child table.
2. `"SET NULL"` - If you delete or update the parent table, the corresponding value in the child table will be set to `null`.
3. `"CASCADE"` - If you delete or update the table, the same action will also be applied to the child table.

#### `CreatedAtColumn` Class

When a column is designated as `CreatedAtColumn`, its value will be automatically generated each time you create a new record in a database, serving as a timestamp.

#### `UpdatedAtColumn` Class

When a column is designated as `UpdatedAtColumn`, its value will be automatically generated each time you create a new record or update an existing record in a database table, acting as a timestamp.

### Syncing Tables

Syncing tables involves the process of creating tables from models and saving them to a database. After defining your tables, you will need to synchronize your database tables using the `sync` method. This method enables you to create and save tables into the database. For instance, if you have two models, `User` and `Post`, and you want to synchronize them with the database, you can achieve it as follows:

```py
tables = sqlite_loom.sync([Post, User], drop=True, force=True)
print(tables)
```

The method returns a list of table names that have been created or that exist in your database. The `sync` method accepts the following arguments:

| Argument | Description                                                     | Type   | Default |
| -------- | --------------------------------------------------------------- | ------ | ------- |
| `models` | A list of your table classes that inherit from the Model class. | `list` | `[]`    |
| `drop`   | Whether to drop tables during syncing or not.                   | `bool` | `False` |
| `force`  | Forcefully drop tables during syncing or not.                   | `bool` | `False` |
| `alter`  | Alter tables instead of dropping them during syncing or not.    | `bool` | `False` |

> We've noticed two steps involved in starting to work with our `orm`. Initially, you need to create a connection and then synchronize the tables in another step. The `connect_and_sync` function proves to be very handy as it handles both the database connection and table synchronization. Here is an example demonstrating its usage:

```py
# ....

sqlite_loom = Dataloom(
    dialect="sqlite", database="hi.db", logs_filename="sqlite-logs.sql", logging=True
)
conn, tables = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
print(tables)

if __name__ == "__main__":
    conn.close()
```

Returns a `conn` and the list of `tablenames` that exist in the database. The method accepts the same arguments as the `sync` method.

### CRUD Operations with Dataloom

In this section of the documentation, we will illustrate how to perform basic `CRUD` operations using `dataloom` on simple `Models`. Please note that in the following code snippets, I will be utilizing `sqlite_loom`. However, it's important to highlight that you can use any `loom` of your choice to follow along.

#### 1. Creating a Record

The `insert_one` method allows you to save a single row in a specific table. Upon saving, it will return the primary key (`pk`) value of the inserted document.

```python
# Example: Creating a user record
user = User(username="@miller")
user_id = sqlite_loom.insert_one(user)
```

The `insert_bulk` method facilitates the bulk insertion of records, as its name suggests. The following example illustrates how you can add `3` posts to the database table simultaneously.

```python
# Example: Inserting multiple posts
posts = [
    Post(userId=userId, title="What are you thinking"),
    Post(userId=userId, title="What are you doing?"),
    Post(userId=userId, title="What are we?"),
]
row_count = sqlite_loom.insert_bulk(posts)
```

> In contrast to the `insert_one` method, the `insert_bulk` method returns the row count of the inserted documents rather than the individual primary keys (`pks`) of those documents.

#### 2. Getting records

To retrieve records from the database, you can utilize the `find_all()` and `find_many()` methods.

```py
users = sqlite_loom.find_all(User)
print([u.to_dict for u in users])
```

Here is an example demonstrating the usage of the `find_many()` function with specific filters.

```py
many = sqlite_loom.find_many(Post, {"userId": 5})
print([u.to_dict for u in many])
```

The distinction between the `find_all()` and `find_many()` methods lies in the fact that `find_many()` enables you to apply specific filters, whereas `find_all()` retrieves all the documents within the specified model.

#### 3. Getting a single record

The `find_by_pk()` and `find_one()` methods are employed to locate a single record in the database.

```py
user = User(name="Crispen", username="heyy")
me = sqlite_loom.find_by_pk(User, 1)
print(me.to_dict)

```

With the `find_one()` method, you can specify the filters of your query as follows:

```py
him = sqlite_loom.find_one(User, filters={"id": 1})
print(him.to_dict)
```

#### 4. Deleting a record

Using the `delete_by_pk()` method, you can delete a record in a database based on the primary-key value.

```py
affected_rows = sqlite_loom.delete_by_pk(User, userId)
```

You can also use `filters` to delete a record in a database. The `delete_one()` function enables you to delete a single record in a database that matches a filter.

```py
affected_rows = sqlite_loom.delete_one(User, {"name": "Crispen"})
```

You can also use the `delete_bulk()` method to delete a multitude of records that match a given filter:

```py
affected_rows = sqlite_loom.delete_bulk(User, {"name": "Crispen"})
```

#### 5. Updating a record

To update a record in a database table, you can utilize the methods `update_by_pk()`, `update_one()`, and `update_bulk()`. The `update_pk()` method can be used as follows:

```py
affected_rows = sqlite_loom.update_by_pk(User, 1, {"name": "Gari"})
```

Here is an example illustrating how to use the `update_one()` method:

```py
affected_rows = sqlite_loom.update_one(User, {"name": "Crispen"}, {"name": "Gari"})
```

The `update_bulk()` method updates all records that match a filter in a database table.

```py
affected_rows = sqlite_loom.update_bulk(User, {"name": "Crispen"}, {"name": "Tinashe Gari"})
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
userId = db.create(user)

post = Post(userId=userId, title="What are you thinking")
db.create(post)
post = Post(userId=userId, title="What are you thinking")
db.create(post)
post = Post(userId=userId, title="What are we?")
db.create(post)
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
