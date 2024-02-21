class TestInsertingOnMySQL:
    def test_insetting_single_document(self):
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
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
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

        conn, _ = mysql_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = mysql_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        post_id = mysql_loom.insert_one(
            Post,
            values=[
                ColumnValue(name="title", value="What are you doing?"),
                ColumnValue(name="userId", value=userId),
            ],
        )
        assert userId == 1
        assert post_id == 1
        conn.close()

    def test_insetting_multiple_document(self):
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
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
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

        conn, _ = mysql_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = mysql_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]

        count = mysql_loom.insert_bulk(Post, values=[values for i in range(5)])
        assert count == 5
        conn.close()

    def test_relational_instances(self):
        from dataloom import (
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            PrimaryKeyColumn,
            Column,
            Loom,
            ColumnValue,
            TableColumn,
        )
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")

            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            userId = ForeignKeyColumn(
                User, type="bigint", onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = mysql_loom.connect_and_sync([User, Post], drop=True, force=True)

        userId = mysql_loom.insert_one(
            User, ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]

        postId = mysql_loom.insert_one(Post, values)
        now = mysql_loom.find_by_pk(Post, postId)
        assert userId == now["userId"]
        conn.close()

    def test_insert_bulk_with_errors(self):
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
        from dataloom.keys import MySQLConfig
        import pytest
        from dataloom.exceptions import InvalidColumnValuesException

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
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

        conn, _ = mysql_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = mysql_loom.insert_one(
            User, values=ColumnValue(name="username", value="@miller")
        )
        values = [
            ColumnValue(name="title", value="What are you doing?"),
            ColumnValue(name="userId", value=userId),
        ]
        with pytest.raises(InvalidColumnValuesException) as exc_info:
            mysql_loom.insert_bulk(Post, values=values)

        assert (
            str(exc_info.value)
            == "The insert_bulk method takes in values as lists of lists."
        )

        with pytest.raises(InvalidColumnValuesException) as exc_info:
            mysql_loom.insert_bulk(
                Post,
                values=[
                    [
                        ColumnValue(name="title", value="What are you doing?"),
                        ColumnValue(name="userId", value=userId),
                    ],
                    ColumnValue(name="title", value="What are you doing?"),
                ],
            )
        assert (
            str(exc_info.value)
            == "The insert_bulk method takes in values as lists of lists."
        )

        with pytest.raises(InvalidColumnValuesException) as exc_info:
            mysql_loom.insert_bulk(
                Post,
                values=[
                    [
                        ColumnValue(name="title", value="What are you doing?"),
                        ColumnValue(name="userId", value=userId),
                    ],
                    [
                        ColumnValue(name="title", value="What are you doing?"),
                    ],
                ],
            )
        assert (
            str(exc_info.value)
            == "The insert_bulk method takes in values as lists of lists with equal ColumnValues."
        )
        conn.close()
