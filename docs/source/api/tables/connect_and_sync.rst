
2. The ``connect_and_sync`` method.
+++++++++++++++++++++++++++++++++++


The ``connect_and_sync`` function proves to be very handy as it handles both the database connection and table synchronization. Here is an example demonstrating its usage.

.. code-block:: 

    # ....
    sqlite_loom = Loom(
        dialect="sqlite", database="hi.db", logs_filename="sqlite-logs.sql", logging=True
    )
    conn, tables = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
    print(tables)

    if __name__ == "__main__":
        conn.close()


Returns a ``conn`` and the list of ``tablenames`` that exist in the database. The method accepts the same arguments as the ``sync`` method.


.. note:: See also - `sync <sync.html>`_
