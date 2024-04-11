Ordering Records
++++++++++++++++

In ``dataloom`` you can order documents in either ```DESC``` (descending) or ```ASC``` (ascending) order using the helper class ``Order``.

.. code-block:: 

    posts = mysql_loom.find_all(
        instance=Post,
        order=[Order(column="id", order="DESC")],
    )


You can apply multiple and these orders will ba applied in sequence of application here is an example:

.. code-block:: 

    posts = mysql_loom.find_all(
        instance=Post,
        order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
    )

