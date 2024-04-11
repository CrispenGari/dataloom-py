ForeignKeyColumn Class
++++++++++++++++++++++

This class is utilized when informing ``dataloom`` that a column has a relationship with a primary key in another table. 
Consider the following model definition of a ``Post``

.. code-block:: 

    class Post(Model):
        __tablename__: Optional[TableColumn] = TableColumn(name="posts")
        id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
        completed = Column(type="boolean", default=False)
        title = Column(type="varchar", length=255, nullable=False)
        # timestamps
        createdAt = CreatedAtColumn()
        updatedAt = UpdatedAtColumn()
        # relations
        userId = ForeignKeyColumn(
            User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
        )



- ``userId`` is a foreign key in the table ``posts``, indicating it has a relationship with a primary key in the ``users`` table.

This column accepts the following arguments

.. rst-class:: my-table

+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| Argument | Description                                                                                                          | Type                               | Default     |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| table    | Required. This is the parent table that the current model references. In our example, this is referred to as 'User'. | str                                | --          |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| type     | Optional. Specifies the data type of the foreign key. If not provided, dataloom can infer it from the parent table.  | None                               | None        |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| required | Optional. Indicates whether the foreign key is required or not.                                                      | bool                               | False       |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| onDelete | Optional. Specifies the action to be taken when the associated record in the parent table is deleted.                | "NO ACTION", "SET NULL", "CASCADE" | "NO ACTION" |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+
| onUpdate | Optional. Specifies the action to be taken when the associated record in the parent table is updated.                | "NO ACTION", "SET NULL", "CASCADE" | "NO ACTION" |
+----------+----------------------------------------------------------------------------------------------------------------------+------------------------------------+-------------+

.. tip:: It is crucial to specify the actions for ``onDelete`` and ``onUpdate`` to ensure that ``dataloom`` manages your model's relationship actions appropriately. The available actions are

#. ``"NO ACTION"`` - If you delete or update the parent table, no changes will occur in the child table.
#. ``"SET NULL"`` - If you delete or update the parent table, the corresponding value in the child table will be set to ``null``.
#. ``"CASCADE"`` - If you delete or update the table, the same action will also be applied to the child table.