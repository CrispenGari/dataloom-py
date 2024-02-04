class TestDeletingOnPG:
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

        user = User(name="Crispen", username="heyy")
        userId = pg_loom.insert_one(user)
        affected_rows_1 = pg_loom.delete_by_pk(User, userId)
        affected_rows_2 = pg_loom.delete_by_pk(User, 89)
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
        pg_loom.insert_bulk(
            [
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="who"),
                User(name="Crispen", username="hi"),
            ]
        )
        pg_loom.delete_one(User, {"name": "Crispen"})
        rows_1 = pg_loom.find_many(User, {"name": "Crispen"})
        pg_loom.delete_one(User, {"name": "Crispen", "id": 9})
        rows_2 = pg_loom.find_many(User, {"name": "Crispen"})
        pg_loom.delete_one(User, {"name": "Crispen", "id": 2})
        rows_3 = pg_loom.find_many(User, {"name": "Crispen"})

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.delete_bulk(User, {"location": "Crispen", "username": "@miller"})
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
        pg_loom.insert_bulk(
            [
                User(name="Crispen", username="hi"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="hie"),
            ]
        )
        pg_loom.delete_bulk(User, {"name": "Crispen"})
        rows_1 = pg_loom.find_many(User, {"name": "Crispen"})
        pg_loom.insert_bulk(
            [
                User(name="Crispen", username="hi"),
                User(name="Crispen", username="heyy"),
                User(name="Crispen", username="hie"),
            ]
        )
        pg_loom.delete_bulk(User, {"name": "Crispen", "id": 99})
        rows_2 = pg_loom.find_many(User, {"name": "Crispen"})
        pg_loom.delete_bulk(User, {"name": "Crispen", "id": 5})
        rows_3 = pg_loom.find_many(User, {"name": "Crispen"})

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.delete_bulk(User, {"location": "Crispen", "username": "@miller"})
        assert str(exc_info.value) == "Table users does not have column 'location'."

        assert len(rows_1) == 0
        assert len(rows_2) == 3
        assert len(rows_3) == 2
        conn.close()
