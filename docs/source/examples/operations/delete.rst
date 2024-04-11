4. Deleting a record
++++++++++++++++++++

To delete a record or records in a database table you make use of the following functions:

1. ``delete_by_pk()``
2. ``delete_one()``
3. ``delete_bulk()``

1. ``delete_by_pk()``
=====================

Using the ``delete_by_pk()`` method, you can delete a record in a database based on the primary-key value.

.. code-block:: 

    affected_rows = mysql_loom.delete_by_pk(instance=User, pk=1)


The above take the following as arguments:

.. rst-class:: my-table

+--------------+----------------------------------------------------+-----------+---------+----------+
| Argument     | Description                                        | Type      | Default | Required |
+==============+====================================================+===========+=========+==========+
| ``instance`` | The model class from which to delete the instance. | ``Model`` |         | ``Yes``  |
+--------------+----------------------------------------------------+-----------+---------+----------+
| ``pk``       | The primary key value of the instance to delete.   | ``Any``   |         | ``Yes``  |
+--------------+----------------------------------------------------+-----------+---------+----------+


2. ``delete_one()``
===================

You can also use ``filters`` to delete a record in a database. The ``delete_one()`` function enables you to delete a single record in a database that matches a filter.

.. code-block:: 

    affected_rows = mysql_loom.delete_one(
        instance=User, filters=[Filter(column="username", value="@miller")]
    )


The method takes in the following arguments:

.. rst-class:: my-table

+--------------+-------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| Argument     | Description                                                                               | Type                                       | Default  | Required |
+==============+===========================================================================================+============================================+==========+==========+
| ``instance`` | The model class from which to delete the instance(s).                                     | ``Model``                                  |          | ``Yes``  |
+--------------+-------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``filters``  | Filter or collection of filters to apply to the deletion query.                           | ``Filter`` or ``list[Filter]`` or ``None`` | ``None`` | ``No``   |
+--------------+-------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``offset``   | Number of instances to skip before deleting.                                              | ``int`` or ``None``                        | ``No``   |          |
+--------------+-------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``order``    | Collection of ``Order`` or as single ``Order`` to order the instances by before deletion. | ``list[Order]`` or ``Order``or ``None``    | ``[]``   | ``No``   |
+--------------+-------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+


3. ``delete_bulk()``
====================

You can also use the ``delete_bulk()`` method to delete a multitude of records that match a given filter:

.. code-block:: 

    affected_rows = mysql_loom.delete_bulk(
        instance=User, filters=[Filter(column="username", value="@miller")]
    )


The method takes the following as arguments:

.. rst-class:: my-table

+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| Argument     | Description                                                                              | Type                                       | Default  | Required |
+==============+==========================================================================================+============================================+==========+==========+
| ``instance`` | The model class from which to delete instances.                                          | ``Model``                                  |          | ``Yes``  |
+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``filters``  | Filter or collection of filters to apply to the deletion query.                          | ``Filter`` or ``list[Filter]`` or ``None`` | ``None`` | ``No``   |
+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``limit``    | Maximum number of instances to delete.                                                   | ``int`` or ``None``                        | ``No``   |          |
+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``offset``   | Number of instances to skip before deleting.                                             | ``int`` or ``None``                        | ``No``   |          |
+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``order``    | Collection of ``Order`` or a single ``Order`` to order the instances by before deletion. | ``list[Order]`` or ``Order``or ``None``    | ``[]``   | ``No``   |
+--------------+------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+


Warning: Potential Risk with ``delete_bulk()``
----------------------------------------------

.. warning:: When using the ``delete_bulk()`` function, exercise caution as it can be aggressive. If the filter is not explicitly provided, there is a risk of mistakenly deleting all records in the table.

Guidelines for Safe Usage
----------------------------------------------

To mitigate the potential risks associated with ``delete_bulk()``, follow these guidelines:

1. **Always Provide a Filter:**

   - When calling ``delete_bulk()``, make sure to provide a filter to specify the subset of records to be deleted. This helps prevent unintentional deletions.

   .. code-block::
   
        # Example: Delete records where 'status' is 'inactive'
        affected_rows = mysql_loom.delete_bulk(
            instance=User,
            filters=Filter(column="status",  value='inactive'),
        )


2. **Consider Usage When Necessary:**

- When contemplating data deletion, it is advisable to consider more targeted methods before resorting to ``delete_bulk()``. Prioritize the use of ``delete_one()`` or ``delete_by_pk()`` methods to remove specific records based on your needs. This ensures a more precise and controlled approach to data deletion.

3. **Use limit and offsets options**

- You can consider using the ``limit`` and offset options during invocation of ``delete_bulk``

.. code-block:: 

    affected_rows = mysql_loom.delete_bulk(
        instance=Post,
        order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
        filters=[Filter(column="id", operator="gt", value=0)],
        offset=0,
        limit=10,
    )


By following these guidelines, you can use the ``delete_bulk()`` function safely and minimize the risk of unintended data loss. Always exercise caution and adhere to best practices when performing bulk deletion operations.