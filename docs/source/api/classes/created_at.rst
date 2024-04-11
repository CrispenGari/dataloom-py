
CreatedAtColumn Class
+++++++++++++++++++++

When a column is designated as ``CreatedAtColumn``, its value will be automatically generated each time you create a new record in a database, serving as a timestamp.


Bellow is an example demonstrating the use of the ``CreatedAtColumn`` class in a model ``Post``

.. code-block:: 

    class Post(Model):
        __tablename__: Optional[TableColumn] = TableColumn(name="posts")
        
        # timestamps
        createdAt = CreatedAtColumn()


.. note:: This means that every insert of a document in the ``posts`` table will have a timestamp ``createdAt`` column being automatically generated. You can also use another timestamp
    class called `UpdatedAtColumn <updated_at.html>`_ which automatically update to the current time stamp on the insertion or update of a record.
