Table Synchronization
+++++++++++++++++++++

Syncing tables involves the process of creating tables from models and saving them to a database. After defining your tables, you will need to synchronize your database tables using the ``sync`` method or the ``connect_and_sync``.

#. `sync Method <sync.html>`_ 
#. `connect_and_sync Method <connect_and_sync.html>`_ 


 The ``sync`` and ``connect_and_sync`` method accepts the following arguments:

.. rst-class:: my-table

+------------+----------------------------------------------------------------------------------------------------------------------------+-----------+-----------+
| Argument   | Description                                                                                                                | Type      | Default   |
+============+============================================================================================================================+===========+===========+
| ``models`` | A collection or a single instance(s) of your table classes that inherit from the ``Model`` class.                          | ``Model`` | ``[]``    |
+------------+----------------------------------------------------------------------------------------------------------------------------+-----------+-----------+
| ``drop``   | Whether to drop tables during syncing or not.                                                                              | ``bool``  | ``False`` |
+------------+----------------------------------------------------------------------------------------------------------------------------+-----------+-----------+
| ``force``  | Forcefully drop tables during syncing. In mysql this will temporarily disable foreign key checks when dropping the tables. | ``bool``  | ``False`` |
+------------+----------------------------------------------------------------------------------------------------------------------------+-----------+-----------+
| ``alter``  | Alter tables instead of dropping them during syncing or not.                                                               | ``bool``  | ``False`` |
+------------+----------------------------------------------------------------------------------------------------------------------------+-----------+-----------+

.. tip:: 🥇 We recommend you to use ``drop`` or ``force`` if you are going to change or modify ``foreign`` and ``primary`` keys. This is because setting the option ``alter`` does not have an effect on ``primary`` key columns.

.. toctree::
   :maxdepth: 2
   :hidden:

   sync
   connect_and_sync
   