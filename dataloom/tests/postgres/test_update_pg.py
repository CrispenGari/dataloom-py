class TestUpdateOnPG:
    def test_update_by_pk_fn(self):
        import time
        from typing import Optional

        from dataloom import (
            Column,
            CreatedAtColumn,
            Dataloom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            ColumnValue,
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
        res_1 = pg_loom.update_by_pk(
            User, userId, ColumnValue(name="username", value="Gari")
        )
        res_2 = pg_loom.update_by_pk(
            User, 10, ColumnValue(name="username", value="Gari")
        )
        me = pg_loom.find_by_pk(User, userId)

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
            Filter,
            ColumnValue,
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
        res_1 = pg_loom.update_one(
            User,
            filters=Filter(column="username", value="@miller"),
            values=ColumnValue(name="name", value="Jonh"),
        )
        res_2 = pg_loom.update_one(
            User,
            Filter(column="username", value="miller"),
            values=ColumnValue(name="name", value="Jonh"),
        )
        me = pg_loom.find_by_pk(User, userId)

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(
                Post,
                Filter(column="wrong_key", value="@miller"),
                values=ColumnValue(name="id", value=3),
            )
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(
                Post,
                Filter(column="userId", value=userId),
                values=ColumnValue(name="loca", value=3),
            )
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
            Filter,
            ColumnValue,
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
        res_1 = pg_loom.update_bulk(
            Post,
            Filter(column="userId", value=userId),
            ColumnValue(name="title", value="John"),
        )
        res_2 = pg_loom.update_bulk(
            Post, Filter(column="id", value=10), ColumnValue(name="title", value="John")
        )

        with pytest.raises(Exception) as exc_info:
            pg_loom.update_bulk(
                Post,
                Filter(column="userId", value=userId),
                ColumnValue(name="userId", value="Gari"),
            )
        assert exc_info.value.pgcode == "22P02"
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(
                Post,
                Filter(column="wrong_key", value="@miller"),
                ColumnValue(name="userId", value=3),
            )
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.update_one(
                Post,
                Filter(column="userId", value=userId),
                ColumnValue(name="loca", value="miller"),
            )
        assert str(exc_info.value) == "Table posts does not have column 'loca'."

        assert res_1 == 5
        assert res_2 == 0
        conn.close()
