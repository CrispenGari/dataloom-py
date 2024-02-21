class TestUpdateOnSQLite:
    def test_update_by_pk_fn(self):
        import time
        from typing import Optional

        from dataloom import (
            Column,
            CreatedAtColumn,
            Loom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            ColumnValue,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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
        userId = sqlite_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )
        post = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, values=[post for i in range(5)])
        time.sleep(0.05)
        res_1 = sqlite_loom.update_by_pk(
            User, userId, ColumnValue(name="username", value="Gari")
        )
        res_2 = sqlite_loom.update_by_pk(
            User, 10, ColumnValue(name="username", value="Gari")
        )
        me = sqlite_loom.find_by_pk(User, userId)

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
            Loom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            Filter,
            ColumnValue,
        )
        from dataloom.exceptions import UnknownColumnException

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        userId = sqlite_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )
        post = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, values=[post for i in range(5)])
        time.sleep(0.05)
        res_1 = sqlite_loom.update_one(
            User,
            filters=Filter(column="username", value="@miller"),
            values=ColumnValue(name="name", value="Jonh"),
        )
        res_2 = sqlite_loom.update_one(
            User,
            Filter(column="username", value="miller"),
            values=ColumnValue(name="name", value="Jonh"),
        )
        me = sqlite_loom.find_by_pk(User, userId)

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.update_one(
                Post,
                Filter(column="wrong_key", value="@miller"),
                values=ColumnValue(name="id", value=3),
            )
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."
        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.update_one(
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
            Loom,
            ForeignKeyColumn,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            Filter,
            ColumnValue,
        )
        from dataloom.exceptions import UnknownColumnException

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        userId = sqlite_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )
        post = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        _ = sqlite_loom.insert_bulk(Post, values=[post for i in range(5)])
        res_1 = sqlite_loom.update_bulk(
            Post,
            Filter(column="userId", value=userId),
            ColumnValue(name="title", value="John"),
        )
        res_2 = sqlite_loom.update_bulk(
            Post, Filter(column="id", value=10), ColumnValue(name="title", value="John")
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.update_one(
                Post,
                Filter(column="wrong_key", value="@miller"),
                ColumnValue(name="userId", value=3),
            )
        assert str(exc_info.value) == "Table posts does not have column 'wrong_key'."

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.update_one(
                Post,
                Filter(column="userId", value=userId),
                ColumnValue(name="loca", value="miller"),
            )
        assert str(exc_info.value) == "Table posts does not have column 'loca'."

        assert res_1 == 5
        assert res_2 == 0
        conn.close()

    def test_increment_fn(self):
        from typing import Optional
        import pytest
        from dataloom import (
            Column,
            CreatedAtColumn,
            Loom,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            Filter,
            ColumnValue,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)
            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        conn, _ = sqlite_loom.connect_and_sync([User], drop=True, force=True)

        userId = sqlite_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )

        affected_rows = sqlite_loom.increment(
            User,
            filters=Filter(column="id", value=1),
            column=ColumnValue(name="tokenVersion", value=3),
        )
        assert affected_rows == 1

        affected_rows = sqlite_loom.increment(
            User,
            filters=Filter(column="id", value=2),
            column=ColumnValue(name="tokenVersion", value=3),
        )
        assert affected_rows == 0

        me = sqlite_loom.find_by_pk(User, userId, select=["tokenVersion"])
        assert me["tokenVersion"] == 3

        with pytest.raises(Exception) as exc_info:
            sqlite_loom.increment(
                User,
                filters=Filter(column="id", value=2),
                column=ColumnValue(name="tokenVersion", value="3"),
            )
        assert (
            str(exc_info.value)
            == "The increment operation only works with integer and float values."
        )
        conn.close()

    def test_decrement_fn(self):
        from typing import Optional
        import pytest
        from dataloom import (
            Column,
            CreatedAtColumn,
            Loom,
            Model,
            PrimaryKeyColumn,
            TableColumn,
            UpdatedAtColumn,
            Filter,
            ColumnValue,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)
            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        conn, _ = sqlite_loom.connect_and_sync([User], drop=True, force=True)

        userId = sqlite_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )

        affected_rows = sqlite_loom.decrement(
            User,
            filters=Filter(column="id", value=1),
            column=ColumnValue(name="tokenVersion", value=3),
        )
        assert affected_rows == 1

        affected_rows = sqlite_loom.decrement(
            User,
            filters=Filter(column="id", value=2),
            column=ColumnValue(name="tokenVersion", value=3),
        )
        assert affected_rows == 0

        me = sqlite_loom.find_by_pk(User, userId, select=["tokenVersion"])
        assert me["tokenVersion"] == -3

        with pytest.raises(Exception) as exc_info:
            sqlite_loom.decrement(
                User,
                filters=Filter(column="id", value=2),
                column=ColumnValue(name="tokenVersion", value="3"),
            )
        assert (
            str(exc_info.value)
            == "The decrement operation only works with integer and float values."
        )
        conn.close()
