2. Reading records
++++++++++++++++++

To retrieve documents or a document from the database, you can make use of the following functions:

1. ``find_all()``: This function is used to retrieve all documents from the database.
2. ``find_by_pk()``: This function is used to retrieve a document by its primary key (or ID).
3. ``find_one()``: This function is used to retrieve a single document based on a specific condition.
4. ``find_many()``: This function is used to retrieve multiple documents based on a specific condition.

1. ``find_all()``
================

This method is used to retrieve all the records that are in the database table. Below are examples demonstrating how to do it:

.. code-block:: 

    users = pg_loom.find_all(
        instance=User,
        select=["id", "username"],
        limit=3,
        offset=0,
        order=[Order(column="id", order="DESC")],
    )
    print(users) # ? [{'id': 1, 'username': '@miller'}]

The ``find_all()`` method takes in the following arguments:

.. rst-class:: my-table

+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| Argument     | Description                                                                                  | Type                             | Default  | Required |
+==============+==============================================================================================+==================================+==========+==========+
| ``instance`` | The model class to retrieve documents from.                                                  | ``Model``                        | ``None`` | ``Yes``  |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``select``   | Collection or a string of fields to select from the documents.                               | ``list[str]`` or ``str``         | ``None`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``limit``    | Maximum number of documents to retrieve.                                                     | ``int``                          | ``None`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``offset``   | Number of documents to skip before retrieving.                                               | ``int``                          | ``0``    | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``order``    | Collection of ``Order`` or a single ``Order`` to order the documents when querying.          | ``list[Order]`` or ``Order``     | ``None`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``include``  | Collection or a ``Include`` of related models to eagerly load.                               | ``list[Include]`` or ``Include`` | ``None`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``group``    | Collection of ``Group`` which specifies how you want your data to be grouped during queries. | ``list[Group]`` or ``Group``     | ``None`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+
| ``distinct`` | Boolean telling ``dataloom`` to return distinct row values based on selected fields or not.  | ``bool``                         | ``No``   |          |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+----------+----------+

.. tip:: 👍 **Pro Tip**: A collection can be any python iterable, the supported iterables are ``list``, ``set``, ``tuple``.

2. ``find_many()``
=================

Here is an example demonstrating the usage of the ``find_many()`` function with specific filters.

.. code-block:: 

    users = mysql_loom.find_many(
        User,
        filters=[Filter(column="username", value="@miller")],
        select=["id", "username"],
        offset=0,
        limit=10,
    )

    print(users) # ? [{'id': 1, 'username': '@miller'}]


The ``find_many()`` method takes in the following arguments:

.. rst-class:: my-table

+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| Argument     | Description                                                                                  | Type                             | Default   | Required |
+==============+==============================================================================================+==================================+===========+==========+
| ``instance`` | The model class to retrieve documents from.                                                  | ``Model``                        | ``None``  | ``Yes``  |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``select``   | Collection or a string of fields to select from the documents.                               | ``list[str]`` or ``str``         | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``limit``    | Maximum number of documents to retrieve.                                                     | ``int``                          | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``offset``   | Number of documents to skip before retrieving.                                               | ``int``                          | ``0``     | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``order``    | Collection of ``Order`` or a single ``Order`` to order the documents when querying.          | ``list[Order]`` or ``Order``     | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``include``  | Collection or a ``Include`` of related models to eagerly load.                               | ``list[Include]`` or ``Include`` | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``group``    | Collection of ``Group`` which specifies how you want your data to be grouped during queries. | ``list[Group]`` or ``Group``     | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``filters``  | Collection of ``Filter`` or a ``Filter`` to apply to the query.                              | ``list[Filter]`` or ``Filter``   | ``None``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+
| ``distinct`` | Boolean telling ``dataloom`` to return distinct row values based on selected fields or not.  | ``bool``                         | ``False`` | ``No``   |
+--------------+----------------------------------------------------------------------------------------------+----------------------------------+-----------+----------+

.. tip:: 👍 **Pro Tip**: The distinction between the ``find_all()`` and ``find_many()`` methods lies in the fact that ``find_many()`` enables you to apply specific filters, whereas ``find_all()`` retrieves all the documents within the specified model.

3. ``find_one()``
=================

Here is an example showing you how you can use ``find_one()`` locate a single record in the database.

.. code-block:: 

    user = mysql_loom.find_one(
        User,
        filters=[Filter(column="username", value="@miller")],
        select=["id", "username"],
    )
    print(user) # ? {'id': 1, 'username': '@miller'}


This method take the following as arguments

.. rst-class:: my-table

+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| Argument     | Description                                                                                    | Type                                       | Default  | Required |
+==============+================================================================================================+============================================+==========+==========+
| ``instance`` | The model class to retrieve instances from.                                                    | ``Model``                                  |          | ``Yes``  |
+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``filters``  | ``Filter`` or a collection of ``Filter`` to apply to the query.                                | ``Filter`` or ``list[Filter]`` or ``None`` | ``None`` | ``No``   |
+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``select``   | Collection of ``str`` or ``str`` of which is the name of the columns or column to be selected. | ``list[str]``or``str``                     | ``[]``   | ``No``   |
+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``include``  | Collection of ``Include`` or a single ``Include`` of related models to eagerly load.           | ``list[Include]``or``Include``             | ``[]``   | ``No``   |
+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+
| ``offset``   | Number of instances to skip before retrieving.                                                 | ``int`` or ``None``                        | ``No``   |          |
+--------------+------------------------------------------------------------------------------------------------+--------------------------------------------+----------+----------+

4. ``find_by_pk()``
===================

Here is an example showing how you can use the ``find_by_pk()`` to locate a single record in the database.

.. code-block:: 

    user = mysql_loom.find_by_pk(User, pk=userId, select=["id", "username"])
    print(user) # ? {'id': 1, 'username': '@miller'}

The method takes the following as arguments:

.. rst-class:: my-table

+--------------+----------------------------------------------------------------------------------------+----------------------------------+---------+----------+
| Argument     | Description                                                                            | Type                             | Default | Required |
+==============+========================================================================================+==================================+=========+==========+
| ``instance`` | The model class to retrieve instances from.                                            | ``Model``                        |         | ``Yes``  |
+--------------+----------------------------------------------------------------------------------------+----------------------------------+---------+----------+
| ``pk``       | The primary key value to use for retrieval.                                            | ``Any``                          |         | ``Yes``  |
+--------------+----------------------------------------------------------------------------------------+----------------------------------+---------+----------+
| ``select``   | Collection column names to select from the instances.                                  | ``list[str]``                    | ``[]``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------+----------------------------------+---------+----------+
| ``include``  | A Collection of ``Include`` or a single ``Include`` of related models to eagerly load. | ``list[Include]`` or ``Include`` | ``[]``  | ``No``   |
+--------------+----------------------------------------------------------------------------------------+----------------------------------+---------+----------+
