Loom
++++

This class is used to create a loom object that will be use to perform actions to a database.
The following example show how you can create a ``loom`` object using this class.

.. code-block:: 

    from dataloom import Loom
    loom = Loom(
        dialect="postgres",
        database="hi",
        password="root",
        user="postgres",
        host="localhost",
        sql_logger="console",
        logs_filename="logs.sql",
        port=5432,
    )

    # OR with connection_uri
    loom = Loom(
        dialect="mysql",
        connection_uri = "mysql://root:root@localhost:3306/hi",
    # ...
    )


The ``Loom`` class takes in the following options

.. rst-class:: my-table

+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| Parameter          | Description                                                                                                                                                                                                                                                                                                                                                                   | Value Type                          | Default Value    | Required |
+====================+===============================================================================================================================================================================================================================================================================================================================================================================+=====================================+==================+==========+
| ``connection_uri`` | The connection uri for the specified dialect.                                                                                                                                                                                                                                                                                                                                 | ``str`` or ``None``                 | ``None``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``dialect``        | Dialect for the database connection. Options are ``mysql``, ``postgres``, or ``sqlite``.                                                                                                                                                                                                                                                                                      | "mysql" or "postgres" or "sqlite"   | ``None``         | ``Yes``  |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``database``       | Name of the database for ``mysql`` and ``postgres``, filename for ``sqlite``.                                                                                                                                                                                                                                                                                                 | ``str`` or ``None``                 | ``None``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``password``       | Password for the database user (only for ``mysql`` and ``postgres``).                                                                                                                                                                                                                                                                                                         | ``str`` or ``None``                 | ``None``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``user``           | Database user (only for ``mysql`` and ``postgres``).                                                                                                                                                                                                                                                                                                                          | ``str`` or ``None``                 | ``None``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``host``           | Database host (only for ``mysql`` and ``postgres``).                                                                                                                                                                                                                                                                                                                          | ``str`` or ``None``                 | ``localhost``    | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``sql_logger``     | Enable logging for the database queries. If you don't want to see the sql logs you can set this option to ``None`` which is the default value. If you set it to file then you will see the logs in the default dataloom.sql file, you can overide this by passing a logs_filename option. Setting this option to console, then sql statements will be printed on the console. | ``console`` or ``file`` or ``None`` | ``True``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``logs_filename``  | Filename for the query logs                                                                                                                                                                                                                                                                                                                                                   | ``str`` or ``None``                 | ``dataloom.sql`` | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+
| ``port``           | Port number for the database connection (only for ``mysql`` and ``postgres``).                                                                                                                                                                                                                                                                                                | ``int`` or ``None``                 | ``None``         | ``No``   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+------------------+----------+

