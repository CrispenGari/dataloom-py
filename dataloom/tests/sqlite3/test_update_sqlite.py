class TestUpdateOnMySQL:
    def test_update_by_pk_fn(self):
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

        from typing import Optional
        import time, pytest

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = sqlite_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = sqlite_loom.insert_bulk([post for i in range(5)])
        time.sleep(0.05)
        res_1 = sqlite_loom.update_by_pk(User, userId)
        res_2 = sqlite_loom.update_by_pk(User, 10)
        me = sqlite_loom.find_by_pk(User, userId)

        assert me.createdAt != me.updatedAt
        assert res_1 == 1
        assert res_2 == 0
        conn.close()

    def test_update_one_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            InvalidFiltersForTableColumnException,
            InvalidColumnValuesException,
        )

        from typing import Optional
        import time, pytest

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = sqlite_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = sqlite_loom.insert_bulk([post for i in range(5)])
        time.sleep(0.05)
        res_1 = sqlite_loom.update_one(Post, {"userId": userId}, {"title": "John"})
        res_2 = sqlite_loom.update_one(Post, {"userId": 2}, {"title": "John"})

        post = sqlite_loom.find_by_pk(Post, 1)

        with pytest.raises(InvalidFiltersForTableColumnException) as exc_info:
            sqlite_loom.update_one(Post, {"wrong_key": "@miller"}, {"userId": 3})

        assert (
            str(exc_info.value)
            == "There are no column filter passed to perform the UPDATE ONE operation or you passed filters that does not match columns in table 'posts'."
        )

        with pytest.raises(InvalidColumnValuesException) as exc_info:
            sqlite_loom.update_one(Post, {"userId": userId}, values={"loca": "miller"})
        assert (
            str(exc_info.value)
            == "There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table 'posts'."
        )

        post.title == "John"
        assert res_1 == 1
        assert res_2 == 0
        conn.close()

    def test_update_bulk_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            InvalidFiltersForTableColumnException,
            InvalidColumnValuesException,
        )

        from typing import Optional
        import time, pytest

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)

        user = User(username="@miller")
        userId = sqlite_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        _ = sqlite_loom.insert_bulk([post for i in range(5)])
        time.sleep(0.05)
        res_1 = sqlite_loom.update_bulk(Post, {"userId": userId}, {"title": "John"})
        res_2 = sqlite_loom.update_bulk(Post, {"userId": 2}, {"title": "John"})

        post = sqlite_loom.find_by_pk(Post, 1)

        with pytest.raises(InvalidFiltersForTableColumnException) as exc_info:
            sqlite_loom.update_bulk(Post, {"wrong_key": "@miller"}, {"userId": 3})

        assert (
            str(exc_info.value)
            == "There are no column filter passed to perform the UPDATE ONE operation or you passed filters that does not match columns in table 'posts'."
        )

        with pytest.raises(InvalidColumnValuesException) as exc_info:
            sqlite_loom.update_bulk(Post, {"userId": userId}, values={"loca": "miller"})
        assert (
            str(exc_info.value)
            == "There are no new values passed to perform the UPDATE ONE operation, or you don't have the CreatedAtColumn field in your table 'posts'."
        )

        post.title == "John"
        assert res_1 == 5
        assert res_2 == 0
        conn.close()
