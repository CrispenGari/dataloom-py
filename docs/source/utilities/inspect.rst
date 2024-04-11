1. ``inspect()``
++++++++++++++++

This function takes in a model as argument and inspect the model fields or columns. The following examples show how we can use this handy function in inspecting table names.

.. code-block:: 

    table = mysql_loom.inspect(instance=User, fields=["name", "type"], print_table=False)
    print(table)

The above snippet returns a list of dictionaries containing the column name and the arguments that were passed.

.. code-block:: shell

    [{'id': {'type': 'int'}}, {'name': {'type': 'varchar'}}, {'tokenVersion': {'type': 'int'}}, {'username': {'type': 'varchar'}}]

You can print table format these fields with their types as follows

.. code-block:: 

    mysql_loom.inspect(instance=User)

Output:

.. rst-class:: my-table

+--------------+---------+----------+---------+
| name         | type    | nullable | default |
+==============+=========+==========+=========+
| id           | int     | NO       | None    |
+--------------+---------+----------+---------+
| name         | varchar | NO       | Bob     |
+--------------+---------+----------+---------+
| tokenVersion | int     | YES      | 0       |
+--------------+---------+----------+---------+
| username     | varchar | YES      | None    |
+--------------+---------+----------+---------+



The ``inspect`` function take the following arguments.

.. rst-class:: my-table

+-----------------+--------------------------------------------------------+---------------+---------------------------------------------+----------+
| Argument        | Description                                            | Type          | Default                                     | Required |
+=================+========================================================+===============+=============================================+==========+
| ``instance``    | The model instance to inspect.                         | ``Model``     | --                                          | ``Yes``  |
+-----------------+--------------------------------------------------------+---------------+---------------------------------------------+----------+
| ``fields``      | The list of fields to include in the inspection.       | ``list[str]`` | ``["name", "type", "nullable", "default"]`` | ``No``   |
+-----------------+--------------------------------------------------------+---------------+---------------------------------------------+----------+
| ``print_table`` | Flag indicating whether to print the inspection table. | ``bool``      | ``True``                                    | ``No``   |
+-----------------+--------------------------------------------------------+---------------+---------------------------------------------+----------+
