class TestQueryingSQLite:
    def test_find_by_pk_fn(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
        )
        import pytest
        from typing import Optional
        from dataloom.exceptions import UnknownColumnException

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = sqlite_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, [values for i in range(5)])
        me = sqlite_loom.find_by_pk(User, 1)
        her = sqlite_loom.find_by_pk(User, 2)

        posts = sqlite_loom.find_by_pk(Post, 1, select=["id", "completed"])
        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_by_pk(Post, 1, select=["id", "location"])
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
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
        )
        from typing import Optional
        from dataloom.exceptions import UnknownColumnException
        import pytest

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = sqlite_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, [values for i in range(5)])
        users = sqlite_loom.find_all(User)
        posts = sqlite_loom.find_all(Post)
        paginated = sqlite_loom.find_all(
            Post, select=["id", "completed"], limit=3, offset=3
        )
        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_all(Post, select=["id", "location"], limit=3, offset=3)
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
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            Filter,
            ColumnValue,
        )
        from typing import Optional
        import pytest
        from dataloom.exceptions import UnknownColumnException

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = sqlite_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, [values for i in range(5)])

        one_0 = sqlite_loom.find_one(User, filters=Filter(column="id", value=5))
        one_1 = sqlite_loom.find_one(User, filters=Filter(column="id", value=1))
        one_2 = sqlite_loom.find_one(
            User,
            filters=[Filter(column="name", value="Bob"), Filter(column="id", value=1)],
        )
        one_3 = sqlite_loom.find_one(
            User,
            filters=[
                Filter(column="id", value=5),
                Filter(column="username", value="@miller"),
            ],
        )
        one_4 = sqlite_loom.find_one(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="username", value="@miller"),
            ],
        )

        posts = sqlite_loom.find_one(Post, select=["id", "completed"])
        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_one(Post, select=["id", "location"])
        assert (
            str(exc_info.value)
            == 'The table "posts" does not have a column "location".'
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            one_4 = sqlite_loom.find_one(
                User,
                filters=[
                    Filter(column="location", value="Crispen"),
                    Filter(column="username", value="@miller"),
                ],
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
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            Filter,
            ColumnValue,
        )
        from typing import Optional
        from dataloom.exceptions import UnknownColumnException
        import pytest

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = sqlite_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        rows = sqlite_loom.insert_bulk(Post, [values for i in range(5)])
        posts = sqlite_loom.find_many(
            Post,
            filters=[Filter(column="id", value=1), Filter(column="userId", value=1)],
        )
        users = sqlite_loom.find_many(User)
        many_0 = sqlite_loom.find_many(User, filters=Filter(column="id", value=5))
        many_1 = sqlite_loom.find_many(User, filters=Filter(column="id", value=1))
        many_2 = sqlite_loom.find_many(
            User,
            filters=[
                Filter(column="id", value=1),
                Filter(column="name", value="Crispen"),
            ],
        )
        many_3 = sqlite_loom.find_many(
            User,
            filters=[
                Filter(column="id", value=5),
                Filter(column="username", value="@miller"),
            ],
        )
        many_4 = sqlite_loom.find_many(
            User,
            filters=[
                Filter(column="name", value="Bob"),
                Filter(column="username", value="@miller"),
            ],
        )

        paginated = sqlite_loom.find_many(
            Post,
            Filter(column="userId", value=1),
            select=["id", "completed"],
            limit=3,
            offset=3,
        )
        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_many(
                Post,
                Filter(column="id", value=1),
                select=["id", "location"],
                limit=3,
                offset=3,
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
            sqlite_loom.find_many(
                User,
                filters=[
                    Filter(column="username", value="@miller"),
                    Filter(column="location", value="Crispen"),
                ],
            )
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert len(users) == 1
        assert len(posts) == 1
        assert len(many_0) == 0
        assert len(many_1) == 1
        assert len(many_2) == 0
        assert len(many_3) == 0
        assert len(many_4) == 1
        assert rows == len(sqlite_loom.find_all(Post))
        assert [u for u in users] == [{"id": 1, "name": "Bob", "username": "@miller"}]
        assert [u for u in many_0] == []
        assert [u for u in many_3] == []
        assert [u for u in many_1] == [{"id": 1, "name": "Bob", "username": "@miller"}]
        assert [u for u in many_2] == []
        assert [u for u in many_4] == [{"id": 1, "name": "Bob", "username": "@miller"}]

        conn.close()
