class TestQueryingPG:
    def test_find_by_pk_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UnknownColumnException,
        )
        import pytest
        from dataloom.keys import PgConfig
        from typing import Optional

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
        me = pg_loom.find_by_pk(User, 1)
        her = pg_loom.find_by_pk(User, 2)

        posts = pg_loom.find_by_pk(Post, 1, select=["id", "completed"])
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_by_pk(Post, 1, select=["id", "location"])
        assert (
            str(exc_info.value)
            == 'The table "posts" does not have a column "location".'
        )
        assert len(posts) == 2
        assert posts == {"id": 1, "completed": 0}

        assert her is None
        assert me == {"id": 1, "name": "Bob", "username": "@miller"}
        conn.close()

    def test_find_all_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UnknownColumnException,
        )
        from dataloom.keys import PgConfig
        from typing import Optional
        import pytest

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
        users = pg_loom.find_all(User)
        posts = pg_loom.find_all(Post)
        paginated = pg_loom.find_all(
            Post, select=["id", "completed"], limit=3, offset=3
        )
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_all(Post, select=["id", "location"], limit=3, offset=3)
        assert (
            str(exc_info.value)
            == 'The table "posts" does not have a column "location".'
        )
        assert len(paginated) == 2
        assert paginated == [
            {"id": 4, "completed": False},
            {"id": 5, "completed": False},
        ]

        assert len(users) == 1
        assert len(posts) == 5

        assert True
        conn.close()

    def test_find_one_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UnknownColumnException,
        )
        from dataloom.keys import PgConfig
        from typing import Optional
        import pytest

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

        one_0 = pg_loom.find_one(User, {"id": 5})
        one_1 = pg_loom.find_one(User, {"id": 1})
        one_2 = pg_loom.find_one(User, {"id": 1, "name": "Bob"})
        one_3 = pg_loom.find_one(User, {"id": 5, "username": "@miller"})
        one_4 = pg_loom.find_one(User, {"name": "Crispen", "username": "@miller"})

        posts = pg_loom.find_one(Post, select=["id", "completed"])
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_one(Post, select=["id", "location"])
        assert (
            str(exc_info.value)
            == 'The table "posts" does not have a column "location".'
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            one_4 = pg_loom.find_one(
                User, {"location": "Crispen", "username": "@miller"}
            )
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert one_0 is None
        assert len(posts) == 2
        assert posts == {"id": 1, "completed": False}
        assert one_3 is None
        assert one_1 == {"id": 1, "name": "Bob", "username": "@miller"}
        assert one_2 == {"id": 1, "name": "Bob", "username": "@miller"}
        assert one_4 is None

        conn.close()

    def test_find_many(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UnknownColumnException,
        )
        from dataloom.keys import PgConfig
        from typing import Optional
        import pytest

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
        rows = pg_loom.insert_bulk([post for i in range(5)])
        posts = pg_loom.find_many(Post, {"id": 1, "userId": 1})
        users = pg_loom.find_many(User)
        many_0 = pg_loom.find_many(User, {"id": 5})
        many_1 = pg_loom.find_many(User, {"id": 1})
        many_2 = pg_loom.find_many(User, {"id": 1, "name": "Crispen"})
        many_3 = pg_loom.find_many(User, {"id": 5, "username": "@miller"})
        many_4 = pg_loom.find_many(User, {"name": "Bob", "username": "@miller"})

        paginated = pg_loom.find_many(
            Post, {"userId": 1}, select=["id", "completed"], limit=3, offset=3
        )
        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_many(
                Post, {"userId": 1}, select=["id", "location"], limit=3, offset=3
            )
        assert (
            str(exc_info.value)
            == 'The table "posts" does not have a column "location".'
        )
        assert len(paginated) == 2
        assert paginated == [
            {"id": 4, "completed": False},
            {"id": 5, "completed": False},
        ]

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_many(User, {"location": "Crispen", "username": "@miller"})
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert len(users) == 1
        assert len(posts) == 1
        assert len(many_0) == 0
        assert len(many_1) == 1
        assert len(many_2) == 0
        assert len(many_3) == 0
        assert len(many_4) == 1
        assert rows == len(pg_loom.find_all(Post))
        assert [u for u in users] == [{"id": 1, "name": "Bob", "username": "@miller"}]
        assert [u for u in many_0] == []
        assert [u for u in many_3] == []
        assert [u for u in many_1] == [{"id": 1, "name": "Bob", "username": "@miller"}]
        assert [u for u in many_2] == []
        assert [u for u in many_4] == [{"id": 1, "name": "Bob", "username": "@miller"}]

        conn.close()
