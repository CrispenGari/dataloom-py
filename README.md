### dataloom

**`dataloom`** is a lightweight and versatile Object-Relational Mapping (ORM) library for Python. With support for `PostgreSQL`, `MySQL`, and `SQLite3` databases, `dataloom` simplifies database interactions, providing a seamless experience for developers.

<p align="center">
<img src="https://raw.githubusercontent.com/CrispenGari/dataloom-py/main/dataloom.png" alt="dataloom" width="200">
</p>

---

<p align="center">
  <a href="https://pypi.python.org/pypi/dataloom"><img src="https://badge.fury.io/py/dataloom.svg"></a>
  <a href="https://github.com/crispengari/dataloom/actions/workflows/ci.yml"><img src="https://github.com/crispengari/dataloom/actions/workflows/ci.yml/badge.svg"></a>
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green"></a>
  <a href="https://pypi.python.org/pypi/dataloom"><img src="https://img.shields.io/pypi/pyversions/dataloom.svg"></a>
</p>

#### Why choose `dataloom`?

1. **Ease of Use**: `dataloom` offers a user-friendly interface, making it straightforward to work with.
2. **Flexible SQL Driver**: Write one codebase and seamlessly switch between `PostgreSQL`, `MySQL`, and `SQLite3` drivers as needed.
3. **Lightweight**: Despite its powerful features, `dataloom` remains lightweight, ensuring efficient performance.
4. **Comprehensive Documentation**: Benefit from extensive documentation that guides users through various functionalities and use cases.
5. **Active Maintenance**: `dataloom` is actively maintained, ensuring ongoing support and updates for a reliable development experience.
6. **Cross-platform Compatibility**: `dataloom` works seamlessly across different operating systems, including `Windows`, `macOS`, and `Linux`.
7. **Scalability**: Scale your application effortlessly with `dataloom`, whether it's a small project or a large-scale enterprise application.

### Table of Contents

