class TestDeletingOnSqlite:
    def test_delete_by_pk_fn(self):
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Dataloom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
        )

        from typing import Optional

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

        user = User(name="Crispen", username="heyy")
        userId = sqlite_loom.insert_one(user)
        affected_rows_1 = sqlite_loom.delete_by_pk(User, userId)
        affected_rows_2 = sqlite_loom.delete_by_pk(User, 89)
        assert affected_rows_1 == 1
        assert affected_rows_2 == 0
        conn.close()

    def test_delete_one_fn(self):
        import pytest
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Dataloom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            UnknownColumnException,
            Filter,
        )

        from typing import Optional

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
        sqlite_loom.insert_bulk(
            [
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="who"),
                User(name="Crispen", username="hi"),
            ]
        )
        sqlite_loom.delete_one(User, filters=[Filter(column="name", value="Crispen")])
        rows_1 = sqlite_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )
        sqlite_loom.delete_one(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=9),
            ],
        )
        rows_2 = sqlite_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )
        sqlite_loom.delete_one(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=2),
            ],
        )
        rows_3 = sqlite_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.delete_bulk(
                User,
                filters=[
                    Filter(column="location", value="Crispen"),
                    Filter(column="username", value="@miller"),
                ],
            )
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert len(rows_1) == 2
        assert len(rows_2) == 2
        assert len(rows_3) == 1
        conn.close()

    def test_delete_bulk_fn(self):
        import pytest
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Dataloom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            UnknownColumnException,
            Filter,
        )

        from typing import Optional

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
        sqlite_loom.insert_bulk(
            [
                User(name="Crispen", username="hi"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="hie"),
            ]
        )
        sqlite_loom.delete_bulk(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        rows_1 = sqlite_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        sqlite_loom.insert_bulk(
            [
                User(name="Crispen", username="hi"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="hie"),
            ]
        )
        sqlite_loom.delete_bulk(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=99),
            ],
        )
        rows_2 = sqlite_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        sqlite_loom.delete_bulk(
            User,
            filters=[
                Filter(column="name", value="Crispen", operator="eq"),
                Filter(column="id", value=5, operator="eq"),
            ],
        )
        rows_3 = sqlite_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.delete_bulk(
                User,
                filters=[
                    Filter(column="location", value="Crispen"),
                    Filter(column="username", value="@miller"),
                ],
            )
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert len(rows_1) == 0
        assert len(rows_2) == 3
        assert len(rows_3) == 2
        conn.close()
