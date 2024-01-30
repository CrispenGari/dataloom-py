class TestCreatingTablePG:
    def test_2_pk_error(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model
        from orm.keys import password, database, user
        import pytest

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class Users(Model):
            _id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            db.sync([Users], drop=True, force=True)

        assert (
            str(exc_info.value)
            == 'You have defined many field as primary keys which is not allowed. Fields ("_id", "id") are primary keys.'
        )
        conn.close()

    def test_no_pk_error(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model
        from orm.keys import password, database, user
        import pytest

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class Users(Model):
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        with pytest.raises(Exception) as exc_info:
            db.sync([Users], drop=True, force=True)

        assert str(exc_info.value) == "Your table does not have a primary key column."
        conn.close()

    def test_table_name(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model
        from orm.keys import database, password, user

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class Todos(Model):
            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)

        class User(Model):
            __tablename__ = "users"
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        assert User._get_name() == "users"
        assert Todos._get_name() == "todos"
        conn.close()

    def test_connect_sync(self):
        from orm.db import Database
        from orm.keys import password, database, user
        from orm.model.model import Model
        from orm.model.column import Column

        class User(Model):
            __tablename__ = "users"
            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)

        class Post(Model):
            __tablename__ = "posts"

            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            title = Column(type="text", nullable=False, default="Hello there!!")

        db = Database(database, password=password, user=user)
        conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)

        assert len(tables) == 2
        assert conn.status == 1
        assert tables == ["users", "posts"]

        conn.close()

    def test_syncing_tables(self):
        from orm.db import Database
        from orm.keys import password, database, user
        from orm.model.model import Model
        from orm.model.column import Column

        class User(Model):
            __tablename__ = "users"
            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)

        class Post(Model):
            __tablename__ = "posts"

            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            title = Column(type="text", nullable=False, default="Hello there!!")

        db = Database(database, password=password, user=user)
        conn = db.connect()
        tables = db.sync([User, Post], drop=True, force=True)
        assert len(tables) == 2
        assert tables == ["users", "posts"]
        conn.close()
