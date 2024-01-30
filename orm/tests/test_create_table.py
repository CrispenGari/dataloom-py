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
            == "You have defined many field as primary keys which is not allowed. Fields (_id, id) are primary keys."
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
