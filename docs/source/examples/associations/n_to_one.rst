3. ``Many to One`` Association
++++++++++++++++++++++++++++++

Models can have ``Many`` to ``One`` relationship, it depends on how you define them. Let's have a look at the relationship between a ``Category`` and a ``Post``. Many categories can belong to a single post.

.. code-block:: 

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



In the provided code, we have two models: ``Post`` and ``Category``. The relationship between these two models can be described as a ``Many-to-One`` relationship.

This means that many categories can belong to a single post. In other words:

- For each ``Post`` instance, there can be multiple ``Category`` instances associated with it.
- However, each ``Category`` instance can only be associated with one ``Post``.

For example, consider a blogging platform where each ``Post`` represents an article and each ``Category`` represents a topic or theme. Each article (post) can be assigned to multiple topics (categories), such as "Technology", "Travel", "Food", etc. However, each topic (category) can only be associated with one specific article (post).

This relationship allows for a hierarchical organization of data, where posts can be categorized into different topics or themes represented by categories.

Inserting Records
=================

Let's illustrate the following example where we insert categories into a post with the ``id`` 1.

.. code-block:: 

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


- **Inserting Posts**
  We're inserting new posts into the ``Post`` table. Each post is associated with a user (``userId``), and we're iterating over a list of titles to insert multiple posts.

- **Inserting Categories**
  We're inserting new categories into the ``Category`` table. Each category is associated with a specific post (``postId``), and we're inserting categories for a post with ``id`` 1.

.. tip::  In summary, we're creating a relationship between posts and categories by inserting records into their respective tables. Each category record is linked to a specific post record through the ``postId`` attribute.

Retrieving Records
==================

Let's attempt to retrieve a post with an ID of ``1`` along with its corresponding categories. We can achieve this as follows:

.. code-block:: 

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


- We use the ``mysql_loom.find_by_pk()`` method to retrieve a single post (``Post``) with an ``id`` equal to 1. We select only specific columns (``id`` and ``title``) for the post.
- We use the ``mysql_loom.find_many()`` method to retrieve multiple categories (``Category``) associated with the post. We select only specific columns (``type`` and ``id``) for the categories. We apply a filter to only fetch categories associated with the post with ``postId`` equal to 1. We sort the categories based on the ``id`` column in descending order.
- We create a dictionary (``post_with_categories``) that contains the retrieved post and its associated categories. The post information is stored under the key ``post``, and the categories information is stored under the key ``categories``.

.. note:: The above task can be accomplished using ``eager`` document retrieval as shown below.

.. code-block:: 

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



The code snippet queries a database to retrieve a post with an ``id`` of ``1`` along with its associated categories. Here's a breakdown:

1. **Querying for Post**:

   - The ``mysql_loom.find_by_pk()`` method fetches a single post from the database.
   - It specifies the ``Post`` model and ID ``1``, retrieving only the ``id`` and ``title`` columns.

2. **Including Categories**:

   - The ``include`` parameter specifies additional related data to fetch.
   - Inside ``include``, an ``Include`` instance is created for categories related to the post.
   - It specifies the ``Category`` model and selects only the ``type`` and ``id`` columns.
   - Categories are ordered by ``id`` in descending order.

3. **Result**:
   - The result is stored in ``post_with_categories``, containing the post information and associated categories.

.. tip:: In summary, this code is retrieving a specific post along with its categories from the database, and it's using ``eager`` loading to efficiently fetch related data in a single query.