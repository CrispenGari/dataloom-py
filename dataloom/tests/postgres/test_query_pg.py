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
        )
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

            @property
            def to_dict(self):
                return {
                    "id": self.id,
                    "name": self.name,
                    "username": self.username,
                }

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
        _ = pg_loom.insert_one(user)
        me = pg_loom.find_by_pk(User, 1).to_dict
        her = pg_loom.find_by_pk(User, 2)

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
        )
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

            @property
            def to_dict(self):
                return {
                    "id": self.id,
                    "name": self.name,
                    "username": self.username,
                }

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

            @property
            def to_dict(self):
                return {
                    "id": self.id,
                    "name": self.name,
                    "username": self.username,
                }

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

        with pytest.raises(UnknownColumnException) as exc_info:
            one_4 = pg_loom.find_one(
                User, {"location": "Crispen", "username": "@miller"}
            )
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert one_0 is None
        assert one_3 is None
        assert one_1.to_dict == {"id": 1, "name": "Bob", "username": "@miller"}
        assert one_2.to_dict == {"id": 1, "name": "Bob", "username": "@miller"}
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

            @property
            def to_dict(self):
                return {
                    "id": self.id,
                    "name": self.name,
                    "username": self.username,
                }

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
        assert [u.to_dict for u in users] == [
            {"id": 1, "name": "Bob", "username": "@miller"}
        ]
        assert [u.to_dict for u in many_0] == []
        assert [u.to_dict for u in many_3] == []
        assert [u.to_dict for u in many_1] == [
            {"id": 1, "name": "Bob", "username": "@miller"}
        ]
        assert [u.to_dict for u in many_2] == []
        assert [u.to_dict for u in many_4] == [
            {"id": 1, "name": "Bob", "username": "@miller"}
        ]

        conn.close()
