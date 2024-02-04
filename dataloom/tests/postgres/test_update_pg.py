class TestUpdateOnPG:
    def test_update_by_pk_fn(self):
        import time
        from typing import Optional

        import pytest

        from dataloom import (
            Column,
            CreatedAtColumn,
            Dataloom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import PgConfig

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = pg_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = pg_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = pg_loom.insert_bulk([post for i in range(5)])
        time.sleep(0.05)
        res_1 = pg_loom.update_by_pk(User, userId)
        res_2 = pg_loom.update_by_pk(User, 10)
        me = pg_loom.find_by_pk(User, userId)

        with pytest.raises(Exception) as exc_info:
            pg_loom.update_by_pk(User, userId, {"id": "Gari"})
        assert exc_info.value.pgcode == "22P02"

        assert me["createdAt"] != me["updatedAt"]
        assert res_1 == 1
        assert res_2 == 0
        conn.close()

    def test_update_one_fn(self):
        import time
        from typing import Optional

        import pytest

        from dataloom import (
            Column,
            CreatedAtColumn,
            Dataloom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UnknownColumnException,
            UpdatedAtColumn,
        )
        from dataloom.keys import PgConfig

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = pg_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = pg_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = pg_loom.insert_bulk([post for i in range(5)])
        time.sleep(0.05)
        res_1 = pg_loom.update_one(User, {"username": "@miller"}, {"name": "John"})
        res_2 = pg_loom.update_one(User, {"username": "miller"}, {"name": "John"})
        me = pg_loom.find_by_pk(User, userId)

        with pytest.raises(Exception) as exc_info:
            pg_loom.update_one(User, {"username": "@miller"}, {"id": "Gari"})
        assert exc_info.value.pgcode == "22P02"
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(Post, {"wrong_key": "@miller"}, {"userId": 3})
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(Post, {"userId": userId}, values={"loca": "miller"})
        assert str(exc_info.value) == "Table posts does not have column 'loca'."

        assert me["createdAt"] != me["updatedAt"]
        assert res_1 == 1
        assert res_2 == 0
        conn.close()

    def test_update_bulk_fn(self):
        from typing import Optional

        import pytest

        from dataloom import (
            Column,
            CreatedAtColumn,
            Dataloom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UnknownColumnException,
            UpdatedAtColumn,
        )
        from dataloom.keys import PgConfig

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = pg_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = pg_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = pg_loom.insert_bulk([post for i in range(5)])
        res_1 = pg_loom.update_bulk(Post, {"userId": userId}, {"title": "John"})
        res_2 = pg_loom.update_bulk(Post, {"userId": 2}, {"title": "John"})

        with pytest.raises(Exception) as exc_info:
            pg_loom.update_bulk(Post, {"userId": userId}, {"userId": "Gari"})
        assert exc_info.value.pgcode == "22P02"
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(Post, {"wrong_key": "@miller"}, {"userId": 3})
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(Post, {"userId": userId}, values={"loca": "miller"})
        assert str(exc_info.value) == "Table posts does not have column 'loca'."

        assert res_1 == 5
        assert res_2 == 0
        conn.close()
