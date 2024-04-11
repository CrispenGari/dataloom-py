1. ``One to One`` Association
+++++++++++++++++++++++++++++

Let's consider an example where we want to map the relationship between a ``User`` and a ``Profile``:

.. code-block:: 

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



The above code demonstrates how to establish a ``one-to-one`` relationship between a ``User`` and a ``Profile`` using the ``dataloom``.

- ``User`` and ``Profile`` are two model classes inheriting from ``Model``.
- Each model is associated with a corresponding table in the database, defined by the ``__tablename__`` attribute.
- Both models have a primary key column (``id``) defined using ``PrimaryKeyColumn``.
- Additional columns (``name``, ``username``, ``tokenVersion`` for ``User`` and ``avatar``, ``userId`` for ``Profile``) are defined using ``Column``.
- The ``userId`` column in the ``Profile`` model establishes a foreign key relationship with the ``id`` column of the ``User`` model using ``ForeignKeyColumn``. This relationship is specified to be a ``one-to-one`` relationship (``maps_to="1-1"``).
- Various constraints such as ``nullable``, ``unique``, ``default``, and foreign key constraints (``onDelete``, ``onUpdate``) are specified for the columns.

Inserting Records
=================

In the following code example we are going to demonstrate how we can create a ``user`` with a ``profile``, first we need to create a user first so that we get reference to the user of the profile that we will create.

.. code-block:: 

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


This Python code snippet demonstrates how to insert data into the database using the ``mysql_loom.insert_one`` method, it also work on other methods like ``insert_bulk``.

1. **Inserting a User Record**:

   - The ``mysql_loom.insert_one`` method is used to insert a new record into the ``User`` table.
   - The ``instance=User`` parameter specifies that the record being inserted belongs to the ``User`` model.
   - The ``values=ColumnValue(name="username", value="@miller")`` parameter specifies the values to be inserted into the ``User`` table, where the ``username`` column will be set to ``"@miller"``.
   - The ID of the newly inserted record is obtained and assigned to the variable ``userId``.

2. **Inserting a Profile Record**:
   
   - Again, the ``mysql_loom.insert_one`` method is called to insert a new record into the ``Profile`` table.
   - The ``instance=Profile`` parameter specifies that the record being inserted belongs to the ``Profile`` model.
   - The ``values`` parameter is a list containing two ``ColumnValue`` objects:
     - The first ``ColumnValue`` object specifies that the ``userId`` column of the ``Profile`` table will be set to the ``userId`` value obtained from the previous insertion.
     - The second ``ColumnValue`` object specifies that the ``avatar`` column of the ``Profile`` table will be set to ``"hello.jpg"``.
   - The ID of the newly inserted record is obtained and assigned to the variable ``profileId``.

Retrieving Records
==================

The following example shows you how you can retrieve the data in a associations

.. code-block:: 

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


This Python code snippet demonstrates how to query data from the database using the ``mysql_loom.find_one`` and ``mysql_loom.find_by_pk`` methods, and combine the results of these two records that have association.

1. **Querying a Profile Record**:

   - The ``mysql_loom.find_one`` method is used to retrieve a single record from the ``Profile`` table.
   - The ``filters=Filter(column="userId", value=userId)`` parameter filters the results to only include records where the ``userId`` column matches the ``userId`` value obtained from a previous insertion.

2. **Querying a User Record**:

   - The ``mysql_loom.find_by_pk`` method is used to retrieve a single record from the ``User`` table based on its primary key (``pk=userId``).
   - The ``instance=User`` parameter specifies that the record being retrieved belongs to the ``User`` model.
   - The ``select=["id", "username"]`` parameter specifies that only the ``id`` and ``username`` columns should be selected.
   - The retrieved user data is assigned to the variable ``user``.

3. **Combining User and Profile Data**:
   
   - The user data (``user``) and profile data (``profile``) are combined into a single dictionary (``user_with_profile``) using dictionary unpacking (``{**user, "profile": profile}``).
   - This dictionary represents a user with their associated profile.

.. tip:: 🏒 We have realized that we are performing three steps when querying records, which can be verbose. However, in dataloom, we have introduced ``eager`` data fetching for all methods that retrieve data from the database. The following example demonstrates how we can achieve the same result as before using eager loading:

.. code-block:: 

    # With eager loading
    user_with_profile = mysql_loom.find_by_pk(
        instance=User,
        pk=userId,
        select=["id", "username"],
        include=[Include(model=Profile, select=["id", "avatar"], has="one")],
    )
    print(user_with_profile) # ? = {'id': 1, 'username': '@miller', 'profile': {'id': 1, 'avatar': 'hello.jpg'}}


This Python code snippet demonstrates how to use eager loading with the ``mysql_loom.find_by_pk`` method to efficiently retrieve data from the ``User`` and ``Profile`` tables in a single query.

- Eager loading allows us to retrieve related data from multiple tables in a single database query, reducing the need for multiple queries and improving performance.
- In this example, the ``include`` parameter is used to specify eager loading for the ``Profile`` model associated with the ``User`` model.
- By including the ``Profile`` model with the ``User`` model in the ``find_by_pk`` method call, we instruct the database to retrieve both the user data (``id`` and ``username``) and the associated profile data (`id` and `avatar`) in a single query.
- This approach streamlines the data retrieval process and minimizes unnecessary database calls, leading to improved efficiency and performance in applications.