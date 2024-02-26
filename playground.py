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


class Employee(Model):
    __tablename__: TableColumn = TableColumn(name="employees")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    supervisorId = ForeignKeyColumn(
        "Employee", maps_to="1-1", type="int", required=False
    )


class Employee(Model):
    __tablename__: TableColumn = TableColumn(name="employees")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    supervisorId = ForeignKeyColumn(
        "Employee", maps_to="1-1", type="int", required=False
    )


class Course(Model):
    __tablename__: TableColumn = TableColumn(name="courses")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")


class Student(Model):
    __tablename__: TableColumn = TableColumn(name="students")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")


# the only table that is allowed to have no primary key is the one that maps n-n and must have 2 foreign key columns


class StudentCourses(Model):
    __tablename__: TableColumn = TableColumn(name="students_courses")
    studentId = ForeignKeyColumn(table=Student, type="int")
    courseId = ForeignKeyColumn(table=Course, type="int")


"""
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

"""

"""
INSERT INTO employees (id, name, supervisor_id) VALUES
(1, 'John Doe', NULL),  -- John Doe doesn't have a supervisor
(2, 'Jane Smith', 1),    -- Jane Smith's supervisor is John Doe
(3, 'Michael Johnson', 1); -- Michael Johnson's supervisor is also John Doe
"""


conn, tables = sqlite_loom.connect_and_sync(
    [Student, Course, StudentCourses], alter=True
)


# userId = mysql_loom.insert_one(
#     instance=User,
#     values=ColumnValue(name="username", value="@miller"),
# )

# for title in ["Hey", "Hello", "What are you doing", "Coding"]:
#     mysql_loom.insert_one(
#         instance=Post,
#         values=[
#             ColumnValue(name="userId", value=userId),
#             ColumnValue(name="title", value=title),
#         ],
#     )
