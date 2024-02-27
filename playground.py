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


conn, tables = pg_loom.connect_and_sync(
    [Student, Course, StudentCourses, Employee], force=True
)


empId = pg_loom.insert_one(
    instance=Employee, values=ColumnValue(name="name", value="John Doe")
)

rows = pg_loom.insert_bulk(
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


emp_and_sup = pg_loom.find_by_pk(
    instance=Employee,
    pk=1,
    select=["id", "name", "supervisorId"],
    include=Include(
        model=Employee,
        has="one",
        select=["id", "name"],
        alias="supervisor",
    ),
)

print(emp_and_sup)
