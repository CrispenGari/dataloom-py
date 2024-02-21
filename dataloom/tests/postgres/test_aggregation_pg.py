class TestAggregationLoadingOnPG:
    def test_find_many(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Filter,
            Group,
            Having,
        )
        import pytest
        from dataloom.exceptions import UnknownColumnException
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = pg_loom.connect_and_sync(
            [
                User,
                Post,
            ],
            drop=True,
            force=True,
        )
        userId = pg_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        for title in ["Hello", "Hello", "What are you doing", "Coding"]:
            pg_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_many(
                Post,
                select="title",
                filters=Filter(column="id", operator="gt", value=1),
                group=Group(
                    column="id",
                    function="MAX",
                    having=Having(column="id", operator="in", value=(2, 3, 4)),
                    return_aggregation_column=False,
                ),
            )

        assert (
            str(exc_info.value)
            == 'The column "id" was omitted in selection of records to be grouped.'
        )

        posts = pg_loom.find_many(
            Post,
            select="id",
            filters=Filter(column="id", operator="gt", value=1),
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=False,
            ),
        )

        assert sorted(posts, key=lambda d: d["id"]) == sorted(
            [{"id": 2}, {"id": 3}, {"id": 4}], key=lambda d: d["id"]
        )
        posts = pg_loom.find_many(
            Post,
            select="id",
            filters=Filter(column="id", operator="gt", value=1),
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=True,
            ),
        )
        assert sorted(posts, key=lambda d: d["id"]) == sorted(
            [
                {"id": 2, 'MAX("id")': 2},
                {"id": 3, 'MAX("id")': 3},
                {"id": 4, 'MAX("id")': 4},
            ],
            key=lambda d: d["id"],
        )
        conn.close()

    def test_find_all(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Group,
            Having,
        )
        import pytest
        from dataloom.exceptions import UnknownColumnException
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = pg_loom.connect_and_sync(
            [
                User,
                Post,
            ],
            drop=True,
            force=True,
        )
        userId = pg_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        for title in ["Hello", "Hello", "What are you doing", "Coding"]:
            pg_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.find_all(
                Post,
                select="title",
                group=Group(
                    column="id",
                    function="MAX",
                    having=Having(column="id", operator="in", value=(2, 3, 4)),
                    return_aggregation_column=False,
                ),
            )

        assert (
            str(exc_info.value)
            == 'The column "id" was omitted in selection of records to be grouped.'
        )

        posts = pg_loom.find_all(
            Post,
            select="id",
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=False,
            ),
        )

        assert sorted(posts, key=lambda d: d["id"]) == sorted(
            [{"id": 2}, {"id": 3}, {"id": 4}], key=lambda d: d["id"]
        )
        posts = pg_loom.find_all(
            Post,
            select="id",
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=True,
            ),
        )

        assert sorted(posts, key=lambda d: d["id"]) == sorted(
            [
                {"id": 2, 'MAX("id")': 2},
                {"id": 3, 'MAX("id")': 3},
                {"id": 4, 'MAX("id")': 4},
            ],
            key=lambda d: d["id"],
        )

        conn.close()
