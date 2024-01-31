class TestDeletingOnPG:
    def test_delete_by_pk_single_fn(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model, PrimaryKeyColumn
        from orm.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        db.sync([User], drop=True, force=True)

        user = User(name="Crispen", username="heyy")
        userId = db.commit(user)
        affected_rows_1 = db.delete_by_pk(User, userId)
        affected_rows_2 = db.delete_by_pk(User, 89)
        assert affected_rows_1 == 1
        assert affected_rows_2 == 0
        conn.close()

    def test_delete_one_fn(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model, PrimaryKeyColumn
        from orm.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=False, length=255)

        db.sync([User], drop=True, force=True)

        db.commit_bulk(
            [
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="heyy"),
            ]
        )
        affected_rows_1 = db.delete_one(User, {"name": "Crispen"})
        affected_rows_2 = db.delete_one(User, {"name": "Crispen", "id": 9})
        affected_rows_3 = db.delete_one(User, {"name": "Crispen", "id": 2})

        assert affected_rows_1 == 3
        assert affected_rows_3 == 0
        assert affected_rows_2 == 0
        conn.close()

    def test_delete_bulk_fn(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model, PrimaryKeyColumn
        from orm.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=False, length=255)

        db.sync([User], drop=True, force=True)

        db.commit_bulk(
            [
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="heyy"),
            ]
        )
        affected_rows_1 = db.delete_one(User, {"name": "Crispen"})
        affected_rows_2 = db.delete_one(User, {"name": "Crispen", "id": 9})
        affected_rows_3 = db.delete_one(User, {"name": "Crispen", "id": 2})

        assert affected_rows_1 == 3
        assert affected_rows_3 == 0
        assert affected_rows_2 == 0
        conn.close()
