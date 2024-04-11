
Data Aggregation
++++++++++++++++

With the ``Having`` and the ``Group`` classes you can perform some powerful powerful queries. In this section we are going to demonstrate an example of how we can do the aggregate queries.

.. code-block:: 

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


The following will be the output from the above query.

.. code-block:: shell

    [{'id': 2, 'MAX(`id`)': 2}, {'id': 3, 'MAX(`id`)': 3}, {'id': 4, 'MAX(`id`)': 4}]


However you can remove the aggregation column from the above query by specifying the ``return_aggregation_column`` to be ``False``:

.. code-block:: 

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


This will output:

.. code-block:: shell

    [{'id': 2}, {'id': 3}, {'id': 4}]


Aggregation Functions
=====================

You can use the following aggregation functions that ``dataloom`` supports:

.. rst-class:: my-table

+-------------+--------------------------------------------------+
| Description |                                                  |
+=============+==================================================+
| ``"AVG"``   | Computes the average of the values in the group. |
+-------------+--------------------------------------------------+
| ``"COUNT"`` | Counts the number of items in the group.         |
+-------------+--------------------------------------------------+
| ``"SUM"``   | Computes the sum of the values in the group.     |
+-------------+--------------------------------------------------+
| ``"MAX"``   | Retrieves the maximum value in the group.        |
+-------------+--------------------------------------------------+
| ``"MIN"``   | Retrieves the minimum value in the group.        |
+-------------+--------------------------------------------------+

.. tip:: 👍 **Pro Tip**: Note that data aggregation only works without ``eager`` loading and also works only with ``find_may()`` and ``find_all()`` in ``dataloom``.