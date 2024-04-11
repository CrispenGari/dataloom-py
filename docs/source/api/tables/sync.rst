1. The ``sync`` method.
+++++++++++++++++++++++

This method enables you to create and save tables into the database. For instance, if you have two models, ``User`` and ``Post``, and you want to synchronize them with the database, you can achieve it as follows.

.. code-block:: 

    tables = sqlite_loom.sync([Post, User], drop=True, force=True)
    print(tables)


The method returns a list of table names that have been created or that exist in your database.

.. note:: We've noticed two steps involved in starting to work with our ``orm``. Initially, you need to create a connection and then synchronize the tables in another step.
    So we have designed the `connect_and_sync <connect_and_sync.html>`_ method that does that at once.
