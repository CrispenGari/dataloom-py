
Query Builder
+++++++++++++

``Dataloom`` exposes a method called ``getQueryBuilder``, which allows you to obtain a ``qb`` object. This object enables you to execute SQL queries directly from SQL scripts.

.. code-block:: 

    qb = loom.getQueryBuilder()
    print(qb) # ? = Loom QB<mysql>


The ``qb`` object contains the method called ``run``, which is used to execute SQL scripts or SQL queries.

.. code-block:: 

    ids = qb.run("select id from posts;", fetchall=True)
    print(ids) # ? = [(1,), (2,), (3,), (4,)]


You can also execute SQL files. In the following example, we will demonstrate how you can execute SQL scripts using the ``qb``. Let's say we have an SQL file called ``qb.sql`` which contains the following SQL code:

.. code-block:: SQL
    -- qb.sql

    SELECT id, title FROM posts WHERE id IN (1, 3, 2, 4) LIMIT 4 OFFSET  1;
    SELECT COUNT(*) FROM (
        SELECT DISTINCT `id`
        FROM `posts`
        WHERE `id` < 5
        LIMIT 3 OFFSET 2
    ) AS subquery;


We can use the query builder to execute the SQL as follows:

.. code-block:: 

    with open("qb.sql", "r") as reader:
        sql = reader.read()
    res = qb.run(
        sql,
        fetchall=True,
        is_script=True,
    )
    print(res)


.. tip:: 👍 **Pro Tip:** Executing a script using query builder does not return a result. The result value is always ``None``.

The ``run`` method takes the following as arguments:

.. rst-class:: my-table

+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| Argument          | Description                                                                              | Type                                                             | Required | Default   |
+===================+==========================================================================================+==================================================================+==========+===========+
| ``sql``           | SQL query to execute.                                                                    | ``str``                                                          | `Yes`    |           |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``args``          | Parameters for the SQL query.                                                            | ``Any`` or ``None``                                              | ``No``   | ``None``  |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``fetchone``      | Whether to fetch only one result.                                                        | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``fetchmany``     | Whether to fetch multiple results.                                                       | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``fetchall``      | Whether to fetch all results.                                                            | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``mutation``      | Whether the query is a mutation (insert, update, delete).                                | ``bool``                                                         | ``No``   | ``True``  |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``bulk``          | Whether the query is a bulk operation.                                                   | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``affected_rows`` | Whether to return affected rows.                                                         | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``operation``     | Type of operation being performed.                                                       | ``'insert'``, ``'update'``, ``'delete'``, ``'read'`` or ``None`` | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``verbose``       | Verbosity level for logging . Set this option to ``0`` if you don't want logging at all. | ``int``                                                          | ``No``   | ``1``     |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+
| ``is_script``     | Whether the SQL is a script.                                                             | ``bool``                                                         | ``No``   | ``False`` |
+-------------------+------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------+-----------+


Why Use Query Builder?
----------------------

- The query builder empowers developers to seamlessly execute ``SQL`` queries directly.
- While Dataloom primarily utilizes ``subqueries`` for eager data fetching on models, developers may prefer to employ JOIN operations, which are achievable through the ``qb`` object.

.. code-block:: 
    qb = loom.getQueryBuilder()
    result = qb.run("SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.table1_id;")
    print(result)
  