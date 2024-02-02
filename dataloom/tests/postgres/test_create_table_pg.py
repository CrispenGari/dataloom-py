class TestCreatingTablePG:
    def test_2_pk_error(self):
        from dataloom import Column, PrimaryKeyColumn, Dataloom, TableColumn, Model
        import pytest
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database="hi",
            password="root",
            user="postgres",
            logging=True,
        )
        conn = pg_loom.connect()

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            _id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            tables = pg_loom.sync([User], drop=True, force=True)

        assert (
            str(exc_info.value)
            == 'You have defined many field as primary keys which is not allowed. Fields ("_id", "id") are primary keys.'
        )
        conn.close()

    def test_no_pk_error(self):
        import pytest
        from dataloom import Model, Dataloom, Column, TableColumn
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database="hi",
            password="root",
            user="postgres",
            logging=True,
        )
        conn = pg_loom.connect()

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            tables = pg_loom.sync([User], drop=True, force=True)
        assert str(exc_info.value) == "Your table does not have a primary key column."
        conn.close()

    def test_table_name(self):
        from dataloom import Model, Dataloom, Column, PrimaryKeyColumn, TableColumn
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database="hi",
            password="root",
            user="postgres",
            logging=True,
        )
        conn = pg_loom.connect()

        class Posts(Model):
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        assert User._get_table_name() == "users"
        assert Posts._get_table_name() == "posts"
        conn.close()

    def test_connect_sync(self):
        from dataloom import Dataloom, Model, TableColumn, Column, PrimaryKeyColumn
        from typing import Optional

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")

            id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")

        pg_loom = Dataloom(
            dialect="postgres",
            database="hi",
            password="root",
            user="postgres",
            logging=True,
        )
        conn, tables = pg_loom.connect_and_sync([User, Post], drop=True, force=True)
        assert len(tables) == 2
        assert conn.status == 1
        assert sorted(tables) == sorted(["users", "posts"])

        conn.close()

    def test_syncing_tables(self):
        from dataloom import Model, Dataloom, Column, PrimaryKeyColumn, TableColumn
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database="hi",
            password="root",
            user="postgres",
            logging=True,
        )
        conn = pg_loom.connect()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        tables = pg_loom.sync([User, Post], drop=True, force=True)
        assert len(tables) == 2
        assert sorted(tables) == sorted(["users", "posts"])
        conn.close()
