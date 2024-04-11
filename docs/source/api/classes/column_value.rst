ColumnValue Class
+++++++++++++++++

Just like the ``Filter`` class, ``dataloom`` also provides a ``ColumnValue`` class. This class acts as a setter to update the values of columns in your database table.

The following code snippet demonstrates how the ``ColumnValue`` class is used to update records in the database.

.. code-block:: 

    re = pg_loom.update_one(
        Post,
        values=[
            ColumnValue(name="title", value="Hey"),
            ColumnValue(name="completed", value=True),
        ],
        filters=[
            Filter(column="id",  value=1, join_next_with="AND"),
            Filter(column="userId", value=1, join_next_with="AND"),
        ],
    )


It accepts two arguments: ``name`` and ``value``. name represents the column name, while value corresponds to the new value to be assigned to that column.

.. rst-class:: my-table

+-----------+------------------------------------------------------------+---------+---------+
| Argument  | Description                                                | Type    | Default |
+-----------+------------------------------------------------------------+---------+---------+
| ``name``  | The name of the column to be updated or inserted.          | ``str`` | --      |
+-----------+------------------------------------------------------------+---------+---------+
| ``value`` | The value to assign to the column during update or insert. | ``Any`` | --      |
+-----------+------------------------------------------------------------+---------+---------+

.. note:: The ``ColumnValue`` is used during data insertion and update.
