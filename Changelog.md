===
Dataloom **`1.1.0`**
===

### Update Notes - `dataloom`

We have release the new `dataloom` Version `1.1.0` (`2024-02-12`)

##### Features

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

- `N-N` relational mapping
- Now you can return python objects when querying data meaning that the option `return_dict` in the query functions like `find_by_pk`, `find_one`, `find_many` and `find_all` now works starting from this version
- Updated the documentation.
- Grouping data in queries will also be part of this release, using the class `Group`

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
