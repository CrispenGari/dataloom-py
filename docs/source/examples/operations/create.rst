1. Creating a Record.
+++++++++++++++++++++

To insert a single or multiple records in a database you make use of the following functions:

#. ``insert_one()``
#. ``insert_bulk()``

1. ``insert_one()``
===================

The ``insert_one`` method allows you to save a single row in a specific table. Upon saving, it will return the primary key (``pk``) value of the inserted document. The following example shows how the ``insert_one()`` method works.

.. code-block:: 

    # Example: Creating a user record
    userId = pg_loom.insert_one(
        instance=User, values=ColumnValue(name="username", value="@miller")
    )

    userId = pg_loom.insert_one(
        instance=User,
        values=[
            ColumnValue(name="username", value="@miller"),
            ColumnValue(name="name", value="Jonh"),
        ],
    )


This function takes in two arguments which are ``instance`` and ``values``. Where values are the column values that you are inserting in a user table or a single column value.


.. rst-class:: my-table

+--------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------+----------+----------+
| Argument     | Description                                                                                                  | Type                                     | Required | Default  |
+==============+==============================================================================================================+==========================================+==========+==========+
| ``instance`` | The instance of the table where the row will be inserted.                                                    | ``Model``                                | ``Yes``  | ``None`` |
+--------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------+----------+----------+
| ``values``   | The column values to be inserted into the table. It can be a single column value or a list of column values. | list[``ColumnValue``] or ``ColumnValue`` | ``Yes``  | ``None`` |
+--------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------+----------+----------+

2. ``insert_bulk()``.
=====================

The ``insert_bulk`` method facilitates the bulk insertion of records, as its name suggests. The following example illustrates how you can add ``3`` posts to the database table simultaneously.

.. code-block:: 

    # Example: Inserting multiple posts
    rows = pg_loom.insert_bulk(
        User,
        values=[
            [
                ColumnValue(name="username", value="@miller"),
                ColumnValue(name="name", value="Jonh"),
            ],
            [
                ColumnValue(name="username", value="@brown"),
                ColumnValue(name="name", value="Jonh"),
            ],
            [
                ColumnValue(name="username", value="@blue"),
                ColumnValue(name="name", value="Jonh"),
            ],
        ],
    )


The argument parameters for the ``insert_bulk`` methods are as follows.

.. rst-class:: my-table

+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+----------+----------+
| Argument     | Description                                                                                                                                                                                                 | Type                                           | Required | Default  |
+==============+=============================================================================================================================================================================================================+================================================+==========+==========+
| ``instance`` | The instance of the table where the row will be inserted.                                                                                                                                                   | ``Model``                                      | ``Yes``  | ``None`` |
+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+----------+----------+
| ``values``   | The column values to be inserted into the table. **It must be a list of list of column values with the same length, otherwise dataloom will fail to map the values correctly during the insert operation.** | list[list[``ColumnValue``]] or ``ColumnValue`` | ``Yes``  | ``None`` |
+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+----------+----------+

.. tip:: In contrast to the ``insert_one`` method, the ``insert_bulk`` method returns the row count of the inserted documents rather than the individual primary keys (``pks``) of those documents.
