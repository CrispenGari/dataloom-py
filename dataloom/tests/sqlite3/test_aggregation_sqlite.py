class TestAggregationLoadingOnSQLite:
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

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, tables = sqlite_loom.connect_and_sync(
            [
                User,
                Post,
            ],
            drop=True,
            force=True,
        )
        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        for title in ["Hello", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_many(
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

        posts = sqlite_loom.find_many(
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

        assert posts == [{"id": 2}, {"id": 3}, {"id": 4}]
        posts = sqlite_loom.find_many(
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

        assert posts == [
            {"id": 2, "MAX(`id`)": 2},
            {"id": 3, "MAX(`id`)": 3},
            {"id": 4, "MAX(`id`)": 4},
        ]

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

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, tables = sqlite_loom.connect_and_sync(
            [
                User,
                Post,
            ],
            drop=True,
            force=True,
        )
        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        for title in ["Hello", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        with pytest.raises(UnknownColumnException) as exc_info:
            sqlite_loom.find_all(
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

        posts = sqlite_loom.find_all(
            Post,
            select="id",
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=False,
            ),
        )

        assert posts == [{"id": 2}, {"id": 3}, {"id": 4}]
        posts = sqlite_loom.find_all(
            Post,
            select="id",
            group=Group(
                column="id",
                function="MAX",
                having=Having(column="id", operator="in", value=(2, 3, 4)),
                return_aggregation_column=True,
            ),
        )

        assert posts == [
            {"id": 2, "MAX(`id`)": 2},
            {"id": 3, "MAX(`id`)": 3},
            {"id": 4, "MAX(`id`)": 4},
        ]

        conn.close()
