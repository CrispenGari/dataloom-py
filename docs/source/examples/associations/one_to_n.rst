2. ``One to Many`` Association
++++++++++++++++++++++++++++++

Let's consider a scenario where a ``User`` has multiple ``Post``. here is how the relationships are mapped.

.. code-block:: 

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


So clearly we can see that when creating a ``post`` we need to have a ``userId``

Inserting Records
=================

Here is how we can insert a user and a post to the database tables.

.. code-block:: 

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


We're performing database operations to insert records for a user and multiple posts associated with that user.

- We insert a user record into the database using ``mysql_loom.insert_one()`` method.
- We iterate over a list of titles.
- For each title in the list, we insert a new post record into the database.
- Each post is associated with the user we inserted earlier, identified by the ``userId``.
- The titles for the posts are set based on the titles in the list.

Retrieving Records
==================

Now let's query the user with his respective posts. we can do it as follows:

.. code-block:: 

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


We're querying the database to retrieve information about a ``user`` and their associated ``posts``.

1. **Querying User**:

   - We use ``mysql_loom.find_by_pk()`` to fetch a single user record from the database.
   - The user's ID is specified as ``1``.
   - We select only the ``id`` and ``username`` columns for the user.

2. **Querying Posts**:

   - We use ``mysql_loom.find_many()`` to retrieve multiple post records associated with the user.
   - A filter is applied to only fetch posts where the ``userId`` matches the ID of the user retrieved earlier.
   - We select only the ``id`` and ``title`` columns for the posts.
   - The posts are ordered by the ``id`` column in descending order.
   - We set a limit of ``2`` posts to retrieve, and we skip the first post using an offset of ``1``.
   - We create a dictionary ``user_with_posts`` containing the user information and a list of their associated posts under the key ``"posts"``.

With eager loading this can be done as follows the above can be done as follows:

.. code-block:: 

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


- We use ``mysql_loom.find_by_pk()`` to fetch a single user record from the database.
- The user's ID is specified as ``1``.
- We select only the ``id`` and ``username`` columns for the user.
- Additionally, we include associated post records using ``eager`` loading.
- Inside the ``include`` parameter, we specify the ``Post`` model and select only the ``id`` and ``title`` columns for the posts.
- The posts are ordered by the ``id`` column in descending order.
- We set a limit of ``2`` posts to retrieve, and we skip the first post using an offset of ``1``.