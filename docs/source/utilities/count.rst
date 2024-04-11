3. ``count()``
++++++++++++++

This is a utility function that comes within the ``loom`` object that is used to count rows in a database table that meets a specific criteria. Here is an example on how to use this utility function.

.. code-block:: 

    # example
    count = mysql_loom.count(
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
    print(count)

The ``count`` function takes the following arguments:

.. rst-class:: my-table

+--------------+--------------------------------------------------------------------------------------------+
| Argument     | Description                                                                                |
+==============+============================================================================================+
| ``instance`` | The model class to retrieve documents from.                                                |
+--------------+--------------------------------------------------------------------------------------------+
| ``column``   | A string of column to count values based on.                                               |
+--------------+--------------------------------------------------------------------------------------------+
| ``limit``    | Maximum number of documents to retrieve.                                                   |
+--------------+--------------------------------------------------------------------------------------------+
| ``offset``   | Number of documents to skip before counting.                                               |
+--------------+--------------------------------------------------------------------------------------------+
| ``filters``  | Collection of ``Filter`` or a ``Filter`` to apply to the rows to be counted.               |
+--------------+--------------------------------------------------------------------------------------------+
| ``distinct`` | Boolean telling dataloom to count distinct rows of values based on selected column or not. |
+--------------+--------------------------------------------------------------------------------------------+
