3. Updating a record
++++++++++++++++++++

To update records in your database table you make use of the following functions:

1. ``update_by_pk()``
2. ``update_one()``
3. ``update_bulk()``

1. ``update_by_pk()``
=====================

The ``update_pk()`` method can be used as follows:

.. code-block:: 

    affected_rows = mysql_loom.update_by_pk(
        instance=Post,
        pk=1,
        values=[
            ColumnValue(name="title", value="Updated?"),
        ],
    )


The above method takes in the following as arguments:

.. rst-class:: my-table

+--------------+--------------------------------------------------------------------+------------------------------------------+---------+----------+
| Argument     | Description                                                        | Type                                     | Default | Required |
+==============+====================================================================+==========================================+=========+==========+
| ``instance`` | The model class for which to update the instance.                  | ``Model``                                |         | ``Yes``  |
+--------------+--------------------------------------------------------------------+------------------------------------------+---------+----------+
| ``pk``       | The primary key value of the instance to update.                   | ``Any``                                  |         | ``Yes``  |
+--------------+--------------------------------------------------------------------+------------------------------------------+---------+----------+
| ``values``   | Single or Collection of ``ColumnValue`` to update in the instance. | ``ColumnValue`` or ``list[ColumnValue]`` |         | ``Yes``  |
+--------------+--------------------------------------------------------------------+------------------------------------------+---------+----------+

2. ``update_one()``
===================

Here is an example illustrating how to use the ``update_one()`` method:

.. code-block:: 

    affected_rows = mysql_loom.update_one(
        instance=Post,
        filters=[
            Filter(column="id", value=8, join_next_with="OR"),
            Filter(column="userId", value=1, join_next_with="OR"),
        ],
        values=[
            ColumnValue(name="title", value="Updated?"),
        ],
    )


The method takes the following as arguments:

.. rst-class:: my-table

+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| Argument     | Description                                                           | Type                                       | Default | Required |
+==============+=======================================================================+============================================+=========+==========+
| ``instance`` | The model class for which to update the instance(s).                  | ``Model``                                  |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| ``filters``  | Filter or collection of filters to apply to the update query.         | ``Filter`` or ``list[Filter]`` or ``None`` |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| ``values``   | Single or collection of column-value pairs to update in the instance. | ``ColumnValue`` or ``list[ColumnValue]``   |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+


3. ``update_bulk()``
====================

The ``update_bulk()`` method updates all records that match a filter in a database table.

.. code-block:: python

    affected_rows = mysql_loom.update_bulk(
        instance=Post,
        filters=[
            Filter(column="id", value=8, join_next_with="OR"),
            Filter(column="userId", value=1, join_next_with="OR"),
        ],
        values=[
            ColumnValue(name="title", value="Updated?"),
        ],
    )


The above method takes in the following as argument:

.. rst-class:: my-table

+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| Argument     | Description                                                           | Type                                       | Default | Required |
+==============+=======================================================================+============================================+=========+==========+
| ``instance`` | The model class for which to update instances.                        | ``Model``                                  |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| ``filters``  | Filter or collection of filters to apply to the update query.         | ``Filter`` or ``list[Filter]`` or ``None`` |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
| ``values``   | Single or collection of column-value pairs to update in the instance. | ``ColumnValue`` or ``list[ColumnValue]``   |         | ``Yes``  |
+--------------+-----------------------------------------------------------------------+--------------------------------------------+---------+----------+
