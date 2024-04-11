7. ``sum()``
++++++++++++

This is a utility function that comes within the ``loom`` object that is used to find the total sum in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

.. code-block:: 

    # example
    _sum = mysql_loom.sum(
        instance=Post,
        filters=Filter(
            column="id",
            operator="between",
            value=[1, 7],
        ),
        column="id",
        limit=3,
        offset=0,
        distinct=True,
    )
    print(_sum)


The ``sum`` function takes the following arguments:

.. rst-class:: my-table

+--------------+------------------------------------------------------------------------------------------------+
| Argument     | Description                                                                                    |
+==============+================================================================================================+
| ``instance`` | The model class to retrieve documents from.                                                    |
+--------------+------------------------------------------------------------------------------------------------+
| ``column``   | A string of column to sum values based on.                                                     |
+--------------+------------------------------------------------------------------------------------------------+
| ``limit``    | Maximum number of documents to retrieve.                                                       |
+--------------+------------------------------------------------------------------------------------------------+
| ``offset``   | Number of documents to skip before summing.                                                    |
+--------------+------------------------------------------------------------------------------------------------+
| ``filters``  | Collection of ``Filter`` or a ``Filter`` to apply to the rows to be used.                      |
+--------------+------------------------------------------------------------------------------------------------+
| ``distinct`` | Boolean telling dataloom to sum value in distinct rows values based on selected column or not. |
+--------------+------------------------------------------------------------------------------------------------+
