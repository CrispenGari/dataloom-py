PrimaryKeyColumn
++++++++++++++++

This class is used to create a unique index in every table you create. In the context of a table that inherits from the ``Model`` class, exactly one ``PrimaryKeyColumn`` is required.



Below is an example of creating an ``id`` column as a primary key in a table named ``Post``.

.. code-block:: 

    class Post(Model):
        __tablename__: Optional[TableColumn] = TableColumn(name="users")
        id = PrimaryKeyColumn(type="int", auto_increment=True)
        #...rest of your columns



The following are the arguments that the ``PrimaryKeyColumn`` class accepts.

.. rst-class:: my-table

+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| Argument           | Description                                                                                                                        | Type                | Default   |
+====================+====================================================================================================================================+=====================+===========+
| ``type``           | The datatype of your primary key.                                                                                                  | ``str``             |           |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| ``length``         | ``Optional`` to specify the length of the type. If passed as ``N`` with type ``T``, it yields an SQL statement with type ``T(N)``. | ``int`` or ``None`` | ``None``  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| ``auto_increment`` | ``Optional`` to specify if the column will automatically increment or not.                                                         | ``bool``            | ``False`` |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| ``default``        | ``Optional`` to specify the default value in a column.                                                                             | ``any``             | ``None``  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| ``nullable``       | ``Optional`` to specify if the column will allow null values or not.                                                               | ``bool``            | ``False`` |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+
| ``unique``         | ``Optional`` to specify if the column will contain unique values or not.                                                           | ``bool``            | ``True``  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------+

.. note:: Each table you create that inherits from the `Model <model.html>`_ class requires this column to be available unless the table is a joint-table.
