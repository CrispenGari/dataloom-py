Group Class
+++++++++++

This class is used for data ``aggregation`` and grouping data in ``dataloom``. Below is a table detailing the parameters available for the ``Group`` class


The following code cell demonstrates how we can do data aggregation using the ``Group`` class.

.. code-block:: 

    posts = mysql_loom.find_many(
        Post,
        select="id",
        filters=Filter(column="id", operator="gt", value=1),
        group=Group(
            column="id",
            function="MAX",
            return_aggregation_column=True,
        ),
    )

.. rst-class:: my-table

+---------------------------------------------------------+---------------------------------------+---------+---------+----------+
| Argument                                                | Description                           | Type    | Default | Required |
+---------------------------------------------------------+---------------------------------------+---------+---------+----------+
| column                                                  | The name of the column to group by.   | str     |         | Yes      |
+---------------------------------------------------------+---------------------------------------+---------+---------+----------+
| function                                                | "MAX"                                 | "COUNT" | No      |          |
+---------------------------------------------------------+---------------------------------------+---------+---------+----------+
| having                                                  | Filters to apply to the grouped data. | None    | None    | No       |
+---------------------------------------------------------+---------------------------------------+---------+---------+----------+
| Whether to return the aggregation column in the result. | bool                                  | False   | No      |          |
+---------------------------------------------------------+---------------------------------------+---------+---------+----------+

.. note:: You can include a single or multiple groups when doing data aggregation in ``dataloom``. You can filter the data while grouping using the `Having <having.html>`_ class.
