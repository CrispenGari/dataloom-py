class TestUtilsFunctionsPG:
    def test_util_fns(self):
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
            Filter,
        )

        from typing import Optional

        from dataloom.keys import PgConfig

        pg_loom = Loom(
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
        userId = pg_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            pg_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        count = pg_loom.count(
            instance=Post,
            filters=Filter(
                column="id",
                operator="between",
                value=[1, 7],
            ),
            column="id",
            limit=3,
            offset=0,
            distinct=True,
        )
        assert count == 3

        avg = pg_loom.avg(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert avg == 2.5
        sum = pg_loom.sum(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert sum == 10
        min = pg_loom.min(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert min == 1
        max = pg_loom.max(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert max == 4
        conn.close()
