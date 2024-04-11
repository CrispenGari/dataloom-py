4. What about ``bidirectional`` queries?
++++++++++++++++++++++++++++++++++++++++

In ``Dataloom``, we support bidirectional relations with eager loading on-the-fly. You can query from a ``parent`` to a ``child`` and from a ``child`` to a ``parent``. You just need to know how the relationship is mapped between these two models. In this case, the `has` option is very important in the `Include` class. Here are some examples demonstrating bidirectional querying between `user` and `post`, where the `user` is the parent table and the `post` is the child table in this case.

1. Child to Parent
==================

Here is an example illustrating how we can query a parent from child table.

.. code-block:: 

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


2. Parent to Child
==================

Here is an example of how we can query a child table from parent table

.. code-block:: 

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


