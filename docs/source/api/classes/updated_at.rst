
UpdatedAtColumn Class
+++++++++++++++++++++

When a column is designated as ``UpdatedAtColumn``, its value will be automatically generated each time you create a new record or update an existing record in a database table, acting as a timestamp.



Bellow is an example demonstrating the use of the ``UpdatedAtColumn`` class in a model ``Post``

.. code-block:: 

    class Post(Model):
        __tablename__: Optional[TableColumn] = TableColumn(name="posts")
        
        # timestamps
        updatedAt = UpdatedAtColumn()


.. note:: This means that every update or on the first insertion of a document in the ``posts`` table will have a timestamp ``updatedAt`` column being automatically generated and updated when a record is updated. You can also use another timestamp
    class called `CreatedAtColumn <created_at.html>`_ which automatically set current time stamp on the insertion of a record.
