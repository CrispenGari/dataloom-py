Include Class
+++++++++++++

The ``Include`` class facilitates eager loading for models with relationships. Below is a table detailing the parameters available for the ``Include`` class


The following example demonstrates how we can use the ``Include`` class do to eager loading by fetching the profile of the user when we fetch the user by primary key.

.. code-block:: 
    
    user_with_profile = mysql_loom.find_by_pk(
        instance=User,
        pk=userId,
        select=["id", "username"],
        include=[Include(model=Profile, select=["id", "avatar"], has="one")],
    )



.. rst-class:: my-table

+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| Argument           | Description                                                                                   | Type                | Default    | Required |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``model``          | The model to be included when eagerly fetching records.                                       | ``Model``           | --         | ``Yes``  |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``junction_table`` | The ``junction_table`` model that is used as a reference table in a many to many association. | ``Model``           | ``None``   | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``order``          | The list of order specifications for sorting the included data.                               | list[``Order``]     | ``[]``     | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``limit``          | The maximum number of records to include.                                                     | ``None``            | ``0``      | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``offset``         | The number of records to skip before including.                                               | ``None``            | ``0``      | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``select``         | The list of columns to include.                                                               | ``None``            | ``None``   | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``has``            | The relationship type between the current model and the included model.                       | ``INCLUDE_LITERAL`` | ``"many"`` | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``include``        | The extra included models.                                                                    | list[``Include``]   | ``[]``     | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+
| ``alias``          | The alias name for the included model. Very important when mapping self relations.            | ``str``             | ``None``   | ``No``   |
+--------------------+-----------------------------------------------------------------------------------------------+---------------------+------------+----------+

.. note:: You can include a single or multiple relations when doing eager data fetching in ``dataloom``.
