6. ``Many to Many`` Relationship
++++++++++++++++++++++++++++++++

Let's consider a scenario where we have tables for ``Students`` and ``Courses``. In this scenario, a student can enroll in many courses, and a single course can have many students enrolled. This represents a ``Many-to-Many`` relationship. The model definitions for this scenario can be done as follows in ``dataloom``:

**Table: Student**

.. rst-class:: my-table

+-------------+-------------+
| Column Name | Data Type   |
+=============+=============+
| ``id``      | ``INT``     |
+-------------+-------------+
| ``name``    | ``VARCHAR`` |
+-------------+-------------+

**Table: Course**
.. rst-class:: my-table

+-------------+-------------+
| Column Name | Data Type   |
+=============+=============+
| ``id``      | ``INT``     |
+-------------+-------------+
| ``name``    | ``VARCHAR`` |
+-------------+-------------+
| ...         | ...         |
+-------------+-------------+

**Table: Student_Courses** (junction table)

.. rst-class:: my-table

+---------------+-----------+
| Column Name   | Data Type |
+===============+===========+
| ``studentId`` | ``INT``   |
+---------------+-----------+
| ``courseId``  | ``INT``   |
+---------------+-----------+


.. tip:: 👍 **Pro Tip:** Note that the ``junction`` table can also be called ``association``-table or ``reference``-table or ``joint``-table.

In ``dataloom`` we can model the above relations as follows:

.. code-block:: 

    class Course(Model):
        __tablename__: TableColumn = TableColumn(name="courses")
        id = PrimaryKeyColumn(type="int", auto_increment=True)
        name = Column(type="text", nullable=False, default="Bob")


    class Student(Model):
        __tablename__: TableColumn = TableColumn(name="students")
        id = PrimaryKeyColumn(type="int", auto_increment=True)
        name = Column(type="text", nullable=False, default="Bob")


    class StudentCourses(Model):
        __tablename__: TableColumn = TableColumn(name="students_courses")
        studentId = ForeignKeyColumn(table=Student, type="int")
        courseId = ForeignKeyColumn(table=Course, type="int")



- The tables ``students`` and ``courses`` will not have foreign keys.
- The ``students_courses`` table will have two columns that joins these two tables together in an ``N-N`` relational mapping.

.. tip:: 👍 **Pro Tip:** In a joint table no other columns such as ``CreateAtColumn``, ``UpdatedAtColumn``, ``Column`` and ``PrimaryKeyColumn`` are allowed and only exactly ``2`` foreign keys should be in this table.

Inserting Records
=================

Here is how we can insert ``students`` and ``courses`` in their respective tables.

.. code-block:: 


    # insert the courses
    mathId = mysql_loom.insert_one(
        instance=Course, values=ColumnValue(name="name", value="Mathematics")
    )
    engId = mysql_loom.insert_one(
        instance=Course, values=ColumnValue(name="name", value="English")
    )
    phyId = mysql_loom.insert_one(
        instance=Course, values=ColumnValue(name="name", value="Physics")
    )

    # create students

    stud1 = mysql_loom.insert_one(
        instance=Student, values=ColumnValue(name="name", value="Alice")
    )
    stud2 = mysql_loom.insert_one(
        instance=Student, values=ColumnValue(name="name", value="Bob")
    )
    stud3 = mysql_loom.insert_one(
        instance=Student, values=ColumnValue(name="name", value="Lisa")
    )


- You will notice that we are keeping in track of the ``studentIds`` and the ``courseIds`` because we will need them in the ``joint-table`` or ``association-table``.
- Now we can enrol students to their courses by inserting them in their id's in the association table.

