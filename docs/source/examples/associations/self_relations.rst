5. ``Self`` Association
+++++++++++++++++++++++

Let's consider a scenario where we have a table ``Employee``, where an employee can have a supervisor, which in this case a supervisor is also an employee. This is an example of self relations. The model definition for this can be done as follows in ``dataloom``.

.. code-block:: 

    class Employee(Model):
        __tablename__: TableColumn = TableColumn(name="employees")
        id = PrimaryKeyColumn(type="int", auto_increment=True)
        name = Column(type="text", nullable=False, default="Bob")
        supervisorId = ForeignKeyColumn(
            "Employee", maps_to="1-1", type="int", required=False
        )


So clearly we can see that when creating a ``employee`` it is not a must to have a ``supervisorId`` as this relationship is optional.

.. tip:: 👍 **Pro Tip:** Note that when doing self relations the referenced table must be a string that matches the table class name irrespective of case. In our case we used ``"Employee"`` and also ``"employee"`` and ``"EMPLOYEe"`` will be valid, however ``"Employees"`` and also ``"employees"`` and ``"EMPLOYEEs"`` are invalid.

Inserting Records
==================

Here is how we can insert employees to this table and we will make ``John`` the supervisor of other employees.

.. code-block:: 

    empId = mysql_loom.insert_one(
        instance=Employee, values=ColumnValue(name="name", value="John Doe")
    )

    rows = mysql_loom.insert_bulk(
        instance=Employee,
        values=[
            [
                ColumnValue(name="name", value="Michael Johnson"),
                ColumnValue(name="supervisorId", value=empId),
            ],
            [
                ColumnValue(name="name", value="Jane Smith"),
                ColumnValue(name="supervisorId", value=empId),
            ],
        ],
    )



- Some employees is are associated with a supervisor ``John`` which are ``Jane`` and ``Michael``.
- However the employee ``John`` does not have a supervisor.

Retrieving Records
==================

Now let's query employee ``Michael`` with his supervisor.

.. code-block:: 

    emp = mysql_loom.find_by_pk(
        instance=Employee, pk=2, select=["id", "name", "supervisorId"]
    )
    sup = mysql_loom.find_by_pk(
        instance=Employee, select=["id", "name"], pk=emp["supervisorId"]
    )
    emp_and_sup = {**emp, "supervisor": sup}
    print(emp_and_sup) # ? = {'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'supervisor': {'id': 1, 'name': 'John Doe'}}


We're querying the database to retrieve information about a ``employee`` and their associated ``supervisor``.

1. **Querying an Employee**:

   - We use ``mysql_loom.find_by_pk()`` to fetch a single employee record from the database.
   - The employee's ID is specified as ``2``.

2. **Querying Supervisor**:

   - We use ``mysql_loom.find_by_pk()`` to retrieve a supervisor that is associated with this employee.
   - We create a dictionary ``emp_and_sup`` containing the ``employee`` information and their ``supervisor``.

With eager loading this can be done in one query as follows the above can be done as follows:

.. code-block:: 

    emp_and_sup = mysql_loom.find_by_pk(
        instance=Employee,
        pk=2,
        select=["id", "name", "supervisorId"],
        include=Include(
            model=Employee,
            has="one",
            select=["id", "name"],
            alias="supervisor",
        ),
    )

    print(emp_and_sup) # ? = {'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'supervisor': {'id': 1, 'name': 'John Doe'}}


- We use ``mysql_loom.find_by_pk()`` to fetch a single an employee record from the database.
- Additionally, we include associated ``employee`` record using ``eager`` loading with an ``alias`` of ``supervisor``.

.. tip:: 👍 **Pro Tip:** Note that the ``alias`` is very important in this situation because it allows you to get the included relationships with objects that are named well, if you don't give an alias dataloom will just use the model class name as the alias of your included models, in this case you will get an object that looks like ``{'id': 2, 'name': 'Michael Johnson', 'supervisorId': 1, 'employee': {'id': 1, 'name': 'John Doe'}}``, which practically and theoretically doesn't make sense.