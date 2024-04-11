Order Class
+++++++++++

The ``Order`` class enables us to specify the desired order in which documents should be returned. Below is an example illustrating its usage

.. code-block:: 

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


.. note:: Note when utilizing a list of orders, they are applied sequentially, one after the other.

.. rst-class:: my-table

+-------------+---------------------------------------------------------+-----------------+
| Description | Type                                                    | Default         |
+=============+=========================================================+=================+
| column      | The name of the column to order by.                     | str             |
+-------------+---------------------------------------------------------+-----------------+
| order       | The order direction, either "ASC" (ascending) or "DESC" | "ASC" or "DESC" |
+-------------+---------------------------------------------------------+-----------------+