.. code-block:: 

    # enrolling students
    mysql_loom.insert_bulk(
        instance=StudentCourses,
        values=[
            [
                ColumnValue(name="studentId", value=stud1),
                ColumnValue(name="courseId", value=mathId),
            ],  # enrolling Alice to mathematics
            [
                ColumnValue(name="studentId", value=stud1),
                ColumnValue(name="courseId", value=phyId),
            ],  # enrolling Alice to physics
            [
                ColumnValue(name="studentId", value=stud1),
                ColumnValue(name="courseId", value=engId),
            ],  # enrolling Alice to english
            [
                ColumnValue(name="studentId", value=stud2),
                ColumnValue(name="courseId", value=engId),
            ],  # enrolling Bob to english
            [
                ColumnValue(name="studentId", value=stud3),
                ColumnValue(name="courseId", value=phyId),
            ],  # enrolling Lisa to physics
            [
                ColumnValue(name="studentId", value=stud3),
                ColumnValue(name="courseId", value=engId),
            ],  # enrolling Lisa to english
        ],
    )



Retrieving Records
==================

Now let's query a student called ``Alice`` with her courses. We can do it as follows:

.. code-block:: 

    s = mysql_loom.find_by_pk(
        Student,
        pk=stud1,
        select=["id", "name"],
    )
    c = mysql_loom.find_many(
        StudentCourses,
        filters=Filter(column="studentId", value=stud1),
        select=["courseId"],
    )
    courses = mysql_loom.find_many(
        Course,
        filters=Filter(column="id", operator="in", value=[list(i.values())[0] for i in c]),
        select=["id", "name"],
    )

    alice = {**s, "courses": courses}
    print(courses) # ? = {'id': 1, 'name': 'Alice', 'courses': [{'id': 1, 'name': 'Mathematics'}, {'id': 2, 'name': 'English'}, {'id': 3, 'name': 'Physics'}]}


We're querying the database to retrieve information about a ``student`` and their associated ``courses``. Here are the steps in achieving that:

1. **Querying Student**:

   - We use ``mysql_loom.find_by_pk()`` to fetch a single ``student`` record from the database in the table ``students``.

2. **Querying Course Id's**:
   - Next we are going to query all the course ids of that student and store them in ``c`` in the joint table ``students_courses``.
   - We use ``mysql_loom.find_many()`` to retrieve the course ``ids`` of ``alice``.
3. **Querying Course**:
   - Next we will query all the courses using the operator ``in`` in the ``courses`` table based on the id's we obtained previously.

As you can see we are doing a lot of work to get the information about ``Alice``. With eager loading this can be done in one query as follows the above can be done as follows:

.. code-block:: 

    alice = mysql_loom.find_by_pk(
        Student,
        pk=stud1,
        select=["id", "name"],
        include=Include(
            model=Course, junction_table=StudentCourses, alias="courses", has="many"
        ),
    )

    print(alice) # ? = {'id': 1, 'name': 'Alice', 'courses': [{'id': 1, 'name': 'Mathematics'}, {'id': 2, 'name': 'English'}, {'id': 3, 'name': 'Physics'}]}


- We use ``mysql_loom.find_by_pk()`` to retrieve a single student record from the database.
- Furthermore, we include the associated ``course`` records using ``eager`` loading with an ``alias`` of ``courses``.
- We specify a ``junction_table`` in our ``Include`` statement. This allows dataloom to recognize the relationship between the ``students`` and ``courses`` tables through this ``junction_table``.

.. note:: 👍 **Pro Tip:** It is crucial to specify the ``junction_table`` when querying in a many-to-many (``N-N``) relationship. This is because, by default, the models will not establish a direct many-to-many relationship without referencing the ``junction_table``. They lack foreign key columns within them to facilitate this relationship.

As for our last example let's query all the students that are enrolled in the ``English`` class. We can easily do it as follows:

.. code-block:: 

    english = mysql_loom.find_by_pk(
        Course,
        pk=engId,
        select=["id", "name"],
        include=Include(model=Student, junction_table=StudentCourses, has="many"),
    )

    print(english) # ? = {'id': 2, 'name': 'English', 'students': [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Lisa'}]}
