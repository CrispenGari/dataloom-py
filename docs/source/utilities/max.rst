5. ``max()``
++++++++++++

This is a utility function that comes within the ``loom`` object that is used to find the maximum value in rows of data in a database table that meets a specific criteria. Here is an example on how to use this utility function.

.. code-block:: 

    # example
    _max = mysql_loom.max(
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
    print(_max)


The ``max`` function takes the following arguments:

.. rst-class:: my-table

+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| Argument     | Description                                                                                                | Type                           | Default   | Required |
+==============+============================================================================================================+================================+===========+==========+
| ``instance`` | The model class to retrieve documents from.                                                                | ``Model``                      | ``None``  | ``Yes``  |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| ``column``   | A string of column to find maximum values based on.                                                        | ``str``                        | ``None``  | ``Yes``  |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| ``limit``    | Maximum number of documents to retrieve.                                                                   | ``int``                        | ``None``  | ``No``   |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| ``offset``   | Number of documents to skip before finding the maximum.                                                    | ``int``                        | ``0``     | ``No``   |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| ``filters``  | Collection of ``Filter`` or a ``Filter`` to apply to the rows to be used.                                  | ``list[Filter]`` or ``Filter`` | ``None``  | ``No``   |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
| ``distinct`` | Boolean telling dataloom to find maximum value in distinct rows of values based on selected column or not. | ``bool``                       | ``False`` | ``No``   |
+--------------+------------------------------------------------------------------------------------------------------------+--------------------------------+-----------+----------+
