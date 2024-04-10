Usage
+++++

In this section we are going to go through how you can use our ``orm`` package in your project.

Connection
==========

To use Dataloom, you need to establish a connection with a specific database ``dialect``. The available dialect options are ``mysql``, ``postgres``, and ``sqlite``.

**Postgres**

The following is an example of how you can establish a connection with postgres database.

.. code-block:: 

    from dataloom import Loom

    # Create a Loom instance with PostgreSQL configuration
    pg_loom = Loom(
        dialect="postgres",
        database="hi",
        password="root",
        user="postgres",
        host="localhost",
        sql_logger="console",
        logs_filename="logs.sql",
        port=5432,
    )

    # Connect to the PostgreSQL database
    conn = pg_loom.connect()


    # Close the connection when the script completes
    if __name__ == "__main__":
        conn.close()

In ``dataloom`` you can use connection uris to establish a connection to the database in ``postgres`` as follows:

.. code-block:: 

    pg_loom = Loom(
        dialect="postgres",
        connection_uri = "postgressql://root:root@localhost:5432/hi",
    # ...
    )

This will establish a connection with ``postgres`` with the database ``hi``.

**MySQL**

To establish a connection with a ``MySQL`` database using ``Loom``, you can use the following example:

.. code-block:: 

    from dataloom import Loom

    # Create a Loom instance with MySQL configuration
    mysql_loom = Loom(
        dialect="mysql",
        database="hi",
        password="root",
        user="root",
        host="localhost",
        sql_logger="console",
        logs_filename="logs.sql",
        port=3306,
    )

    # Connect to the MySQL database
    conn = mysql_loom.connect()

    # Close the connection when the script completes
    if __name__ == "__main__":
        conn.close()


In ``dataloom`` you can use connection uris to establish a connection to the database in ``mysql`` as follows:

.. code-block:: 

    mysql_loom = Loom(
        dialect="mysql",
        connection_uri = "mysql://root:root@localhost:3306/hi",
    # ...
    )


This will establish a connection with ``mysql`` with the database ``hi``.

**SQLite**

To establish a connection with an ``SQLite`` database using ``Loom``, you can use the following example:

.. code-block:: 

    from dataloom import Loom

    # Create a Loom instance with SQLite configuration
    sqlite_loom = Loom(
        dialect="sqlite",
        database="hi.db",
        logs_filename="sqlite-logs.sql",
        logging=True,
        sql_logger="console",
    )

    # Connect to the SQLite database
    conn = sqlite_loom.connect()

    # Close the connection when the script completes
    if __name__ == "__main__":
        conn.close()


In ``dataloom`` you can use connection uris to establish a connection to the database in ``sqlite`` as follows:

.. code-block:: 

    sqlite_loom = Loom(
        dialect="sqlite",
    connection_uri = "sqlite:///hi.db",
    # ...
    )

This will establish a connection with ``sqlite`` with the database ``hi``.