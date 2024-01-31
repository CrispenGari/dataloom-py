class TestConnectionPG:
    def test_connect(self):
        from orm.db import Database
        from orm.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()
        assert conn.status == 1
        conn.close()

    def test_connect_sync(self):
        from orm.db import Database
        from orm.keys import password, database, user
        from orm.model.model import Model
        from orm.model.column import Column, PrimaryKeyColumn

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)

        class Post(Model):
            __tablename__ = "posts"

            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")

        db = Database(database, password=password, user=user)
        conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)

        assert len(tables) == 2
        assert conn.status == 1
        assert tables == ["users", "posts"]

        conn.close()
