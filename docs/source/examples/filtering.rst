
Filtering Records
+++++++++++++++++

There are different find of filters that you can use when filtering documents for mutations and queries. Filters are very important to use when updating and deleting documents as they give you control on which documents should be updated or deleted. When doing a mutation you can use a single or multiple filters. Bellow is an example that shows you how you can use a single filter in deleting a single record that has an ``id`` greater than ``1`` from the database.

.. code-block:: 

    res2 = mysql_loom.delete_one(
        instance=Post,
        offset=0,
        order=Order(column="id", order="DESC"),
        filters=Filter(column="id", value=1, operator="gt"),
    )


Or you can use it as follows:

.. code-block:: 

    res2 = mysql_loom.delete_one(
        instance=Post,
        offset=0,
        order=[Order(column="id", order="DESC")],
        filters=[Filter(column="id", value=1, operator="gt")],
    )


As you have noticed, you can join your filters together and they will be applied sequentially using the ``join_next_with`` which can be either ``OR`` or ``AND`` te default value is ``AND``. Here is an of filter usage in sequential.

.. code-block:: 

    res2 = mysql_loom.delete_one(
        instance=Post,
        offset=0,
        order=[Order(column="id", order="DESC")],
        filters=[
            Filter(column="id", value=1, operator="gt"),
            Filter(column="userId", value=1, operator="eq", join_next_with="OR"),
            Filter(
                column="title",
                value='"What are you doing general?"',
                operator="=",
                join_next_with="AND",
            ),
        ],
    )


Operators to use with Filters
=============================

You can use the ``operator`` to match the values. Here is the table of description for these filters.

.. rst-class:: my-table
    
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| Operator      | Explanation                                                                                                  | Expect                       |
+===============+==============================================================================================================+==============================+
| ``'eq'``      | Indicates equality. It checks if the value is equal to the specified criteria.                               | ``Value == Criteria``        |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'lt'``      | Denotes less than. It checks if the value is less than the specified criteria.                               | ``Value < Criteria``         |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'gt'``      | Denotes greater than. It checks if the value is greater than the specified criteria.                         | ``Value > Criteria``         |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'leq'``     | Denotes less than or equal to. It checks if the value is less than or equal to the specified criteria.       | ``Value <= Criteria``        |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'geq'``     | Denotes greater than or equal to. It checks if the value is greater than or equal to the specified criteria. | ``Value >= Criteria``        |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'in'``      | Checks if the value is included in a specified list of values.                                               | ``Value in List``            |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'notIn'``   | Checks if the value is not included in a specified list of values.                                           | ``Value in List``            |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'like'``    | Performs a pattern matching operation. It checks if the value is similar to a specified pattern.             | ``Value matches Pattern``    |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'not'``     | Indicates non-equality. It checks if the column value that does not equal to the specified criteria.         | ``Not Value = Criteria``     |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'neq'``     | Indicates non-equality. It checks if the value is not equal to the specified criteria.                       | ``Value != Criteria``        |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+
| ``'between'`` | It checks range values that matches a given range between the minimum and maximum.                           | ``Value BETWEEN (min, max)`` |
+---------------+--------------------------------------------------------------------------------------------------------------+------------------------------+

Let's talk about these filters in detail of code by example. Let's say you want to update a ``Post`` where the ``id`` matches ``1`` you can do it as follows:

.. code-block:: 

    res2 = mysql_loom.update_one(
        instance=Post,
        filters=Filter(
            column="id",
            value=1,
            operator="eq",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


What if you want to update a post where ``id`` is not equal to ``1`` you can do it as follows

.. code-block:: 

    res2 = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=1,
            operator="neq",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


What if i want to update the records that have an ``id`` less than ``3``?

.. code-block:: 

    res2 = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=3,
            operator="lt",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


What if i want to update the records that have an ``id`` less than or equal ``3``?

.. code-block:: 

    res2 = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=1,
            operator="neq",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


What if i want to update the records that have an ``id`` greater than ``3``?

.. code-block:: 

    res = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=3,
            operator="gt",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


What if i want to update the records that have an ``id`` greater or equal to ``3``?

.. code-block:: 

    res = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=3,
            operator="geq",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


You can use the ``in`` to update or query records that matches values in a specified ``list`` of values or ``tuple``. Here is an example showing you how you can update records that does matches ``id`` in ``[1, 2]``.

.. code-block:: 

    res = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=[1, 2],
            operator="in",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


You can use the ``notIn`` to update or query records that does not matches values in a specified ``list`` of values or ``tuple``. Here is an example showing you how you can update records that does not matches ``id`` in ``[1, 2]``.

.. code-block:: 


    res = mysql_loom.update_bulk(
        instance=Post,
        filters=Filter(
            column="id",
            value=[1, 2],
            operator="notIn",
        ),
        values=[ColumnValue(name="title", value="Bob")],
    )


You can use the ``like`` operator to match some patens in your query filters. Let's say we want to match a post that has the title ends with ``general`` we can use the ``like`` operator as follows

.. code-block:: 

    general = mysql_loom.find_one(
        instance=Post,
        filters=Filter(
            column="title",
            value="% general?",
            operator="like",
        ),
        select=["id", "title"],
    )

    print(general) # ?  {'id': 1, 'title': 'What are you doing general?'}


The following table show you some expression that you can use with this ``like`` operator.

.. rst-class:: my-table

+------------------+--------------------------------------------------------------------------------------------------------------------------+
| Value            | Description                                                                                                              |
+==================+==========================================================================================================================+
| ``%pattern``     | Finds values that end with the specified pattern.                                                                        |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``pattern%``     | Finds values that start with the specified pattern.                                                                      |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``%pattern%``    | Finds values that contain the specified pattern anywhere within the string.                                              |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``_pattern``     | Finds values that have any single character followed by the specified pattern.                                           |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``pattern_``     | Finds values that have the specified pattern followed by any single character.                                           |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``[charlist]%``  | Finds values that start with any character in the specified character list.                                              |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``[!charlist]%`` | Finds values that start with any character not in the specified character list.                                          |
+------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``_pattern_``    | Finds values that have any single character followed by the specified pattern and then followed by any single character. |
+------------------+--------------------------------------------------------------------------------------------------------------------------+




