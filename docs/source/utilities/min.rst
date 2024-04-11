4. ``min()``
++++++++++++

This is a utility function that comes within the ``loom`` object that is used to find the minimum value in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

.. code-block:: 

    # example
    _min = mysql_loom.min(
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
    print(_min)


The ``min`` function takes the following arguments:

.. rst-class:: my-table

+--------------+---------------------------------------------------------------------------------------------------------+
| Argument     | Description                                                                                             |
+==============+=========================================================================================================+
| ``instance`` | The model class to retrieve documents from.                                                             |
+--------------+---------------------------------------------------------------------------------------------------------+
| ``column``   | A string of column to find minimum values based on.                                                     |
+--------------+---------------------------------------------------------------------------------------------------------+
| ``limit``    | Maximum number of documents to retrieve.                                                                |
+--------------+---------------------------------------------------------------------------------------------------------+
| ``offset``   | Number of documents to skip before finding the minimum.                                                 |
+--------------+---------------------------------------------------------------------------------------------------------+
| ``filters``  | Collection of ``Filter`` or a ``Filter`` to apply to the rows to be used.                               |
+--------------+---------------------------------------------------------------------------------------------------------+
| ``distinct`` | Boolean telling dataloom to find minimum value in distinct rows values based on selected column or not. |
+--------------+---------------------------------------------------------------------------------------------------------+
