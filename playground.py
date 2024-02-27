from dataloom import (
    Loom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    Filter,
    ColumnValue,
    Include,
    Order,
    Group,
    Having,
)


from dataloom.decorators import initialize
import json, time
from typing import Optional
from dataclasses import dataclass

sqlite_loom = Loom(
    connection_uri="sqlite://hello/database.db",
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)


pg_loom = Loom(
    connection_uri="postgresql://postgres:root@localhost:5432/hi",
    dialect="postgres",
    sql_logger="console",
)

mysql_loom = Loom(
    connection_uri="mysql://root:root@localhost:3306/hi",
    dialect="mysql",
    sql_logger="console",
)


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


conn, tables = mysql_loom.connect_and_sync(
    [Student, Course, StudentCourses], force=True
)

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
    filters=Filter(
        column="courseId", operator="in", value=[list(i.values())[0] for i in c]
    ),
    select=["id", "name"],
)

alice = {**s, "courses": courses}
print(courses)

# alice = mysql_loom.find_by_pk(
#     Student,
#     pk=stud1,
#     select=["id", "name"],
#     include=Include(
#         model=Course, junction_table=StudentCourses, alias="courses", has="many"
#     ),
# )

# print(alice)


# english = mysql_loom.find_by_pk(
#     Course,
#     pk=engId,
#     select=["id", "name"],
#     include=Include(
#         model=Student, junction_table=StudentCourses, alias="students", has="many"
#     ),
# )

# print(english)
