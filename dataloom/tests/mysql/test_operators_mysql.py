class TestOperatorsOnMysql:
    def testing_operators(self):
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
        general = mysql_loom.find_one(
            instance=Post,
            filters=Filter(
                column="title",
                value="% general?",
                operator="like",
            ),
            select=["id", "title"],
        )
        assert general == {"id": 1, "title": "What are you doing general?"}
        res1 = mysql_loom.update_one(
            instance=Post,
            filters=Filter(
                column="id",
                value=1,
                operator="eq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res2 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=1,
                operator="neq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res4 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="lt",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res3 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="leq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res5 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="gt",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res6 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="geq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res7 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=[1, 2],
                operator="in",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res8 = mysql_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=[1, 2],
                operator="notIn",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )

        assert res1 == 1
        assert res2 == 3
        assert res4 == 0
        assert res3 == 0
        assert res5 == 0
        assert res6 == 0
        assert res7 == 0
        assert res8 == 0

        conn.close()