- [dataloom](#dataloom)
  - [Why choose `dataloom`?](#why-choose-dataloom)
- [Table of Contents](#table-of-contents)
- [Key Features:](#key-features)
- [Installation](#installation)
- [Python Version Compatibility](#python-version-compatibility)
- [Usage](#usage)
- [Connection](#connection)
  - [`Postgres`](#postgres)
  - [`MySQL`](#mysql)
  - [`SQLite`](#sqlite)
- [Dataloom Classes](#dataloom-classes)
  - [`Loom` Class](#loom-class)
  - [`Model` Class](#model-class)
  - [`Column` Class](#column-class)
    - [Column Datatypes](#column-datatypes)
      - [1. `mysql`](#1-mysql)
      - [2. `postgres`](#2-postgres)
      - [3. `sqlite`](#3-sqlite)
  - [`PrimaryKeyColumn` Class](#primarykeycolumn-class)
  - [`ForeignKeyColumn` Class](#foreignkeycolumn-class)
  - [`CreatedAtColumn` Class](#createdatcolumn-class)
  - [`UpdatedAtColumn` Class](#updatedatcolumn-class)
  - [`Filter` Class](#filter-class)
  - [`ColumnValue` Class](#columnvalue-class)
  - [`Order` Class](#order-class)
  - [`Include` Class](#include-class)
  - [`Group` Class](#group-class)
  - [`Having` Class](#having-class)
- [Syncing Tables](#syncing-tables)
  - [1. The `sync` method.](#1-the-sync-method)
  - [2. The `connect_and_sync` method.](#2-the-connect_and_sync-method)
- [CRUD Operations with Dataloom](#crud-operations-with-dataloom)
  - [1. Creating a Record](#1-creating-a-record)
    - [1. `insert_one()`](#1-insert_one)
    - [2. `insert_bulk()`.](#2-insert_bulk)
  - [2. Reading records](#2-reading-records)
    - [1. `find_all()`](#1-find_all)
    - [2. `find_many()`](#2-find_many)
    - [3. `find_one()`](#3-find_one)
    - [4. `find_by_pk()`](#4-find_by_pk)
  - [3. Updating a record](#3-updating-a-record)
    - [1. `update_by_pk()`](#1-update_by_pk)
    - [2. `update_one()`](#2-update_one)
    - [3. `update_bulk()`](#3-update_bulk)
  - [4. Deleting a record](#4-deleting-a-record)
    - [1. `delete_by_pk()`](#1-delete_by_pk)
    - [2. `delete_one()`](#2-delete_one)
    - [3. `delete_bulk()`](#3-delete_bulk)
      - [Warning: Potential Risk with `delete_bulk()`](#warning-potential-risk-with-delete_bulk)
      - [Guidelines for Safe Usage](#guidelines-for-safe-usage)
- [Ordering](#ordering)
- [Filters](#filters)
    - [Operators](#operators)
- [Data Aggregation](#data-aggregation)
  - [Aggregation Functions](#aggregation-functions)
- [Utilities](#utilities)
  - [1. `inspect()`](#1-inspect)
  - [2. `decorators`](#2-decorators)
    - [`@initialize()`](#initialize)
  - [3. `count()`](#3-count)
  - [4. `min()`](#4-min)
  - [5. `max()`](#5-max)
  - [6. `avg()`](#6-avg)
  - [7. `sum()`](#7-sum)
- [Associations](#associations)
  - [1. `1-1` Association](#1-1-1-association)
    - [Inserting](#inserting)
    - [Retrieving Records](#retrieving-records)
  - [2. `N-1` Association](#2-n-1-association)
    - [Inserting](#inserting-1)
    - [Retrieving Records](#retrieving-records-1)
  - [3. `1-N` Association](#3-1-n-association)
    - [Inserting](#inserting-2)
    - [Retrieving Records](#retrieving-records-2)
  - [4. What about bidirectional queries?](#4-what-about-bidirectional-queries)
    - [1. Child to Parent](#1-child-to-parent)
    - [2. Parent to Child](#2-parent-to-child)
  - [5. `Self` Association](#5-self-association)
    - [Inserting](#inserting-3)
    - [Retrieving Records](#retrieving-records-3)
  - [6. `N-N` Relationship](#6-n-n-relationship)
    - [Inserting](#inserting-4)
    - [Retrieving Records](#retrieving-records-4)
- [Query Builder.](#query-builder)
  - [Why Use Query Builder?](#why-use-query-builder)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

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

To use Dataloom, you need to establish a connection with a specific database `dialect`. The available dialect options are `mysql`, `postgres`, and `sqlite`.

#### `Postgres`

The following is an example of how you can establish a connection with postgres database.

```python
from dataloom import Loom

# Create a Loom instance with PostgreSQL configuration
pg_loom = Loom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    host="localhost",
    sql_logger="console",
    logs_filename="logs.sql",
    port=5432,
)

# Connect to the PostgreSQL database
conn = pg_loom.connect()


# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

In `dataloom` you can use connection uris to establish a connection to the database in `postgres` as follows:

```py
pg_loom = Loom(
    dialect="postgres",
    connection_uri = "postgressql://root:root@localhost:5432/hi",
   # ...
)
```

This will establish a connection with `postgres` with the database `hi`.

#### `MySQL`

To establish a connection with a `MySQL` database using `Loom`, you can use the following example:

```python
from dataloom import Loom

# Create a Loom instance with MySQL configuration
mysql_loom = Loom(
    dialect="mysql",
    database="hi",
    password="root",
    user="root",
    host="localhost",
    sql_logger="console",
    logs_filename="logs.sql",
    port=3306,
)

# Connect to the MySQL database
conn = mysql_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()

```

In `dataloom` you can use connection uris to establish a connection to the database in `mysql` as follows:

```py
mysql_loom = Loom(
    dialect="mysql",
    connection_uri = "mysql://root:root@localhost:3306/hi",
   # ...
)
```

This will establish a connection with `mysql` with the database `hi`.

#### `SQLite`

To establish a connection with an `SQLite` database using `Loom`, you can use the following example:

```python
from dataloom import Loom

# Create a Loom instance with SQLite configuration
sqlite_loom = Loom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    logging=True,
    sql_logger="console",
)

# Connect to the SQLite database
conn = sqlite_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

In `dataloom` you can use connection uris to establish a connection to the database in `sqlite` as follows:

```py
sqlite_loom = Loom(
    dialect="sqlite",
   connection_uri = "sqlite:///hi.db",
   # ...
)
```

This will establish a connection with `sqlite` with the database `hi`.

### Dataloom Classes

The following are the list of classes that are available in `dataloom`.

#### `Loom` Class

This class is used to create a loom object that will be use to perform actions to a database. The following example show how you can create a `loom` object using this class.

```python
from dataloom import Loom
loom = Loom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    host="localhost",
    sql_logger="console",
    logs_filename="logs.sql",
    port=5432,
)

# OR with connection_uri
loom = Loom(
    dialect="mysql",
    connection_uri = "mysql://root:root@localhost:3306/hi",
   # ...
)
```

The `Loom` class takes in the following options:
| Parameter | Description | Value Type | Default Value | Required |
| --------------- | --------------------------------------------------------------------------------- | --------------- | -------------- | -------- |
| `connection_uri` | The connection `uri` for the specified dialect. | `str` or `None` | `None` | `No` |
| `dialect` | Dialect for the database connection. Options are `mysql`, `postgres`, or `sqlite` | `"mysql" \| "postgres" \| "sqlite"` | `None` | `Yes` |
| `database` | Name of the database for `mysql` and `postgres`, filename for `sqlite` | `str` or `None` | `None` | `No` |
| `password` | Password for the database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `user` | Database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `host` | Database host (only for `mysql` and `postgres`) | `str` or `None` | `localhost` | `No` |
| `sql_logger` | Enable logging for the database queries. If you don't want to see the sql logs you can set this option to `None` which is the default value. If you set it to `file` then you will see the logs in the default `dataloom.sql` file, you can overide this by passing a `logs_filename` option. Setting this option to `console`, then sql statements will be printed on the console. | `console`or `file` or `None`| `True` | `No` |
| `logs_filename` | Filename for the query logs | `str` or `None` | `dataloom.sql` | `No` |
| `port` | Port number for the database connection (only for `mysql` and `postgres`) | `int` or `None` | `None` | `No` |

#### `Model` Class

A model in Dataloom is a top-level class that facilitates the creation of complex SQL tables using regular Python classes. This example demonstrates how to define two tables, `User` and `Post`, by creating classes that inherit from the `Model` class.

```py
from dataloom import (
    Loom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
)

class User(Model):
    __tablename__:TableColumn = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)

    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()


class Post(Model):
    __tablename__: TableColumn = TableColumn(name="posts")
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
```

- Within the `User` model definition, the table name is explicitly specified using the `__tablename__` property, set to `"users"`. This informs `dataloom` to use the provided name instead of automatically deriving it from the class name. If `TableColumn` is not specified, the class name becomes the default table name during the synchronization of tables. To achieve this, the `TableColumn` class is used, accepting the specified table name as an argument.

> 👉:**Note:** When defining a table name, it's not necessary to specify the property as `__tablename__`. However, it's considered good practice to name your table column like that to avoid potential clashes with other columns in the table.

- Every table must include exactly one primary key column unless it is a `joint_table` for `N-N` relations that requires no primary key column. To define this, the `PrimaryKeyColumn` class is employed, signaling to `dataloom` that the specified field is a primary key.
- The `Column` class represents a regular column, allowing the inclusion of various options such as type and whether it is required.
- The `CreatedAtColumn` and `UpdatedAt` column types are automatically generated by the database as timestamps. If timestamps are unnecessary or only one of them is needed, they can be omitted.
- The `ForeignKeyColumn` establishes a relationship between the current (child) table and a referenced (parent) table.

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

##### Column Datatypes

In this section we will list all the `datatypes` that are supported for each dialect.

###### 1. `mysql`

| Data Type     | Description                                       |
| ------------- | ------------------------------------------------- |
| `"int"`       | Integer data type.                                |
| `"smallint"`  | Small integer data type.                          |
| `"bigint"`    | Big integer data type.                            |
| `"float"`     | Floating-point number data type.                  |
| `"double"`    | Double-precision floating-point number data type. |
| `"numeric"`   | Numeric or decimal data type.                     |
| `"text"`      | Text data type.                                   |
| `"varchar"`   | Variable-length character data type.              |
| `"char"`      | Fixed-length character data type.                 |
| `"boolean"`   | Boolean data type.                                |
| `"date"`      | Date data type.                                   |
| `"time"`      | Time data type.                                   |
| `"timestamp"` | Timestamp data type.                              |
| `"json"`      | JSON (JavaScript Object Notation) data type.      |
| `"blob"`      | Binary Large Object (BLOB) data type.             |

###### 2. `postgres`

| Data Type            | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| `"int"`              | Integer data type (Alias: `"INTEGER"`).                                         |
| `"smallint"`         | Small integer data type (Alias: `"SMALLINT"`).                                  |
| `"bigint"`           | Big integer data type (Alias: `"BIGINT"`).                                      |
| `"serial"`           | Auto-incrementing integer data type (Alias: `"SERIAL"`).                        |
| `"bigserial"`        | Auto-incrementing big integer data type (Alias: `"BIGSERIAL"`).                 |
| `"smallserial"`      | Auto-incrementing small integer data type (Alias: `"SMALLSERIAL"`).             |
| `"float"`            | Real number data type (Alias: `"REAL"`).                                        |
| `"double precision"` | Double-precision floating-point number data type (Alias: `"DOUBLE PRECISION"`). |
| `"numeric"`          | Numeric data type (Alias: `"NUMERIC"`).                                         |
| `"text"`             | Text data type.                                                                 |
| `"varchar"`          | Variable-length character data type.                                            |
| `"char"`             | Fixed-length character data type.                                               |
| `"boolean"`          | Boolean data type.                                                              |
| `"date"`             | Date data type.                                                                 |
| `"time"`             | Time data type.                                                                 |
| `"timestamp"`        | Timestamp data type.                                                            |
| `"interval"`         | Time interval data type.                                                        |
| `"uuid"`             | UUID (Universally Unique Identifier) data type.                                 |
| `"json"`             | JSON (JavaScript Object Notation) data type.                                    |
| `"jsonb"`            | Binary JSON (JavaScript Object Notation) data type.                             |
| `"bytea"`            | Binary data type (Array of bytes).                                              |
| `"array"`            | Array data type.                                                                |
| `"inet"`             | IP network address data type.                                                   |
| `"cidr"`             | Classless Inter-Domain Routing (CIDR) address data type.                        |
| `"macaddr"`          | MAC (Media Access Control) address data type.                                   |
| `"tsvector"`         | Text search vector data type.                                                   |
| `"point"`            | Geometric point data type.                                                      |
| `"line"`             | Geometric line data type.                                                       |
| `"lseg"`             | Geometric line segment data type.                                               |
| `"box"`              | Geometric box data type.                                                        |
| `"path"`             | Geometric path data type.                                                       |
| `"polygon"`          | Geometric polygon data type.                                                    |
| `"circle"`           | Geometric circle data type.                                                     |
| `"hstore"`           | Key-value pair store data type.                                                 |

###### 3. `sqlite`

| Data Type            | Description                                       |
| -------------------- | ------------------------------------------------- |
| `"int"`              | Integer data type.                                |
| `"smallint"`         | Small integer data type.                          |
| `"bigint"`           | Big integer data type.                            |
| `"float"`            | Real number data type.                            |
| `"double precision"` | Double-precision floating-point number data type. |
| `"numeric"`          | Numeric data type.                                |
| `"text"`             | Text data type.                                   |
| `"varchar"`          | Variable-length character data type.              |
| `"char"`             | Fixed-length character data type.                 |
| `"boolean"`          | Boolean data type.                                |
| `"date"`             | Date data type.                                   |
| `"time"`             | Time data type.                                   |
| `"timestamp"`        | Timestamp data type.                              |
| `"json"`             | JSON (JavaScript Object Notation) data type.      |
| `"blob"`             | Binary Large Object (BLOB) data type.             |

> Note: Every table that is not a `joint_table` is required to have a primary key column and this column should be 1. Let's talk about the `PrimaryKeyColumn`

#### `PrimaryKeyColumn` Class

This class is used to create a unique index in every table you create. In the context of a table that inherits from the `Model` class, exactly one `PrimaryKeyColumn` is required. Below is an example of creating an `id` column as a primary key in a table named `Post`:

```python
class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    #...rest of your columns

```

The following are the arguments that the `PrimaryKeyColumn` class accepts.

| Argument         | Description                                                                                                              | Type            | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------- | ------- |
| `type`           | The datatype of your primary key.                                                                                        | `str`           | `"int`" |
| `length`         | Optional to specify the length of the type. If passed as `N` with type `T`, it yields an SQL statement with type `T(N)`. | `int` \| `None` | `None`  |
| `auto_increment` | Optional to specify if the column will automatically increment or not.                                                   | `bool`          | `False` |
| `default`        | Optional to specify the default value in a column.                                                                       | `any`           | `None`  |
| `nullable`       | Optional to specify if the column will allow null values or not.                                                         | `bool`          | `False` |
| `unique`         | Optional to specify if the column will contain unique values or not.                                                     | `bool`          | `True`  |

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
| `table` | Required. This is the parent table that the current model references. In our example, this is referred to as `User`. It can be used as a string in self relations. | `Model`\| `str` | |
| `type` | Optional. Specifies the data type of the foreign key. If not provided, dataloom can infer it from the parent table. | `str` \| `None` | `None` |
| `required` | Optional. Indicates whether the foreign key is required or not. | `bool` | `False` |
| `onDelete` | Optional. Specifies the action to be taken when the associated record in the parent table is deleted. |`"NO ACTION"`, `"SET NULL"`, `"CASCADE"` | `"NO ACTION"` |
| `onUpdate` | Optional. Specifies the action to be taken when the associated record in the parent table is updated. | `"NO ACTION"`, `"SET NULL"`, `"CASCADE"`| `"NO ACTION"` |

It is crucial to specify the actions for `onDelete` and `onUpdate` to ensure that `dataloom` manages your model's relationship actions appropriately. The available actions are:

1. `"NO ACTION"` - If you delete or update the parent table, no changes will occur in the child table.
2. `"SET NULL"` - If you delete or update the parent table, the corresponding value in the child table will be set to `null`.
3. `"CASCADE"` - If you delete or update the table, the same action will also be applied to the child table.

#### `CreatedAtColumn` Class

When a column is designated as `CreatedAtColumn`, its value will be automatically generated each time you create a new record in a database, serving as a timestamp.

#### `UpdatedAtColumn` Class

When a column is designated as `UpdatedAtColumn`, its value will be automatically generated each time you create a new record or update an existing record in a database table, acting as a timestamp.

#### `Filter` Class

This `Filter` class in `dataloom` is designed to facilitate the application of filters when executing queries and mutations. It allows users to specify conditions that must be met for the operation to affect certain rows in a database table. Below is an example demonstrating how this class can be used:

```python
affected_rows = pg_loom.update_one(
    Post,
    values=[
        ColumnValue(name="title", value="Hey"),
        ColumnValue(name="completed", value=True),
    ],
    filters=[
        Filter(column="id", value=1, join_next_with="AND"),
        Filter(column="userId", value=1, join_next_with="AND"),
    ],
)
```

So from the above example we are applying filters while updating a `Post` here are the options that you can pass on that filter class:
| Argument | Description | Type | Default |
|-------------------------|------------------------------------------------------------|-------------------------------------------|------------------------|
| `column` | The name of the column to apply the filter on | `String` | - |
| `value` | The value to filter against | `Any` | - |
| `operator` | The comparison operator to use for the filter | `'eq'`, `'neq'`. `'lt'`, `'gt'`, `'leq'`, `'geq'`, `'in'`, `'notIn'`, `'like'`, `'between'`, `'not'` | `'eq'` |
| `join_next_with` | The logical operator to join this filter with the next one | `'AND'`, `'OR'` | `'AND'` |

> 👍**Pro Tip:** Note You can apply either a list of filters or a single filter when filtering records.

#### `ColumnValue` Class

Just like the `Filter` class, `dataloom` also provides a `ColumnValue` class. This class acts as a setter to update the values of columns in your database table.

The following code snippet demonstrates how the `ColumnValue` class is used to update records in the database:

```py
re = pg_loom.update_one(
    Post,
    values=[
        ColumnValue(name="title", value="Hey"),
        ColumnValue(name="completed", value=True),
    ],
    filters=[
        Filter(column="id",  value=1, join_next_with="AND"),
        Filter(column="userId", value=1, join_next_with="AND"),
    ],
)
```

It accepts two arguments: `name` and `value`. name represents the column name, while value corresponds to the new value to be assigned to that column.

| Argument | Description                                                | Type  | Default |
| -------- | ---------------------------------------------------------- | ----- | ------- |
| `name`   | The name of the column to be updated or inserted.          | `str` | -       |
| `value`  | The value to assign to the column during update or insert. | `Any` | -       |

#### `Order` Class

The `Order` class enables us to specify the desired order in which documents should be returned. Below is an example illustrating its usage:

```py
posts = pg_loom.find_all(
    Post,
    select=["id", "completed", "title", "createdAt"],
    limit=3,
    offset=0,
    order=[
        Order(column="createdAt", order="ASC"),
        Order(column="id", order="DESC"),
    ]
)
```

> 👍**Pro Tip:** Note when utilizing a list of orders, they are applied sequentially, one after the other:

| Argument | Description                                                               | Type                | Default |
| -------- | ------------------------------------------------------------------------- | ------------------- | ------- |
| `column` | The name of the column to order by.                                       | `str`               | -       |
| `order`  | The order direction, either `"ASC"` (ascending) or `"DESC"` (descending). | `"ASC"` or `"DESC"` | `"ASC"` |

#### `Include` Class

The `Include` class facilitates eager loading for models with relationships. Below is a table detailing the parameters available for the `Include` class:

| Argument         | Description                                                                                 | Type                | Default  | Required |
| ---------------- | ------------------------------------------------------------------------------------------- | ------------------- | -------- | -------- |
| `model`          | The model to be included when eagerly fetching records.                                     | `Model`             | -        | Yes      |
| `junction_table` | The `junction_table` model that is used as a reference table in a many to many association. | `Model`             | `None`   | No       |
| `order`          | The list of order specifications for sorting the included data.                             | `list[Order]`       | `[]`     | No       |
| `limit`          | The maximum number of records to include.                                                   | `int \| None`       | `0`      | No       |
| `offset`         | The number of records to skip before including.                                             | `int \| None`       | `0`      | No       |
| `select`         | The list of columns to include.                                                             | `list[str] \| None` | `None`   | No       |
| `has`            | The relationship type between the current model and the included model.                     | `INCLUDE_LITERAL`   | `"many"` | No       |
| `include`        | The extra included models.                                                                  | `list[Include]`     | `[]`     | No       |
| `alias`          | The alias name for the included model. Very important when mapping self relations.          | `str`               | `None`   | No       |

#### `Group` Class

This class is used for data `aggregation` and grouping data in `dataloom`. Below is a table detailing the parameters available for the `Group` class:

| Argument                    | Description                                             | Type                                          | Default   | Required |
| --------------------------- | ------------------------------------------------------- | --------------------------------------------- | --------- | -------- |
| `column`                    | The name of the column to group by.                     | `str`                                         |           | Yes      |
| `function`                  | The aggregation function to apply on the grouped data.  | `"COUNT" \| "AVG" \| "SUM" \| "MIN" \| "MAX"` | `"COUNT"` | No       |
| `having`                    | Filters to apply to the grouped data.                   | `list[Having] \| Having \| None`              | `None`    | No       |
| `return_aggregation_column` | Whether to return the aggregation column in the result. | `bool`                                        | `False`   | No       |

#### `Having` Class

This class method is used to specify the filters to be applied on `Grouped` data during `aggregation` in `dataloom`. Below is a table detailing the parameters available for the `Group` class:

| Argument         | Description                                   | Type                                   | Default | Required |
| ---------------- | --------------------------------------------- | -------------------------------------- | ------- | -------- |
| `column`         | The name of the column to filter on.          | `str`                                  |         | `Yes`    |
| `operator`       | The operator to use for the filter.           | [`OPERATOR_LITERAL\|None`](#operators) | `"eq"`  | `No`     |
| `value`          | The value to compare against.                 | `Any`                                  |         | `Yes`    |
| `join_next_with` | The SQL operand to join the next filter with. | `"AND" \| "OR"\|None`                  | `"AND"` | `No`     |

### Syncing Tables

Syncing tables involves the process of creating tables from models and saving them to a database. After defining your tables, you will need to synchronize your database tables using the `sync` method.

#### 1. The `sync` method.

This method enables you to create and save tables into the database. For instance, if you have two models, `User` and `Post`, and you want to synchronize them with the database, you can achieve it as follows:

```py
tables = sqlite_loom.sync([Post, User], drop=True, force=True)
print(tables)
```

The method returns a list of table names that have been created or that exist in your database. The `sync` method accepts the following arguments:

| Argument | Description                                                                                                                 | Type                 | Default |
| -------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| `models` | A collection or a single instance(s) of your table classes that inherit from the Model class.                               | `list[Model]\|Model` | `[]`    |
| `drop`   | Whether to drop tables during syncing or not.                                                                               | `bool`               | `False` |
| `force`  | Forcefully drop tables during syncing. In `mysql` this will temporarily disable foreign key checks when droping the tables. | `bool`               | `False` |
| `alter`  | Alter tables instead of dropping them during syncing or not.                                                                | `bool`               | `False` |

> 🥇 **We recommend you to use `drop` or `force` if you are going to change or modify `foreign` and `primary` keys. This is because setting the option `alter` does not have an effect on `primary` key columns.**

> We've noticed two steps involved in starting to work with our `orm`. Initially, you need to create a connection and then synchronize the tables in another step.

#### 2. The `connect_and_sync` method.

The `connect_and_sync` function proves to be very handy as it handles both the database connection and table synchronization. Here is an example demonstrating its usage:

```py
# ....

sqlite_loom = Loom(
    dialect="sqlite", database="hi.db", logs_filename="sqlite-logs.sql", logging=True
)
conn, tables = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
print(tables)

if __name__ == "__main__":
    conn.close()
```

Returns a `conn` and the list of `tablenames` that exist in the database. The method accepts the same arguments as the `sync` method.

### CRUD Operations with Dataloom

In this section of the documentation, we will illustrate how to perform basic `CRUD` operations using `dataloom` on simple `Models`. Please note that in the following code snippets, I will be utilizing `sqlite_loom`, `mysql_loom`, `pg_loom` or `loom` interchangeably. However, it's important to highlight that you can use any `loom` of your choice to follow along.

#### 1. Creating a Record

To insert a single or multiple records in a database you make use of the following functions:

1. `insert_one()`
2. `insert_bulk()`

##### 1. `insert_one()`

The `insert_one` method allows you to save a single row in a specific table. Upon saving, it will return the primary key (`pk`) value of the inserted document. The following example shows how the `insert_one()` method works.

```python
# Example: Creating a user record
userId = pg_loom.insert_one(
    instance=User, values=ColumnValue(name="username", value="@miller")
)

userId = pg_loom.insert_one(
    instance=User,
    values=[
        ColumnValue(name="username", value="@miller"),
        ColumnValue(name="name", value="Jonh"),
    ],
)
```

This function takes in two arguments which are `instance` and `values`. Where values are the column values that you are inserting in a user table or a single column value.

| Argument   | Description                                                                                                  | `Type`                               | `Required` | `Default` |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------ | ---------- | --------- |
| `instance` | The instance of the table where the row will be inserted.                                                    | `Model`                              | `Yes`      | `None`    |
| `values`   | The column values to be inserted into the table. It can be a single column value or a list of column values. | `list[ColumnValue]` or `ColumnValue` | `Yes`      | `None`    |

##### 2. `insert_bulk()`.

The `insert_bulk` method facilitates the bulk insertion of records, as its name suggests. The following example illustrates how you can add `3` posts to the database table simultaneously.

```python
# Example: Inserting multiple posts
rows = pg_loom.insert_bulk(
    User,
    values=[
        [
            ColumnValue(name="username", value="@miller"),
            ColumnValue(name="name", value="Jonh"),
        ],
        [
            ColumnValue(name="username", value="@brown"),
            ColumnValue(name="name", value="Jonh"),
        ],
        [
            ColumnValue(name="username", value="@blue"),
            ColumnValue(name="name", value="Jonh"),
        ],
    ],
)
```

The argument parameters for the `insert_bulk` methods are as follows.

| Argument   | Description                                                                                                                                                                                                 | `Type`                                     | `Required` | `Default` |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------- | --------- |
| `instance` | The instance of the table where the row will be inserted.                                                                                                                                                   | `Model`                                    | `Yes`      | `None`    |
| `values`   | The column values to be inserted into the table. **It must be a list of list of column values with the same length, otherwise dataloom will fail to map the values correctly during the insert operation.** | `list[list[ColumnValue]]` or `ColumnValue` | `Yes`      | `None`    |

> In contrast to the `insert_one` method, the `insert_bulk` method returns the row count of the inserted documents rather than the individual primary keys (`pks`) of those documents.

#### 2. Reading records

To retrieve documents or a document from the database, you can make use of the following functions:

1. `find_all()`: This function is used to retrieve all documents from the database.
2. `find_by_pk()`: This function is used to retrieve a document by its primary key (or ID).
3. `find_one()`: This function is used to retrieve a single document based on a specific condition.
4. `find_many()`: This function is used to retrieve multiple documents based on a specific condition.

##### 1. `find_all()`

This method is used to retrieve all the records that are in the database table. Below are examples demonstrating how to do it:

```py
users = pg_loom.find_all(
    instance=User,
    select=["id", "username"],
    limit=3,
    offset=0,
    order=[Order(column="id", order="DESC")],
)
print(users) # ? [{'id': 1, 'username': '@miller'}]
```

The `find_all()` method takes in the following arguments:

| Argument   | Description                                                                                | Type                     | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                | `Model`                  | `None`  | `Yes`    |
| `select`   | Collection or a string of fields to select from the documents.                             | `list[str]\|str`         | `None`  | `No`     |
| `limit`    | Maximum number of documents to retrieve.                                                   | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before retrieving.                                             | `int`                    | `0`     | `No`     |
| `order`    | Collection of `Order` or a single `Order` to order the documents when querying.            | `list[Order]\|Order`     | `None`  | `No`     |
| `include`  | Collection or a `Include` of related models to eagerly load.                               | `list[Include]\|Include` | `None`  | `No`     |
| `group`    | Collection of `Group` which specifies how you want your data to be grouped during queries. | `list[Group]\|Group`     | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to return distinct row values based on selected fields or not.    | `bool`                   | `False` | `No`     |

> 👍 **Pro Tip**: A collection can be any python iterable, the supported iterables are `list`, `set`, `tuple`.

##### 2. `find_many()`

Here is an example demonstrating the usage of the `find_many()` function with specific filters.

```py
users = mysql_loom.find_many(
    User,
    filters=[Filter(column="username", value="@miller")],
    select=["id", "username"],
    offset=0,
    limit=10,
)

print(users) # ? [{'id': 1, 'username': '@miller'}]
```

The `find_many()` method takes in the following arguments:

| Argument   | Description                                                                                | Type                     | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                | `Model`                  | `None`  | `Yes`    |
| `select`   | Collection or a string of fields to select from the documents.                             | `list[str]\|str`         | `None`  | `No`     |
| `limit`    | Maximum number of documents to retrieve.                                                   | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before retrieving.                                             | `int`                    | `0`     | `No`     |
| `order`    | Collection of `Order` or a single `Order` to order the documents when querying.            | `list[Order]\|Order`     | `None`  | `No`     |
| `include`  | Collection or a `Include` of related models to eagerly load.                               | `list[Include]\|Include` | `None`  | `No`     |
| `group`    | Collection of `Group` which specifies how you want your data to be grouped during queries. | `list[Group]\|Group`     | `None`  | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the query.                                | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to return distinct row values based on selected fields or not.    | `bool`                   | `False` | `No`     |

> 👍 **Pro Tip**: The distinction between the `find_all()` and `find_many()` methods lies in the fact that `find_many()` enables you to apply specific filters, whereas `find_all()` retrieves all the documents within the specified model.

##### 3. `find_one()`

Here is an example showing you how you can use `find_one()` locate a single record in the database.

```py
user = mysql_loom.find_one(
    User,
    filters=[Filter(column="username", value="@miller")],
    select=["id", "username"],
)
print(user) # ? {'id': 1, 'username': '@miller'}
```

This method take the following as arguments

| Argument   | Description                                                                                | Type                             | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------ | -------------------------------- | ------- | -------- |
| `instance` | The model class to retrieve instances from.                                                | `Model`                          |         | `Yes`    |
| `filters`  | `Filter` or a collection of `Filter` to apply to the query.                                | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `select`   | Collection of `str` or `str` of which is the name of the columns or column to be selected. | `list[str]\|str`                 | `[]`    | `No`     |
| `include`  | Collection of `Include` or a single `Include` of related models to eagerly load.           | `list[Include]\|Include`         | `[]`    | `No`     |
| `offset`   | Number of instances to skip before retrieving.                                             | `int \| None`                    | `None`  | `No`     |

##### 4. `find_by_pk()`

Here is an example showing how you can use the `find_by_pk()` to locate a single record in the database.

```py
user = mysql_loom.find_by_pk(User, pk=userId, select=["id", "username"])
print(user) # ? {'id': 1, 'username': '@miller'}
```

The method takes the following as arguments:

| Argument   | Description                                                                        | Type                     | Default | Required |
| ---------- | ---------------------------------------------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve instances from.                                        | `Model`                  |         | `Yes`    |
| `pk`       | The primary key value to use for retrieval.                                        | `Any`                    |         | `Yes`    |
| `select`   | Collection column names to select from the instances.                              | `list[str]`              | `[]`    | `No`     |
| `include`  | A Collection of `Include` or a single `Include` of related models to eagerly load. | `list[Include]\|Include` | `[]`    | `No`     |

#### 3. Updating a record

To update records in your database table you make use of the following functions:

1. `update_by_pk()`
2. `update_one()`
3. `update_bulk()`

##### 1. `update_by_pk()`

The `update_pk()` method can be used as follows:

```py
affected_rows = mysql_loom.update_by_pk(
    instance=Post,
    pk=1,
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The above method takes in the following as arguments:

| Argument   | Description                                                                            | Type                               | Default | Required |
| ---------- | -------------------------------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update the instance.                                      | `Model`                            |         | `Yes`    |
| `pk`       | The primary key value of the instance to update.                                       | `Any`                              |         | `Yes`    |
| `values`   | Single or Collection of [`ColumnValue`](#columnvalue-class) to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

##### 2. `update_one()`

Here is an example illustrating how to use the `update_one()` method:

```py
affected_rows = mysql_loom.update_one(
    instance=Post,
    filters=[
        Filter(column="id", value=8, join_next_with="OR"),
        Filter(column="userId", value=1, join_next_with="OR"),
    ],
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The method takes the following as arguments:

| Argument   | Description                                                           | Type                               | Default | Required |
| ---------- | --------------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update the instance(s).                  | `Model`                            |         | `Yes`    |
| `filters`  | Filter or collection of filters to apply to the update query.         | `Filter \| list[Filter] \| None`   |         | `Yes`    |
| `values`   | Single or collection of column-value pairs to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

##### 3. `update_bulk()`

The `update_bulk()` method updates all records that match a filter in a database table.

```py
affected_rows = mysql_loom.update_bulk(
    instance=Post,
    filters=[
        Filter(column="id", value=8, join_next_with="OR"),
        Filter(column="userId", value=1, join_next_with="OR"),
    ],
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The above method takes in the following as argument:

| Argument   | Description                                                           | Type                               | Default | Required |
| ---------- | --------------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update instances.                        | `Model`                            |         | `Yes`    |
| `filters`  | Filter or collection of filters to apply to the update query.         | `Filter \| list[Filter] \| None`   |         | `Yes`    |
| `values`   | Single or collection of column-value pairs to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

#### 4. Deleting a record

To delete a record or records in a database table you make use of the following functions:

1. `delete_by_pk()`
2. `delete_one()`
3. `delete_bulk()`

##### 1. `delete_by_pk()`

Using the `delete_by_pk()` method, you can delete a record in a database based on the primary-key value.

```py
affected_rows = mysql_loom.delete_by_pk(instance=User, pk=1)
```

The above take the following as arguments:

| Argument   | Description                                        | Type    | Default | Required |
| ---------- | -------------------------------------------------- | ------- | ------- | -------- |
| `instance` | The model class from which to delete the instance. | `Model` |         | `Yes`    |
| `pk`       | The primary key value of the instance to delete.   | `Any`   |         | `Yes`    |

##### 2. `delete_one()`

You can also use `filters` to delete a record in a database. The `delete_one()` function enables you to delete a single record in a database that matches a filter.

```py
affected_rows = mysql_loom.delete_one(
    instance=User, filters=[Filter(column="username", value="@miller")]
)
```

The method takes in the following arguments:

| Argument   | Description                                                                           | Type                             | Default | Required |
| ---------- | ------------------------------------------------------------------------------------- | -------------------------------- | ------- | -------- |
| `instance` | The model class from which to delete the instance(s).                                 | `Model`                          |         | `Yes`    |
| `filters`  | Filter or collection of filters to apply to the deletion query.                       | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `offset`   | Number of instances to skip before deleting.                                          | `int \| None`                    | `None`  | `No`     |
| `order`    | Collection of `Order` or as single `Order` to order the instances by before deletion. | `list[Order] \| Order\| None`    | `[]`    | `No`     |

##### 3. `delete_bulk()`

You can also use the `delete_bulk()` method to delete a multitude of records that match a given filter:

```py
affected_rows = mysql_loom.delete_bulk(
    instance=User, filters=[Filter(column="username", value="@miller")]
)
```

The method takes the following as arguments:

| Argument   | Description                                                                          | Type                             | Default | Required |
| ---------- | ------------------------------------------------------------------------------------ | -------------------------------- | ------- | -------- |
| `instance` | The model class from which to delete instances.                                      | `Model`                          |         | `Yes`    |
| `filters`  | Filter or collection of filters to apply to the deletion query.                      | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `limit`    | Maximum number of instances to delete.                                               | `int \| None`                    | `None`  | `No`     |
| `offset`   | Number of instances to skip before deleting.                                         | `int \| None`                    | `None`  | `No`     |
| `order`    | Collection of `Order` or a single `Order` to order the instances by before deletion. | `list[Order] \|Order\| None`     | `[]`    | `No`     |

###### Warning: Potential Risk with `delete_bulk()`

> ⚠️ **Warning:** When using the `delete_bulk()` function, exercise caution as it can be aggressive. If the filter is not explicitly provided, there is a risk of mistakenly deleting all records in the table.

###### Guidelines for Safe Usage

To mitigate the potential risks associated with `delete_bulk()`, follow these guidelines:

1. **Always Provide a Filter:**

   - When calling `delete_bulk()`, make sure to provide a filter to specify the subset of records to be deleted. This helps prevent unintentional deletions.

   ```python
    # Example: Delete records where 'status' is 'inactive'
    affected_rows = mysql_loom.delete_bulk(
        instance=User,
        filters=Filter(column="status",  value='inactive'),
    )
   ```

2. **Consider Usage When Necessary:**

- When contemplating data deletion, it is advisable to consider more targeted methods before resorting to `delete_bulk()`. Prioritize the use of `delete_one()` or `delete_by_pk()` methods to remove specific records based on your needs. This ensures a more precise and controlled approach to data deletion.

3. **Use limit and offsets options**

- You can consider using the `limit` and offset options during invocation of `delete_bulk`

```py
affected_rows = mysql_loom.delete_bulk(
    instance=Post,
    order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
    filters=[Filter(column="id", operator="gt", value=0)],
    offset=0,
    limit=10,
)
```

By following these guidelines, you can use the `delete_bulk()` function safely and minimize the risk of unintended data loss. Always exercise caution and adhere to best practices when performing bulk deletion operations.

### Ordering

In dataloom you can order documents in either `DESC` (descending) or `ASC` (ascending) order using the helper class `Order`.

```py
posts = mysql_loom.find_all(
    instance=Post,
    order=[Order(column="id", order="DESC")],
)
```

You can apply multiple and these orders will ba applied in sequence of application here is an example:

```py
posts = mysql_loom.find_all(
    instance=Post,
    order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
)
```

### Filters

There are different find of filters that you can use when filtering documents for mutations and queries. Filters are very important to use when updating and deleting documents as they give you control on which documents should be updated or deleted. When doing a mutation you can use a single or multiple filters. Bellow is an example that shows you how you can use a single filter in deleting a single record that has an `id` greater than `1` from the database.

```py
res2 = mysql_loom.delete_one(
    instance=Post,
    offset=0,
    order=Order(column="id", order="DESC"),
    filters=Filter(column="id", value=1, operator="gt"),
)
```

Or you can use it as follows:

```py
res2 = mysql_loom.delete_one(
    instance=Post,
    offset=0,
    order=[Order(column="id", order="DESC")],
    filters=[Filter(column="id", value=1, operator="gt")],
)
```

As you have noticed, you can join your filters together and they will be applied sequentially using the [`join_next_with`](#filter-class) which can be either `OR` or `AND` te default value is `AND`. Here is an of filter usage in sequential.

```py
res2 = mysql_loom.delete_one(
    instance=Post,
    offset=0,
    order=[Order(column="id", order="DESC")],
    filters=[
        Filter(column="id", value=1, operator="gt"),
        Filter(column="userId", value=1, operator="eq", join_next_with="OR"),
        Filter(
            column="title",
            value='"What are you doing general?"',
            operator="=",
            join_next_with="AND",
        ),
    ],
)
```

##### Operators

You can use the `operator` to match the values. Here is the table of description for these filters.

| Operator    | Explanation                                                                                                  | Expect                |
| ----------- | ------------------------------------------------------------------------------------------------------------ | --------------------- |
| `'eq'`      | Indicates equality. It checks if the value is equal to the specified criteria.                               | Value == Criteria     |
| `'lt'`      | Denotes less than. It checks if the value is less than the specified criteria.                               | Value < Criteria      |
| `'gt'`      | Denotes greater than. It checks if the value is greater than the specified criteria.                         | Value > Criteria      |
| `'leq'`     | Denotes less than or equal to. It checks if the value is less than or equal to the specified criteria.       | Value <= Criteria     |
| `'geq'`     | Denotes greater than or equal to. It checks if the value is greater than or equal to the specified criteria. | Value >= Criteria     |
| `'in'`      | Checks if the value is included in a specified list of values.                                               | Value in List         |
| `'notIn'`   | Checks if the value is not included in a specified list of values.                                           | Value not in List     |
| `'like'`    | Performs a pattern matching operation. It checks if the value is similar to a specified pattern.             | Value matches Pattern |
| `'not'`     | Indicates non-equality. It checks if the column value that does not equal to the specified criteria.         | NOT id = Criteria     |
| `'neq'`     | Indicates non-equality. It checks if the value is not equal to the specified criteria.                       | Value != Criteria     |
| `'between'` | It checks range values that matches a given range between the minimum and maximum.                           | id BETWEEN (min, max) |

Let's talk about these filters in detail of code by example. Let's say you want to update a `Post` where the `id` matches `1` you can do it as follows:

```py
res2 = mysql_loom.update_one(
    instance=Post,
    filters=Filter(
        column="id",
        value=1,
        operator="eq",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

What if you want to update a post where `id` is not equal to `1` you can do it as follows

```py
res2 = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=1,
        operator="neq",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

What if i want to update the records that have an `id` less than `3`?

```py
res2 = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=3,
        operator="lt",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

What if i want to update the records that have an `id` less than or equal `3`?

```py
res2 = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=1,
        operator="neq",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

What if i want to update the records that have an `id` greater than `3`?

```py
res = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=3,
        operator="gt",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

What if i want to update the records that have an `id` greater or equal to `3`?

```py
res = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=3,
        operator="geq",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

You can use the `in` to update or query records that matches values in a specified `list` of values or `tuple`. Here is an example showing you how you can update records that does matches `id` in `[1, 2]`.

```py
res = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=[1, 2],
        operator="in",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

You can use the `notIn` to update or query records that does not matches values in a specified `list` of values or `tuple`. Here is an example showing you how you can update records that does not matches `id` in `[1, 2]`.

```py

res = mysql_loom.update_bulk(
    instance=Post,
    filters=Filter(
        column="id",
        value=[1, 2],
        operator="notIn",
    ),
    values=[ColumnValue(name="title", value="Bob")],
)
```

You can use the `like` operator to match some patens in your query filters. Let's say we want to match a post that has the title ends with `general` we can use the `like` operator as follows

```py
general = mysql_loom.find_one(
    instance=Post,
    filters=Filter(
        column="title",
        value="% general?",
        operator="like",
    ),
    select=["id", "title"],
)

print(general) # ?  {'id': 1, 'title': 'What are you doing general?'}
```

The following table show you some expression that you can use with this `like` operator.

| Value          | Description                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `%pattern`     | Finds values that end with the specified pattern.                                                                        |
| `pattern%`     | Finds values that start with the specified pattern.                                                                      |
| `%pattern%`    | Finds values that contain the specified pattern anywhere within the string.                                              |
| `_pattern`     | Finds values that have any single character followed by the specified pattern.                                           |
| `pattern_`     | Finds values that have the specified pattern followed by any single character.                                           |
| `[charlist]%`  | Finds values that start with any character in the specified character list.                                              |
| `[!charlist]%` | Finds values that start with any character not in the specified character list.                                          |
| `_pattern_`    | Finds values that have any single character followed by the specified pattern and then followed by any single character. |

### Data Aggregation

With the [`Having`](#having-class) and the [`Group`](#group-class) classes you can perform some powerful powerful queries. In this section we are going to demonstrate an example of how we can do the aggregate queries.

```py
posts = mysql_loom.find_many(
    Post,
    select="id",
    filters=Filter(column="id", operator="gt", value=1),
    group=Group(
        column="id",
        function="MAX",
        having=Having(column="id", operator="in", value=(2, 3, 4)),
        return_aggregation_column=True,
    ),
)
```

The following will be the output from the above query.

```shell
[{'id': 2, 'MAX(`id`)': 2}, {'id': 3, 'MAX(`id`)': 3}, {'id': 4, 'MAX(`id`)': 4}]
```

However you can remove the aggregation column from the above query by specifying the `return_aggregation_column` to be `False`:

```py
posts = mysql_loom.find_many(
    Post,
    select="id",
    filters=Filter(column="id", operator="gt", value=1),
    group=Group(
        column="id",
        function="MAX",
        having=Having(column="id", operator="in", value=(2, 3, 4)),
        return_aggregation_column=False,
    ),
)
print(posts)
```

This will output:

```shell
[{'id': 2}, {'id': 3}, {'id': 4}]
```

#### Aggregation Functions

You can use the following aggregation functions that dataloom supports:

| Aggregation Function | Description                                      |
| -------------------- | ------------------------------------------------ |
| `"AVG"`              | Computes the average of the values in the group. |
| `"COUNT"`            | Counts the number of items in the group.         |
| `"SUM"`              | Computes the sum of the values in the group.     |
| `"MAX"`              | Retrieves the maximum value in the group.        |
| `"MIN"`              | Retrieves the minimum value in the group.        |

> 👍 **Pro Tip**: Note that data aggregation only works without `eager` loading and also works only with [`find_may()`](#2-find_many) and [`find_all()`](#1-find_all) in dataloom.

### Utilities

Dataloom comes up with some utility functions that works on an instance of a model. This is very useful when debuging your tables to see how do they look like. These function include:

#### 1. `inspect()`

This function takes in a model as argument and inspect the model fields or columns. The following examples show how we can use this handy function in inspecting table names.

```py
table = mysql_loom.inspect(instance=User, fields=["name", "type"], print_table=False)
print(table)
```

The above snippet returns a list of dictionaries containing the column name and the arguments that were passed.

```shell
[{'id': {'type': 'int'}}, {'name': {'type': 'varchar'}}, {'tokenVersion': {'type': 'int'}}, {'username': {'type': 'varchar'}}]
```

You can print table format these fields with their types as follows

```py
mysql_loom.inspect(instance=User)
```

Output:

```shell
+--------------+---------+----------+---------+
| name         | type    | nullable | default |
+--------------+---------+----------+---------+
| id           | int     | NO       | None    |
| name         | varchar | NO       | Bob     |
| tokenVersion | int     | YES      | 0       |
| username     | varchar | YES      | None    |
+--------------+---------+----------+---------+
```

The `inspect` function take the following arguments.

| Argument      | Description                                            | Type        | Default                                   | Required |
| ------------- | ------------------------------------------------------ | ----------- | ----------------------------------------- | -------- |
| `instance`    | The model instance to inspect.                         | `Model`     | -                                         | Yes      |
| `fields`      | The list of fields to include in the inspection.       | `list[str]` | `["name", "type", "nullable", "default"]` | No       |
| `print_table` | Flag indicating whether to print the inspection table. | `bool`      | `True`                                    | No       |

#### 2. `decorators`

These modules contain several decorators that can prove useful when creating models. These decorators originate from `dataloom.decorators`, and at this stage, we are referring to them as "experimental."

##### `@initialize()`

Let's examine a model named `Profile`, which appears as follows:

```py
class Profile(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    avatar = Column(type="text", nullable=False)
    userId = ForeignKeyColumn(
        User,
        maps_to="1-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )
```

This is simply a Python class that inherits from the top-level class `Model`. However, it lacks some useful `dunder` methods such as `__init__` and `__repr__`. In standard Python, we can achieve this functionality by using `dataclasses`. For example, we can modify our class as follows:

```py
from dataclasses import dataclass

@dataclass
class Profile(Model):
    # ....

```

However, this approach doesn't function as expected in `dataloom` columns. Hence, we've devised these experimental decorators to handle the generation of essential dunder methods required for working with `dataloom`. If you prefer not to use decorators, you always have the option to manually create these dunder methods. Here's an example:

```py
class Profile(Model):
    # ...
    def __init__(self, id: int | None, avatar: str | None, userId: int | None) -> None:
        self.id = id
        self.avatar = avatar
        self.userId = userId

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:id={self.id}>"

    @property
    def to_dict(self):
        return {"id": self.id, "avatar": self.avatar, "userId": self.userId}
```

However, by using the `initialize` decorator, this functionality will be automatically generated for you. Here's all you need to do:

```py
from dataloom.decorators import initialize

@initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
class Profile(Model):
    # ...
```

> 👉 **Tip**: Dataloom has a clever way of skipping the `TableColumn` because it doesn't matter in this case.

The `initialize` decorator takes the following arguments:

| Argument          | Description                                                 | Type            | Default | Required |
| ----------------- | ----------------------------------------------------------- | --------------- | ------- | -------- |
| `to_dict`         | Flag indicating whether to generate a `to_dict` method.     | `bool`          | `False` | `No`     |
| `init`            | Flag indicating whether to generate an `__init__` method.   | `bool`          | `True`  | `No`     |
| `repr`            | Flag indicating whether to generate a `__repr__` method.    | `bool`          | `False` | `No`     |
| `repr_identifier` | Identifier for the attribute used in the `__repr__` method. | `str` or `None` | `None`  | `No`     |

> 👍**Pro Tip:** Note that this `decorator` function allows us to interact with our data from the database in an object-oriented way in Python. Below is an example illustrating this concept:

```py
profile = mysql_loom.find_by_pk(Profile, pk=1, select=["avatar", "id"])
profile = Profile(**profile)
print(profile)  # ? = <Profile:id=1>
print(profile.avatar)  # ? hello.jpg
```

#### 3. `count()`

This is a utility function that comes within the `loom` object that is used to count rows in a database table that meets a specific criteria. Here is an example on how to use this utility function.

```py
# example
count = mysql_loom.count(
    instance=Post,
    filters=Filter(
        column="id",
        operator="between",
        value=[1, 7],
    ),
    column="id",
    limit=3,
    offset=0,
    distinct=True,
)
print(count)
```

The `count` function takes the following arguments:

| Argument   | Description                                                                                | Type                     | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                | `Model`                  | `None`  | `Yes`    |
| `column`   | A string of column to count values based on.                                               | `str`                    | `None`  | `Yes`    |
| `limit`    | Maximum number of documents to retrieve.                                                   | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before counting.                                               | `int`                    | `0`     | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the rows to be counted.                   | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to count distinct rows of values based on selected column or not. | `bool`                   | `False` | `No`     |

#### 4. `min()`

This is a utility function that comes within the `loom` object that is used to find the minimum value in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

```py
# example
_min = mysql_loom.min(
    instance=Post,
    filters=Filter(
        column="id",
        operator="between",
        value=[1, 7],
    ),
    column="id",
    limit=3,
    offset=0,
    distinct=True,
)
print(_min)
```

The `min` function takes the following arguments:

| Argument   | Description                                                                                             | Type                     | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                             | `Model`                  | `None`  | `Yes`    |
| `column`   | A string of column to find minimum values based on.                                                     | `str`                    | `None`  | `Yes`    |
| `limit`    | Maximum number of documents to retrieve.                                                                | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before finding the minimum.                                                 | `int`                    | `0`     | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the rows to be used.                                   | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to find minimum value in distinct rows values based on selected column or not. | `bool`                   | `False` | `No`     |

#### 5. `max()`

This is a utility function that comes within the `loom` object that is used to find the maximum value in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

```py
# example
_max = mysql_loom.max(
    instance=Post,
    filters=Filter(
        column="id",
        operator="between",
        value=[1, 7],
    ),
    column="id",
    limit=3,
    offset=0,
    distinct=True,
)
print(_max)
```

The `max` function takes the following arguments:

| Argument   | Description                                                                                                | Type                     | Default | Required |
| ---------- | ---------------------------------------------------------------------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                                | `Model`                  | `None`  | `Yes`    |
| `column`   | A string of column to find maximum values based on.                                                        | `str`                    | `None`  | `Yes`    |
| `limit`    | Maximum number of documents to retrieve.                                                                   | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before finding the maximum.                                                    | `int`                    | `0`     | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the rows to be used.                                      | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to find maximum value in distinct rows of values based on selected column or not. | `bool`                   | `False` | `No`     |

#### 6. `avg()`

This is a utility function that comes within the `loom` object that is used to calculate the average value in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

```py
# example
_avg = mysql_loom.avg(
    instance=Post,
    filters=Filter(
        column="id",
        operator="between",
        value=[1, 7],
    ),
    column="id",
    limit=3,
    offset=0,
    distinct=True,
)
print(_avg)
```

The `max` function takes the following arguments:

| Argument   | Description                                                                                                         | Type                     | Default | Required |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                                         | `Model`                  | `None`  | `Yes`    |
| `column`   | A string of column to calculate average values based on.                                                            | `str`                    | `None`  | `Yes`    |
| `limit`    | Maximum number of documents to retrieve.                                                                            | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before finding the calculating the average.                                             | `int`                    | `0`     | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the rows to be used.                                               | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to calculate the average value in distinct rows of values based on selected column or not. | `bool`                   | `False` | `No`     |

#### 7. `sum()`

This is a utility function that comes within the `loom` object that is used to find the total sum in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

```py
# example
_sum = mysql_loom.sum(
    instance=Post,
    filters=Filter(
        column="id",
        operator="between",
        value=[1, 7],
    ),
    column="id",
    limit=3,
    offset=0,
    distinct=True,
)
print(_sum)
```

The `sum` function takes the following arguments:

| Argument   | Description                                                                                    | Type                     | Default | Required |
| ---------- | ---------------------------------------------------------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.                                                    | `Model`                  | `None`  | `Yes`    |
| `column`   | A string of column to sum values based on.                                                     | `str`                    | `None`  | `Yes`    |
| `limit`    | Maximum number of documents to retrieve.                                                       | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before summing.                                                    | `int`                    | `0`     | `No`     |
| `filters`  | Collection of `Filter` or a `Filter` to apply to the rows to be used.                          | `list[Filter] \| Filter` | `None`  | `No`     |
| `distinct` | Boolean telling dataloom to sum value in distinct rows values based on selected column or not. | `bool`                   | `False` | `No`     |

### Associations

In dataloom you can create association using the `foreign-keys` column during model creation. You just have to specify a single model to have a relationship with another model using the [`ForeignKeyColum`](#foreignkeycolumn-class). Just by doing that dataloom will be able to learn bidirectional relationship between your models. Let's have a look at the following examples:

#### 1. `1-1` Association

Let's consider an example where we want to map the relationship between a `User` and a `Profile`:

```py
class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)

class Profile(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    avatar = Column(type="text", nullable=False)
    userId = ForeignKeyColumn(
        User,
        maps_to="1-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )

```

The above code demonstrates how to establish a `one-to-one` relationship between a `User` and a `Profile` using the `dataloom`.

- `User` and `Profile` are two model classes inheriting from `Model`.
- Each model is associated with a corresponding table in the database, defined by the `__tablename__` attribute.
- Both models have a primary key column (`id`) defined using `PrimaryKeyColumn`.
- Additional columns (`name`, `username`, `tokenVersion` for `User` and `avatar`, `userId` for `Profile`) are defined using `Column`.
- The `userId` column in the `Profile` model establishes a foreign key relationship with the `id` column of the `User` model using `ForeignKeyColumn`. This relationship is specified to be a `one-to-one` relationship (`maps_to="1-1"`).
- Various constraints such as `nullable`, `unique`, `default`, and foreign key constraints (`onDelete`, `onUpdate`) are specified for the columns.

##### Inserting

In the following code example we are going to demonstrate how we can create a `user` with a `profile`, first we need to create a user first so that we get reference to the user of the profile that we will create.

```py
userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)

profileId = mysql_loom.insert_one(
    instance=Profile,
    values=[
        ColumnValue(name="userId", value=userId),
        ColumnValue(name="avatar", value="hello.jpg"),
    ],
)
```

This Python code snippet demonstrates how to insert data into the database using the `mysql_loom.insert_one` method, it also work on other methods like `insert_bulk`.

1. **Inserting a User Record**:

   - The `mysql_loom.insert_one` method is used to insert a new record into the `User` table.
   - The `instance=User` parameter specifies that the record being inserted belongs to the `User` model.
   - The `values=ColumnValue(name="username", value="@miller")` parameter specifies the values to be inserted into the `User` table, where the `username` column will be set to `"@miller"`.
   - The ID of the newly inserted record is obtained and assigned to the variable `userId`.

2. **Inserting a Profile Record**:
   - Again, the `mysql_loom.insert_one` method is called to insert a new record into the `Profile` table.
   - The `instance=Profile` parameter specifies that the record being inserted belongs to the `Profile` model.
   - The `values` parameter is a list containing two `ColumnValue` objects:
     - The first `ColumnValue` object specifies that the `userId` column of the `Profile` table will be set to the `userId` value obtained from the previous insertion.
     - The second `ColumnValue` object specifies that the `avatar` column of the `Profile` table will be set to `"hello.jpg"`.
   - The ID of the newly inserted record is obtained and assigned to the variable `profileId`.

##### Retrieving Records

The following example shows you how you can retrieve the data in a associations

```py
profile = mysql_loom.find_one(
    instance=Profile,
    select=["id", "avatar"],
    filters=Filter(column="userId", value=userId),
)
user = mysql_loom.find_by_pk(
    instance=User,
    pk=userId,
    select=["id", "username"],
)
user_with_profile = {**user, "profile": profile}
print(user_with_profile) # ? = {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}
```

This Python code snippet demonstrates how to query data from the database using the `mysql_loom.find_one` and `mysql_loom.find_by_pk` methods, and combine the results of these two records that have association.

1. **Querying a Profile Record**:

   - The `mysql_loom.find_one` method is used to retrieve a single record from the `Profile` table.
   - The `filters=Filter(column="userId", value=userId)` parameter filters the results to only include records where the `userId` column matches the `userId` value obtained from a previous insertion.

2. **Querying a User Record**:

   - The `mysql_loom.find_by_pk` method is used to retrieve a single record from the `User` table based on its primary key (`pk=userId`).
   - The `instance=User` parameter specifies that the record being retrieved belongs to the `User` model.
   - The `select=["id", "username"]` parameter specifies that only the `id` and `username` columns should be selected.
   - The retrieved user data is assigned to the variable `user`.

3. **Combining User and Profile Data**:
   - The user data (`user`) and profile data (`profile`) are combined into a single dictionary (`user_with_profile`) using dictionary unpacking (`{**user, "profile": profile}`).
   - This dictionary represents a user with their associated profile.

> 🏒 We have realized that we are performing three steps when querying records, which can be verbose. However, in dataloom, we have introduced `eager` data fetching for all methods that retrieve data from the database. The following example demonstrates how we can achieve the same result as before using eager loading:

```python
# With eager loading
user_with_profile = mysql_loom.find_by_pk(
    instance=User,
    pk=userId,
    select=["id", "username"],
    include=[Include(model=Profile, select=["id", "avatar"], has="one")],
)
print(user_with_profile) # ? = {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}
```

This Python code snippet demonstrates how to use eager loading with the `mysql_loom.find_by_pk` method to efficiently retrieve data from the `User` and `Profile` tables in a single query.

- Eager loading allows us to retrieve related data from multiple tables in a single database query, reducing the need for multiple queries and improving performance.
- In this example, the `include` parameter is used to specify eager loading for the `Profile` model associated with the `User` model.
- By including the `Profile` model with the `User` model in the `find_by_pk` method call, we instruct the database to retrieve both the user data (`id` and `username`) and the associated profile data (`id` and `avatar`) in a single query.
- This approach streamlines the data retrieval process and minimizes unnecessary database calls, leading to improved efficiency and performance in applications.

#### 2. `N-1` Association

Models can have `Many` to `One` relationship, it depends on how you define them. Let's have a look at the relationship between a `Category` and a `Post`. Many categories can belong to a single post.

```py
class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User,
        maps_to="1-N",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )

class Category(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="categories")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    type = Column(type="varchar", length=255, nullable=False)

    postId = ForeignKeyColumn(
        Post,
        maps_to="N-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )

```

In the provided code, we have two models: `Post` and `Category`. The relationship between these two models can be described as a `Many-to-One` relationship.

This means that many categories can belong to a single post. In other words:

- For each `Post` instance, there can be multiple `Category` instances associated with it.
- However, each `Category` instance can only be associated with one `Post`.

For example, consider a blogging platform where each `Post` represents an article and each `Category` represents a topic or theme. Each article (post) can be assigned to multiple topics (categories), such as "Technology", "Travel", "Food", etc. However, each topic (category) can only be associated with one specific article (post).

This relationship allows for a hierarchical organization of data, where posts can be categorized into different topics or themes represented by categories.

##### Inserting

Let's illustrate the following example where we insert categories into a post with the `id` 1.

```py
for title in ["Hey", "Hello", "What are you doing", "Coding"]:
    mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )

for cat in ["general", "education", "tech", "sport"]:
    mysql_loom.insert_one(
        instance=Category,
        values=[
            ColumnValue(name="postId", value=1),
            ColumnValue(name="type", value=cat),
        ],
    )
```

- **Inserting Posts**
  We're inserting new posts into the `Post` table. Each post is associated with a user (`userId`), and we're iterating over a list of titles to insert multiple posts.

- **Inserting Categories**
  We're inserting new categories into the `Category` table. Each category is associated with a specific post (`postId`), and we're inserting categories for a post with `id` 1.

> In summary, we're creating a relationship between posts and categories by inserting records into their respective tables. Each category record is linked to a specific post record through the `postId` attribute.

##### Retrieving Records

Let's attempt to retrieve a post with an ID of `1` along with its corresponding categories. We can achieve this as follows:

```py
post = mysql_loom.find_by_pk(Post, 1, select=["id", "title"])
categories = mysql_loom.find_many(
    Category,
    select=["type", "id"],
    filters=Filter(column="postId", value=1),
    order=[
        Order(column="id", order="DESC"),
    ],
)
post_with_categories = {**post, "categories": categories}
print(post_with_categories)  # ? = {'id': 1, 'title': 'Hey', 'categories': [{'type': 'sport', 'id': 4}, {'type': 'tech', 'id': 3}, {'type': 'education', 'id': 2}, {'type': 'general', 'id': 1}]}
```

- We use the `mysql_loom.find_by_pk()` method to retrieve a single post (`Post`) with an `id` equal to 1. We select only specific columns (`id` and `title`) for the post.
- We use the `mysql_loom.find_many()` method to retrieve multiple categories (`Category`) associated with the post. We select only specific columns (`type` and `id`) for the categories. We apply a filter to only fetch categories associated with the post with `postId` equal to 1. We sort the categories based on the `id` column in descending order.
- We create a dictionary (`post_with_categories`) that contains the retrieved post and its associated categories. The post information is stored under the key `post`, and the categories information is stored under the key `categories`.

> The above task can be accomplished using `eager` document retrieval as shown below.

```py
post_with_categories = mysql_loom.find_by_pk(
    Post,
    1,
    select=["id", "title"],
    include=[
        Include(
            model=Category,
            select=["type", "id"],
            order=[
                Order(column="id", order="DESC"),
            ],
        )
    ],
)

```

The code snippet queries a database to retrieve a post with an `id` of `1` along with its associated categories. Here's a breakdown:

1. **Querying for Post**:

   - The `mysql_loom.find_by_pk()` method fetches a single post from the database.
   - It specifies the `Post` model and ID `1`, retrieving only the `id` and `title` columns.

2. **Including Categories**:

   - The `include` parameter specifies additional related data to fetch.
   - Inside `include`, an `Include` instance is created for categories related to the post.
   - It specifies the `Category` model and selects only the `type` and `id` columns.
   - Categories are ordered by `id` in descending order.

3. **Result**:
   - The result is stored in `post_with_categories`, containing the post information and associated categories.

> In summary, this code is retrieving a specific post along with its categories from the database, and it's using `eager` loading to efficiently fetch related data in a single query.

#### 3. `1-N` Association

Let's consider a scenario where a `User` has multiple `Post`. here is how the relationships are mapped.

```py
class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)

class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User,
        maps_to="1-N",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE"
    )
```

So clearly we can see that when creating a `post` we need to have a `userId`

##### Inserting

Here is how we can insert a user and a post to the database tables.

```py
userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)
for title in ["Hey", "Hello", "What are you doing", "Coding"]:
    mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )
```

We're performing database operations to insert records for a user and multiple posts associated with that user.

- We insert a user record into the database using `mysql_loom.insert_one()` method.
- We iterate over a list of titles.
- For each title in the list, we insert a new post record into the database.
- Each post is associated with the user we inserted earlier, identified by the `userId`.
- The titles for the posts are set based on the titles in the list.

##### Retrieving Records

Now let's query the user with his respective posts. we can do it as follows:

```py
user = mysql_loom.find_by_pk(
    User,
    1,
    select=["id", "username"],
)
posts = mysql_loom.find_many(
    Post,
    filters=Filter(column="userId", value=userId, operator="eq"),
    select=["id", "title"],
    order=[Order(column="id", order="DESC")],
    limit=2,
    offset=1,
)

user_with_posts = {**user, "posts": posts}
print(
    user_with_posts
)  # ? = {'id': 1, 'username': '@miller', 'posts': [{'id': 3, 'title': 'What are you doing'}, {'id': 2, 'title': 'Hello'}]}
```

We're querying the database to retrieve information about a `user` and their associated `posts`.

1. **Querying User**:

   - We use `mysql_loom.find_by_pk()` to fetch a single user record from the database.
   - The user's ID is specified as `1`.
   - We select only the `id` and `username` columns for the user.

2. **Querying Posts**:

   - We use `mysql_loom.find_many()` to retrieve multiple post records associated with the user.
   - A filter is applied to only fetch posts where the `userId` matches the ID of the user retrieved earlier.
   - We select only the `id` and `title` columns for the posts.
   - The posts are ordered by the `id` column in descending order.
   - We set a limit of `2` posts to retrieve, and we skip the first post using an offset of `1`.
   - We create a dictionary `user_with_posts` containing the user information and a list of their associated posts under the key `"posts"`.

With eager loading this can be done as follows the above can be done as follows:

```py
user_with_posts = mysql_loom.find_by_pk(
    User,
    1,
    select=["id", "username"],
    include=[
        Include(
            model=Post,
            select=["id", "title"],
            order=[Order(column="id", order="DESC")],
            limit=2,
            offset=1,
        )
    ],
)
print(
    user_with_posts
)  # ? = {'id': 1, 'username': '@miller', 'posts': [{'id': 3, 'title': 'What are you doing'}, {'id': 2, 'title': 'Hello'}]}
```

- We use `mysql_loom.find_by_pk()` to fetch a single user record from the database.
- The user's ID is specified as `1`.
- We select only the `id` and `username` columns for the user.
- Additionally, we include associated post records using `eager` loading.
- Inside the `include` parameter, we specify the `Post` model and select only the `id` and `title` columns for the posts.
- The posts are ordered by the `id` column in descending order.
- We set a limit of `2` posts to retrieve, and we skip the first post using an offset of `1`.

#### 4. What about bidirectional queries?

In Dataloom, we support bidirectional relations with eager loading on-the-fly. You can query from a `parent` to a `child` and from a `child` to a `parent`. You just need to know how the relationship is mapped between these two models. In this case, the `has` option is very important in the `Include` class. Here are some examples demonstrating bidirectional querying between `user` and `post`, where the `user` is the parent table and the `post` is the child table in this case.

##### 1. Child to Parent

Here is an example illustrating how we can query a parent from child table.

```py
posts_users = mysql_loom.find_many(
    Post,
    limit=2,
    offset=3,
    order=[Order(column="id", order="DESC")],
    select=["id", "title"],
    include=[
        Include(
            model=User,
            select=["id", "username"],
            has="one",
            include=[Include(model=Profile, select=["id", "avatar"], has="one")],
        ),
        Include(
            model=Category,
            select=["id", "type"],
            order=[Order(column="id", order="DESC")],
            has="many",
            limit=2,
        ),
    ],
)
print(posts_users) # ? = [{'id': 1, 'title': 'Hey', 'user': {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}, 'categories': [{'id': 4, 'type': 'sport'}, {'id': 3, 'type': 'tech'}]}]
```

##### 2. Parent to Child

Here is an example of how we can query a child table from parent table

```py
user_post = mysql_loom.find_by_pk(
    User,
    pk=userId,
    select=["id", "username"],
    include=[
        Include(
            model=Post,
            limit=2,
            offset=3,
            order=[Order(column="id", order="DESC")],
            select=["id", "title"],
            include=[
                Include(
                    model=User,
                    select=["id", "username"],
                    has="one",
                    include=[
                        Include(model=Profile, select=["id", "avatar"], has="one")
                    ],
                ),
                Include(
                    model=Category,
                    select=["id", "type"],
                    order=[Order(column="id", order="DESC")],
                    has="many",
                    limit=2,
                ),
            ],
        ),
        Include(model=Profile, select=["id", "avatar"], has="one"),
    ],
)


print(user_post) """ ? =
{'id': 1, 'username': '@miller', 'user': {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}, 'categories': [{'id': 4, 'type': 'sport'}, {'id': 3, 'type': 'tech'}], 'posts': [{'id': 1, 'title': 'Hey', 'user': {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}, 'categories': [{'id': 4, 'type': 'sport'}, {'id': 3, 'type': 'tech'}]}], 'profile': {'id': 1, 'avatar': 'hello.jpg'}}
"""

```

#### 5. `Self` Association

Let's consider a scenario where we have a table `Employee`, where an employee can have a supervisor, which in this case a supervisor is also an employee. This is an example of self relations. The model definition for this can be done as follows in `dataloom`.

```py
class Employee(Model):
    __tablename__: TableColumn = TableColumn(name="employees")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    supervisorId = ForeignKeyColumn(
        "Employee", maps_to="1-1", type="int", required=False
    )
```

So clearly we can see that when creating a `employee` it is not a must to have a `supervisorId` as this relationship is optional.

> 👍 **Pro Tip:** Note that when doing self relations the referenced table must be a string that matches the table class name irrespective of case. In our case we used `"Employee"` and also `"employee"` and `"EMPLOYEe"` will be valid, however `"Employees"` and also `"employees"` and `"EMPLOYEEs"` are invalid.

##### Inserting

Here is how we can insert employees to this table and we will make `John` the supervisor of other employees.

```py
empId = mysql_loom.insert_one(
    instance=Employee, values=ColumnValue(name="name", value="John Doe")
)

rows = mysql_loom.insert_bulk(
    instance=Employee,
    values=[
        [
            ColumnValue(name="name", value="Michael Johnson"),
            ColumnValue(name="supervisorId", value=empId),
        ],
        [
            ColumnValue(name="name", value="Jane Smith"),
            ColumnValue(name="supervisorId", value=empId),
        ],
    ],
)

```

- Some employees is are associated with a supervisor `John` which are `Jane` and `Michael`.
- However the employee `John` does not have a supervisor.

##### Retrieving Records

Now let's query employee `Michael` with his supervisor.

```py
emp = mysql_loom.find_by_pk(
    instance=Employee, pk=2, select=["id", "name", "supervisorId"]
)
sup = mysql_loom.find_by_pk(
    instance=Employee, select=["id", "name"], pk=emp["supervisorId"]
)
emp_and_sup = {**emp, "supervisor": sup}
print(emp_and_sup) # ? = {'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'supervisor': {'id': 1, 'name': 'John Doe'}}
```

We're querying the database to retrieve information about a `employee` and their associated `supervisor`.

1. **Querying an Employee**:

   - We use `mysql_loom.find_by_pk()` to fetch a single employee record from the database.
   - The employee's ID is specified as `2`.

2. **Querying Supervisor**:

   - We use `mysql_loom.find_by_pk()` to retrieve a supervisor that is associated with this employee.
   - We create a dictionary `emp_and_sup` containing the `employee` information and their `supervisor`.

With eager loading this can be done in one query as follows the above can be done as follows:

```py
emp_and_sup = mysql_loom.find_by_pk(
    instance=Employee,
    pk=2,
    select=["id", "name", "supervisorId"],
    include=Include(
        model=Employee,
        has="one",
        select=["id", "name"],
        alias="supervisor",
    ),
)

print(emp_and_sup) # ? = {'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'supervisor': {'id': 1, 'name': 'John Doe'}}
```

- We use `mysql_loom.find_by_pk()` to fetch a single an employee record from the database.
- Additionally, we include associated `employee` record using `eager` loading with an `alias` of `supervisor`.

> 👍 **Pro Tip:** Note that the `alias` is very important in this situation because it allows you to get the included relationships with objects that are named well, if you don't give an alias dataloom will just use the model class name as the alias of your included models, in this case you will get an object that looks like `{'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'employee': {'id': 1, 'name': 'John Doe'}}`, which practically and theoretically doesn't make sense.

#### 6. `N-N` Relationship

Let's consider a scenario where we have tables for `Students` and `Courses`. In this scenario, a student can enroll in many courses, and a single course can have many students enrolled. This represents a `Many-to-Many` relationship. The model definitions for this scenario can be done as follows in `dataloom`:

**Table: Student**
| Column Name | Data Type |
|-------------|-----------|
| `id` | `INT` |
| `name`| `VARCHAR` |

**Table: Course**
| Column Name | Data Type |
|-------------|-----------|
| `id` | `INT` |
| `name` | `VARCHAR` |
| ... | ... |

**Table: Student_Courses** (junction table)
| Column Name | Data Type |
|-------------|-----------|
| `studentId` | `INT` |
| `courseId` | `INT` |

> 👍 **Pro Tip:** Note that the `junction` table can also be called `association`-table or `reference`-table or `joint`-table.

In `dataloom` we can model the above relations as follows:

```py
class Course(Model):
    __tablename__: TableColumn = TableColumn(name="courses")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")


class Student(Model):
    __tablename__: TableColumn = TableColumn(name="students")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")


class StudentCourses(Model):
    __tablename__: TableColumn = TableColumn(name="students_courses")
    studentId = ForeignKeyColumn(table=Student, type="int")
    courseId = ForeignKeyColumn(table=Course, type="int")

```

- The tables `students` and `courses` will not have foreign keys.
- The `students_courses` table will have two columns that joins these two tables together in an `N-N` relational mapping.

> 👍 **Pro Tip:** In a joint table no other columns such as `CreateAtColumn`, `UpdatedAtColumn`, `Column` and `PrimaryKeyColumn` are allowed and only exactly `2` foreign keys should be in this table.

##### Inserting

Here is how we can insert `students` and `courses` in their respective tables.

```py

# insert the courses
mathId = mysql_loom.insert_one(
    instance=Course, values=ColumnValue(name="name", value="Mathematics")
)
engId = mysql_loom.insert_one(
    instance=Course, values=ColumnValue(name="name", value="English")
)
phyId = mysql_loom.insert_one(
    instance=Course, values=ColumnValue(name="name", value="Physics")
)

# create students

stud1 = mysql_loom.insert_one(
    instance=Student, values=ColumnValue(name="name", value="Alice")
)
stud2 = mysql_loom.insert_one(
    instance=Student, values=ColumnValue(name="name", value="Bob")
)
stud3 = mysql_loom.insert_one(
    instance=Student, values=ColumnValue(name="name", value="Lisa")
)

```

- You will notice that we are keeping in track of the `studentIds` and the `courseIds` because we will need them in the `joint-table` or `association-table`.
- Now we can enrol students to their courses by inserting them in their id's in the association table.

```py
# enrolling students
mysql_loom.insert_bulk(
    instance=StudentCourses,
    values=[
        [
            ColumnValue(name="studentId", value=stud1),
            ColumnValue(name="courseId", value=mathId),
        ],  # enrolling Alice to mathematics
        [
            ColumnValue(name="studentId", value=stud1),
            ColumnValue(name="courseId", value=phyId),
        ],  # enrolling Alice to physics
        [
            ColumnValue(name="studentId", value=stud1),
            ColumnValue(name="courseId", value=engId),
        ],  # enrolling Alice to english
        [
            ColumnValue(name="studentId", value=stud2),
            ColumnValue(name="courseId", value=engId),
        ],  # enrolling Bob to english
        [
            ColumnValue(name="studentId", value=stud3),
            ColumnValue(name="courseId", value=phyId),
        ],  # enrolling Lisa to physics
        [
            ColumnValue(name="studentId", value=stud3),
            ColumnValue(name="courseId", value=engId),
        ],  # enrolling Lisa to english
    ],
)

```

##### Retrieving Records

Now let's query a student called `Alice` with her courses. We can do it as follows:

```py
s = mysql_loom.find_by_pk(
    Student,
    pk=stud1,
    select=["id", "name"],
)
c = mysql_loom.find_many(
    StudentCourses,
    filters=Filter(column="studentId", value=stud1),
    select=["courseId"],
)
courses = mysql_loom.find_many(
    Course,
    filters=Filter(column="id", operator="in", value=[list(i.values())[0] for i in c]),
    select=["id", "name"],
)

alice = {**s, "courses": courses}
print(courses) # ? = {'id': 1, 'name': 'Alice', 'courses': [{'id': 1, 'name': 'Mathematics'}, {'id': 2, 'name': 'English'}, {'id': 3, 'name': 'Physics'}]}
```

We're querying the database to retrieve information about a `student` and their associated `courses`. Here are the steps in achieving that:

1. **Querying Student**:

   - We use `mysql_loom.find_by_pk()` to fetch a single `student` record from the database in the table `students`.

2. **Querying Course Id's**:
   - Next we are going to query all the course ids of that student and store them in `c` in the joint table `students_courses`.
   - We use `mysql_loom.find_many()` to retrieve the course `ids` of `alice`.
3. **Querying Course**:
   - Next we will query all the courses using the operator `in` in the `courses` table based on the id's we obtained previously.

As you can see we are doing a lot of work to get the information about `Alice`. With eager loading this can be done in one query as follows the above can be done as follows:

```py
alice = mysql_loom.find_by_pk(
    Student,
    pk=stud1,
    select=["id", "name"],
    include=Include(
        model=Course, junction_table=StudentCourses, alias="courses", has="many"
    ),
)

print(alice) # ? = {'id': 1, 'name': 'Alice', 'courses': [{'id': 1, 'name': 'Mathematics'}, {'id': 2, 'name': 'English'}, {'id': 3, 'name': 'Physics'}]}
```

- We use `mysql_loom.find_by_pk()` to retrieve a single student record from the database.
- Furthermore, we include the associated `course` records using `eager` loading with an `alias` of `courses`.
- We specify a `junction_table` in our `Include` statement. This allows dataloom to recognize the relationship between the `students` and `courses` tables through this `junction_table`.

> 👍 **Pro Tip:** It is crucial to specify the `junction_table` when querying in a many-to-many (`N-N`) relationship. This is because, by default, the models will not establish a direct many-to-many relationship without referencing the `junction_table`. They lack foreign key columns within them to facilitate this relationship.

As for our last example let's query all the students that are enrolled in the `English` class. We can easily do it as follows:

```py
english = mysql_loom.find_by_pk(
    Course,
    pk=engId,
    select=["id", "name"],
    include=Include(model=Student, junction_table=StudentCourses, has="many"),
)

print(english) # ? = {'id': 2, 'name': 'English', 'students': [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Lisa'}]}
```

### Query Builder.

Dataloom exposes a method called `getQueryBuilder`, which allows you to obtain a `qb` object. This object enables you to execute SQL queries directly from SQL scripts.

```py
qb = loom.getQueryBuilder()

print(qb) # ? = Loom QB<mysql>
```

The `qb` object contains the method called `run`, which is used to execute SQL scripts or SQL queries.

```py
ids = qb.run("select id from posts;", fetchall=True)
print(ids) # ? = [(1,), (2,), (3,), (4,)]
```

You can also execute SQL files. In the following example, we will demonstrate how you can execute SQL scripts using the `qb`. Let's say we have an SQL file called `qb.sql` which contains the following SQL code:

```SQL
SELECT id, title FROM posts WHERE id IN (1, 3, 2, 4) LIMIT 4 OFFSET  1;
SELECT COUNT(*) FROM (
    SELECT DISTINCT `id`
    FROM `posts`
    WHERE `id` < 5
    LIMIT 3 OFFSET 2
) AS subquery;
```

We can use the query builder to execute the SQL as follows:

```py
with open("qb.sql", "r") as reader:
    sql = reader.read()
res = qb.run(
    sql,
    fetchall=True,
    is_script=True,
)
print(res)
```

> 👍 **Pro Tip:** Executing a script using query builder does not return a result. The result value is always `None`.

The `run` method takes the following as arguments:

| Argument        | Description                                                                            | Type                                           | Required | Default |
| --------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- | -------- | ------- |
| `sql`           | SQL query to execute.                                                                  | `str`                                          | Yes      |         |
| `args`          | Parameters for the SQL query.                                                          | `Any \| None`                                  | No       | `None`  |
| `fetchone`      | Whether to fetch only one result.                                                      | `bool`                                         | No       | `False` |
| `fetchmany`     | Whether to fetch multiple results.                                                     | `bool`                                         | No       | `False` |
| `fetchall`      | Whether to fetch all results.                                                          | `bool`                                         | No       | `False` |
| `mutation`      | Whether the query is a mutation (insert, update, delete).                              | `bool`                                         | No       | `True`  |
| `bulk`          | Whether the query is a bulk operation.                                                 | `bool`                                         | No       | `False` |
| `affected_rows` | Whether to return affected rows.                                                       | `bool`                                         | No       | `False` |
| `operation`     | Type of operation being performed.                                                     | `'insert', 'update', 'delete', 'read' \| None` | No       | `None`  |
| `verbose`       | Verbosity level for logging . Set this option to `0` if you don't want logging at all. | `int`                                          | No       | `1`     |
| `is_script`     | Whether the SQL is a script.                                                           | `bool`                                         | No       | `False` |

#### Why Use Query Builder?

- The query builder empowers developers to seamlessly execute `SQL` queries directly.
- While Dataloom primarily utilizes `subqueries` for eager data fetching on models, developers may prefer to employ JOIN operations, which are achievable through the `qb` object.

  ```python
  qb = loom.getQueryBuilder()
  result = qb.run("SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.table1_id;")
  print(result)
  ```

### Documentation

You can read the full documentation of dataloom on [readthedocs.io](https://dataloom-py.readthedocs.io/en/latest/)

### Contributing

Contributions to `dataloom` are welcome! Feel free to submit bug reports, feature requests, or pull requests on [GitHub](https://github.com/CrispenGari/dataloom).

### License

This project is licensed under the MIT License - see the [LICENSE](/LISENSE) file for details.
