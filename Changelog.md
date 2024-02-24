===
Dataloom **`2.1.0`**
===

### Release Notes - `dataloom`

We have release the new `dataloom` Version `2.1.0` (`2024-02-24`)

##### Features

- Connecting to databases using connection `uri` for all the supported dialects

  ```py
  # postgress
  pg_loom = Loom(
    dialect="postgres",
    connection_uri = "postgressql://root:root@localhost:5432/hi",
   # ...
  )
  # mysql
  mysql_loom = Loom(
    dialect="mysql",
    connection_uri = "mysql://root:root@localhost:3306/hi",
   # ...
  )

  # sqlite
  sqlite_loom = Loom(
    dialect="sqlite",
   connection_uri = "sqlite:///hi.db",
   # ...
  )
  ```

- updated documentation.
- enable table alterations as an option of `sync` and `connect_and_sync` function.
  ```py
  conn, tables = pg_loom.connect_and_sync([Profile, User], alter=True)
  ```
  > 🥇 **We recommend you to use `drop` or `force` if you are going to change or modify `foreign` and `primary` keys. This is because setting the option `alter` doe not have an effect on `primary` key columns.**

===

# Dataloom **`2.0.0`**

### Release Notes - `dataloom`

We have release the new `dataloom` Version `2.0.0` (`2024-02-21`)

##### Features

- Renaming the class `Dataloom` to `Loom`.
  ```py
  from dataloom import Loom
  ```
- Eager data fetching in relationships

  - Now you can fetch your child relationship together in your query

  ```py
  user = mysql_loom.find_one(
    instance=User,
    filters=[Filter(column="id", value=userId)],
    include=[Include(model=Profile, select=["id", "avatar"], has="one")],
  )
  print(user)
  ```

  - You can apply limits, offsets, filters and orders to your child associations during queries

  ```py
    post = mysql_loom.find_one(
      instance=Post,
      filters=[Filter(column="userId", value=userId)],
      select=["title", "id"],
      include=[
          Include(
              model=User,
              select=["id", "username"],
              has="one",
              include=[Include(model=Profile, select=["avatar", "id"], has="one")],
          ),
          Include(
              model=Category,
              select=["id", "type"],
              has="many",
              order=[Order(column="id", order="DESC")],
              limit=2,
          ),
      ],
    )
  ```

- Now `return_dict` has bee removed as an option in `dataloom` in the query functions like `find_by_pk`, `find_one`, `find_many` and `find_all` now works starting from this version. If you enjoy working with python objects you have to maneuver them manually using experimental features.

  ```py
  from dataloom.decorators import initialize

  @initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
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

  # now you can do this

  profile = mysql_loom.find_many(
      instance=Profile,
  )
  print([Profile(**p) for p in profile]) # ? = [<Profile:id=1>]
  print([Profile(**p) for p in profile][0].id) # ? = 1
  ```

  - These are `experimental` decorators they are little bit slow and they work perfect in a single instance, you can not nest relationships on them.
  - You can use them if you know how your data is structured and also if you know how to manipulate dictionaries

- Deprecated ~~`join_next_filter_with`~~ to the use of `join_next_with`
- Values that was required as `list` e.g, `select`, `include` etc can now be passed as a single value.

  - **Before**

  ```py
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select={"id", "avatar"}) # invalid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select=("id", "avatar")) # invalid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select="id") # invalid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select=["id"]) # valid

  ```

  - **Now**

  ```py
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select={"id", "avatar"}) # valid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select=("id", "avatar")) # valid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select="id") # valid
  res = mysql_loom.find_by_pk(Profile, pk=profileId, select=["id"]) # valid

  ```

- Updated the documentation.
- Grouping data in queries will also be part of this release, using the class `Group` and `Having`.

```py
posts = pg_loom.find_many(
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

=====
Dataloom **`1.0.2`**
=====

We have release the new `dataloom` Version `1.0.2` (`2024-02-12`)

### Changes

We have updated the documentation so that it can look more colorful.

=====
Dataloom **`1.0.1`**
=====
Change logs for the `dataloom` Version `1.0.1` (`2024-02-12`)

### New Features

- **Docstring**: Now the functions and classes have a beautiful docstring that helps ypu with some examples and references in the editor.
- **SQL Loggers**: The SQL Loggers can now log `timestamps` not the log index especially for the `console` logger.

=====
Dataloom **`1.0.0`**
=====

### Release Notes - `dataloom`

We are pleased to release `dataloom` ORM for python version `3.12` and above. The dataloom version `1.0.0 ` released on (`2024-02-11`) is bug-free and ready to be used with the following features.

##### Features

- Initial release of `dataloom`.
- Lightweight and versatile Object-Relational Mapping (ORM) functionality.
- Support for `PostgreSQL`, `MySQL`, and `SQLite3` databases.
- Simplified database interactions for developers.

### What you can do

- Create records
- Delete records
- Update records
- Read records
- Inspect Models
- SQL logging
- Association Mapping
- Order Records
- Filter Records
- Select field in records
- etc.
