
Filter Class
++++++++++++

This ``Filter`` class in ``dataloom`` is designed to facilitate the application of filters when executing queries and mutations.
It allows users to specify conditions that must be met for the operation to affect certain rows in a database table.
Below is an example demonstrating how this class can be used


.. code-block:: 

    affected_rows = pg_loom.update_one(
        Post,
        values=[
            ColumnValue(name="title", value="Hey"),
            ColumnValue(name="completed", value=True),
        ],
        filters=[
            Filter(column="id", value=1, join_next_with="AND"),
            Filter(column="userId", value=1, join_next_with="AND"),
        ],
    )


So from the above example we are applying filters while updating a ``Post`` here are the options that you can pass on that filter class:

.. rst-class:: my-table

+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+
| Argument           | Description                                                | Type                                                                                                                       | Default   |
+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+
| ``column``         | The name of the column to apply the filter on              | ``str``                                                                                                                    |           |
+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+
| ``value``          | The value to filter against                                | ``Any``                                                                                                                    |           |
+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+
| ``operator``       | The comparison operator to use for the filter              | ``'eq'``, ``'neq'``, ``'lt'``, ``'gt'``, ``'leq'``, ``'geq'``, ``'in'``, ``'notIn'``, ``'like'``, ``'between'``, ``'not'`` | ``'eq'``  |
+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+
| ``join_next_with`` | The logical operator to join this filter with the next one | ``'AND'``, ``'OR'``                                                                                                        | ``'AND'`` |
+--------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------+


.. tip:: Note You can apply either a list of filters or a single filter when filtering records.