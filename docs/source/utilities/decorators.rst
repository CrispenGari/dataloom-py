2. ``decorators``
+++++++++++++++++

These modules contain several decorators that can prove useful when creating models. These decorators originate from ``dataloom.decorators``, and at this stage, we are referring to them as "experimental."

``@initialize()``
=================

Let's examine a model named ``Profile``, which appears as follows:

.. code-block:: 

    class Profile(Model):
        __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
        id = PrimaryKeyColumn(type="int", auto_increment=True)
        avatar = Column(type="text", nullable=False)
        userId = ForeignKeyColumn(
            User,
            maps_to="1-1",
            type="int",
            required=True,
            onDelete="CASCADE",
            onUpdate="CASCADE",
        )


This is simply a Python class that inherits from the top-level class ``Model``. However, it lacks some useful ``dunder`` methods such as ``__init__`` and ``__repr__``. In standard Python, we can achieve this functionality by using ``dataclasses``. For example, we can modify our class as follows:

.. code-block:: 

    from dataclasses import dataclass

    @dataclass
    class Profile(Model):
        # ....



However, this approach doesn't function as expected in ``dataloom`` columns. Hence, we've devised these experimental decorators to handle the generation of essential dunder methods required for working with ``dataloom``. If you prefer not to use decorators, you always have the option to manually create these dunder methods. Here's an example:

.. code-block:: 

    class Profile(Model):
        # ...
        def __init__(self, id: int | None, avatar: str | None, userId: int | None) -> None:
            self.id = id
            self.avatar = avatar
            self.userId = userId

        def __repr__(self) -> str:
            return f"<{self.__class__.__name__}:id={self.id}>"

        @property
        def to_dict(self):
            return {"id": self.id, "avatar": self.avatar, "userId": self.userId}


However, by using the ``initialize`` decorator, this functionality will be automatically generated for you. Here's all you need to do:

.. code-block:: 

    from dataloom.decorators import initialize

    @initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
    class Profile(Model):
        # ...


.. tip:: 👉 **Tip**: Dataloom has a clever way of skipping the ``TableColumn`` because it doesn't matter in this case.

The ``initialize`` decorator takes the following arguments:

.. rst-class:: my-table

+---------------------+---------------------------------------------------------------+---------------------+-----------+----------+
| Argument            | Description                                                   | Type                | Default   | Required |
+=====================+===============================================================+=====================+===========+==========+
| ``to_dict``         | Flag indicating whether to generate a ``to_dict`` method.     | ``bool``            | ``False`` | ``No``   |
+---------------------+---------------------------------------------------------------+---------------------+-----------+----------+
| ``init``            | Flag indicating whether to generate an ``__init__`` method.   | ``bool``            | ``True``  | ``No``   |
+---------------------+---------------------------------------------------------------+---------------------+-----------+----------+
| ``repr``            | Flag indicating whether to generate a ``__repr__`` method.    | ``bool``            | ``False`` | ``No``   |
+---------------------+---------------------------------------------------------------+---------------------+-----------+----------+
| ``repr_identifier`` | Identifier for the attribute used in the ``__repr__`` method. | ``str`` or ``None`` | ``None``  | ``No``   |
+---------------------+---------------------------------------------------------------+---------------------+-----------+----------+


.. tip:: 👍 **Pro Tip:** Note that this ``decorator`` function allows us to interact with our data from the database in an object-oriented way in Python. Below is an example illustrating this concept:

.. code-block:: 

    profile = mysql_loom.find_by_pk(Profile, pk=1, select=["avatar", "id"])
    profile = Profile(**profile)
    print(profile)  # ? = <Profile:id=1>
    print(profile.avatar)  # ? hello.jpg
