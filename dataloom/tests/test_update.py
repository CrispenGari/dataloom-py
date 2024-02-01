class TestDeletingOnPG:
    def test_update_by_pk_single_fn(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import (
            Model,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import password, database, user
        import time, pytest

        db = Database(database, password=password, user=user)

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        db.connect_and_sync([User], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = db.create(user)
        time.sleep(0.2)
        res_1 = db.update_by_pk(User, 1, {"name": "Tinashe Gari"})
        me = db.find_by_pk(User, userId)
        assert res_1 == 1
        assert me.createdAt != me.updatedAt
        with pytest.raises(Exception) as exc_info:
            db.update_by_pk(User, 1, {"haha": "Gari"})
        assert exc_info.value.pgcode == "42703"
        with pytest.raises(Exception) as exc_info:
            db.update_by_pk(User, 1, {"id": "Gari"})
        assert exc_info.value.pgcode == "25P02"

    def test_update_one_fn(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import (
            Model,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import password, database, user
        import time, pytest

        db = Database(database, password=password, user=user)

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        db.connect_and_sync([User], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = db.create(user)
        time.sleep(0.2)
        res_1 = db.update_one(User, {"name": "Crispen"}, {"name": "Tinashe Gari"})
        me = db.find_by_pk(User, userId)
        assert res_1 == 1
        assert me.createdAt != me.updatedAt
        with pytest.raises(Exception) as exc_info:
            db.update_one(User, {"name": "Crispen"}, {"haha": "Gari"})
        assert exc_info.value.pgcode == "42703"
        with pytest.raises(Exception) as exc_info:
            db.update_one(User, {"name": "HH"}, {"name": "Gari"})
        assert exc_info.value.pgcode == "25P02"

    def test_update_bulk_fn(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import (
            Model,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import password, database, user
        import time, pytest

        db = Database(database, password=password, user=user)

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=False, length=255)

            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        db.connect_and_sync([User], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        db.create_bulk([user for u in range(4)])
        res_1 = db.update_bulk(User, {"name": "Crispen"}, {"name": "Tinashe Gari"})
        assert res_1 == 4

        with pytest.raises(Exception) as exc_info:
            db.update_bulk(User, {"name": "Crispen"}, {"haha": "Gari"})
        assert exc_info.value.pgcode == "42703"
        with pytest.raises(Exception) as exc_info:
            db.update_bulk(User, {"name": "HH"}, {"name": "Gari"})
        assert exc_info.value.pgcode == "25P02"
