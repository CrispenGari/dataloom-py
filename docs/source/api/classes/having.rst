Having Class
++++++++++++

This class method is used to specify the filters to be applied on ``Grouped`` data during ``aggregation`` in ``dataloom``. Below is a table detailing the parameters available for the ``Group`` class:



The following code cell demonstrates how we can filter in data aggregation using the ``Having`` class.

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

.. rst-class:: my-table

+----------------+-----------------------------------------------+-------+---------+----------+
| Argument       | Description                                   | Type  | Default | Required |
+----------------+-----------------------------------------------+-------+---------+----------+
| column         | The name of the column to filter on.          | str   |         | Yes      |
+----------------+-----------------------------------------------+-------+---------+----------+
| operator       | The operator to use for the filter.           | "eq"  | No      |          |
+----------------+-----------------------------------------------+-------+---------+----------+
| value          | The value to compare against.                 | Any   |         | Yes      |
+----------------+-----------------------------------------------+-------+---------+----------+
| join_next_with | The SQL operand to join the next filter with. | "AND" | No      |          |
+----------------+-----------------------------------------------+-------+---------+----------+

.. note:: You can filter the groups in data aggregation using a single ``Having`` or multiple as a list.

    **See also**
    - `Group Class <group.html>`_
