class TestCreatingTableMysql:
    def test_2_pk_error(self):
        from dataloom import Column, PrimaryKeyColumn, Loom, TableColumn, Model
        import pytest
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn = mysql_loom.connect()

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            _id = PrimaryKeyColumn(type="int", auto_increment=True)
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            _ = mysql_loom.sync([User], drop=True, force=True)
        assert (
            str(exc_info.value)
            == "You have defined many field as primary keys which is not allowed. Fields (`_id`, `id`) are primary keys."
        )
        conn.close()

    def test_no_pk_error(self):
        import pytest
        from dataloom import Model, Loom, Column, TableColumn
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn = mysql_loom.connect()

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            _ = mysql_loom.sync([User], drop=True, force=True)
        assert (
            str(exc_info.value)
            == "Your table 'users' does not have a primary key column and it is not a reference table."
        )
        conn.close()

    def test_table_name(self):
        from dataloom import Model, Loom, Column, PrimaryKeyColumn, TableColumn
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn = mysql_loom.connect()

        class Posts(Model):
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        assert User._get_table_name() == "users"
        assert Posts._get_table_name() == "posts"
        conn.close()

    def test_connect_sync(self):
        from dataloom import Loom, Model, TableColumn, Column, PrimaryKeyColumn
        from dataloom.keys import MySQLConfig

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", nullable=False, auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")

            id = PrimaryKeyColumn(type="int", nullable=False, auto_increment=True)
            title = Column(type="text", nullable=False)

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn, tables = mysql_loom.connect_and_sync([User, Post], drop=True, force=True)
        assert len(tables) >= 2
        assert "users" in tables and "posts" in tables

        conn.close()

    def test_syncing_tables(self):
        from dataloom import Model, Loom, Column, PrimaryKeyColumn, TableColumn
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn = mysql_loom.connect()

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        tables = mysql_loom.sync([User, Post], drop=True, force=True)
        assert len(tables) >= 2
        assert "users" in tables and "posts" in tables
        conn.close()

    def test_create_self_relations_table(self):
        from dataloom import (
            Loom,
            Model,
            TableColumn,
            Column,
            PrimaryKeyColumn,
            ForeignKeyColumn,
        )
        from dataloom.exceptions import InvalidReferenceNameException
        from dataloom.keys import MySQLConfig
        import pytest

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        with pytest.raises(InvalidReferenceNameException) as info:

            class Employee(Model):
                __tablename__: TableColumn = TableColumn(name="employees")
                id = PrimaryKeyColumn(type="int", auto_increment=True)
                name = Column(type="text", nullable=False, default="Bob")
                supervisorId = ForeignKeyColumn(
                    "Employees", maps_to="1-1", type="int", required=False
                )

            conn, tables = mysql_loom.connect_and_sync(
                [Employee], drop=True, force=True
            )
            conn.close()
        assert (
            str(info.value)
            == "It seems like you are trying to create self relations on model 'Employee', however reference model is a string that does not match this model class definition signature."
        )

    def test_create_n2n_relations_tables(self):
        from dataloom import (
            Loom,
            Model,
            TableColumn,
            Column,
            PrimaryKeyColumn,
            ForeignKeyColumn,
            CreatedAtColumn,
        )
        from dataloom.exceptions import (
            IllegalColumnException,
            PkNotDefinedException,
            TooManyFkException,
        )
        from dataloom.keys import MySQLConfig
        import pytest

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class Course(Model):
            __tablename__: TableColumn = TableColumn(name="courses")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")

        class Student(Model):
            __tablename__: TableColumn = TableColumn(name="students")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")

        with pytest.raises(PkNotDefinedException) as info:

            class StudentCourses(Model):
                __tablename__: TableColumn = TableColumn(name="students_courses")
                studentId = ForeignKeyColumn(table=Student, type="int")

            conn, tables = mysql_loom.connect_and_sync(
                [Student, Course, StudentCourses], drop=True, force=True
            )
            conn.close()
        assert (
            str(info.value)
            == "Your table 'students_courses' does not have a primary key column and it is not a reference table."
        )

        with pytest.raises(TooManyFkException) as info:

            class StudentCourses(Model):
                __tablename__: TableColumn = TableColumn(name="students_courses")
                studentId = ForeignKeyColumn(table=Student, type="int")
                courseId = ForeignKeyColumn(table=Course, type="int")
                coursed = ForeignKeyColumn(table=Course, type="int")

            conn, tables = mysql_loom.connect_and_sync(
                [Student, Course, StudentCourses], drop=True, force=True
            )
            conn.close()
        assert (
            str(info.value)
            == "Reference table 'students_courses' can not have more than 2 foreign keys."
        )
        with pytest.raises(IllegalColumnException) as info:

            class StudentCourses(Model):
                __tablename__: TableColumn = TableColumn(name="students_courses")
                studentId = ForeignKeyColumn(table=Student, type="int")
                courseId = ForeignKeyColumn(table=Course, type="int")
                id = PrimaryKeyColumn(type="int")

            conn, tables = mysql_loom.connect_and_sync(
                [Student, Course, StudentCourses], drop=True, force=True
            )
            conn.close()
        assert (
            str(info.value)
            == "Primary keys and columns can not be manually added in a reference table."
        )
        with pytest.raises(IllegalColumnException) as info:

            class StudentCourses(Model):
                __tablename__: TableColumn = TableColumn(name="students_courses")
                studentId = ForeignKeyColumn(table=Student, type="int")
                courseId = ForeignKeyColumn(table=Course, type="int")
                c = CreatedAtColumn()

            conn, tables = mysql_loom.connect_and_sync(
                [Student, Course, StudentCourses], drop=True, force=True
            )
            conn.close()
        assert (
            str(info.value)
            == "Created at and Updated at columns are not allowed in reference tables."
        )
