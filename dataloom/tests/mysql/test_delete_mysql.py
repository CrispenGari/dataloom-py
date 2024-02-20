class TestDeletingOnMysql:
    def test_delete_by_pk_fn(self):
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
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

        affected_rows_1 = mysql_loom.delete_by_pk(User, userId)
        affected_rows_2 = mysql_loom.delete_by_pk(User, 89)
        assert affected_rows_1 == 1
        assert affected_rows_2 == 0
        conn.close()

    def test_delete_one_fn(self):
        import pytest
        from dataloom.exceptions import UnknownColumnException
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            Filter,
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
        mysql_loom.insert_bulk(
            User,
            values=[
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="hi"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="heyy"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="who"),
                ],
            ],
        )
        mysql_loom.delete_one(User, filters=[Filter(column="name", value="Crispen")])
        rows_1 = mysql_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )
        mysql_loom.delete_one(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=9),
            ],
        )
        rows_2 = mysql_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )
        mysql_loom.delete_one(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=2),
            ],
        )
        rows_3 = mysql_loom.find_many(
            User, filters=[Filter(column="name", value="Crispen")]
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            mysql_loom.delete_bulk(
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
        from dataloom.exceptions import UnknownColumnException
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            Filter,
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
        mysql_loom.insert_bulk(
            User,
            values=[
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="hi"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="heyy"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="hie"),
                ],
            ],
        )
        mysql_loom.delete_bulk(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        rows_1 = mysql_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        mysql_loom.insert_bulk(
            User,
            values=[
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="hi"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="heyy"),
                ],
                [
                    ColumnValue(name="name", value="Crispen"),
                    ColumnValue(name="username", value="hie"),
                ],
            ],
        )
        mysql_loom.delete_bulk(
            User,
            filters=[
                Filter(column="name", value="Crispen"),
                Filter(column="id", value=99),
            ],
        )
        rows_2 = mysql_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )
        mysql_loom.delete_bulk(
            User,
            filters=[
                Filter(column="name", value="Crispen", operator="eq"),
                Filter(column="id", value=5, operator="eq"),
            ],
        )
        rows_3 = mysql_loom.find_many(
            User, filters=Filter(column="name", value="Crispen", operator="eq")
        )

        with pytest.raises(UnknownColumnException) as exc_info:
            mysql_loom.delete_bulk(
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

    def test_delete_with_limit(self):
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            ColumnValue,
            Filter,
            Order,
        )
        from dataloom.keys import MySQLConfig
        import pytest
        from dataloom.exceptions import InvalidArgumentsException

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
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        categories = ["general", "education", "sport", "culture"]
        for cat in categories:
            mysql_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="title", value=f"What are you doing {cat}?"),
                    ColumnValue(name="userId", value=userId),
                ],
            )

        res1 = mysql_loom.delete_bulk(
            instance=Post,
            offset=3,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1)],
            limit=1,
        )
        res2 = mysql_loom.delete_bulk(
            instance=Post,
            offset=0,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1, operator="gt")],
            limit=3,
        )
        res3 = mysql_loom.delete_one(
            instance=Post,
            offset=0,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1, operator="gt")],
        )
        assert res1 == 0
        assert res2 == 3
        assert res3 == 0
        with pytest.raises(InvalidArgumentsException) as exc_info:
            mysql_loom.delete_bulk(
                instance=Post,
                offset=3,
                order=[Order(column="id", order="DESC")],
                filters=[Filter(column="id", value=1)],
            )

        assert (
            str(exc_info.value)
            == "You can not apply offset without limit on dialect 'mysql'."
        )

        conn.close()

    def test_delete_with_filters(self):
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            ColumnValue,
            Order,
            Filter,
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
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        categories = ["general", "education", "sport", "culture"]
        for cat in categories:
            mysql_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="title", value=f"What are you doing {cat}?"),
                    ColumnValue(name="userId", value=userId),
                ],
            )

        res1 = mysql_loom.delete_bulk(
            instance=Post,
            offset=3,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1)],
            limit=1,
        )
        res2 = mysql_loom.delete_bulk(
            instance=Post,
            offset=0,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1, operator="gt")],
            limit=3,
        )
        res3 = mysql_loom.delete_one(
            instance=Post,
            offset=0,
            order=[Order(column="id", order="DESC")],
            filters=[Filter(column="id", value=1, operator="gt")],
        )
        assert res1 == 0
        assert res2 == 3
        assert res3 == 0
        conn.close()
