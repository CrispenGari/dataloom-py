class TestOperatorsSqlite:
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

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

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

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        categories = ["general", "education", "sport", "culture"]
        for cat in categories:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="title", value=f"What are you doing {cat}?"),
                    ColumnValue(name="userId", value=userId),
                ],
            )
        general = sqlite_loom.find_one(
            instance=Post,
            filters=Filter(
                column="title",
                value="% general?",
                operator="like",
            ),
            select=["id", "title"],
        )
        assert general == {"id": 1, "title": "What are you doing general?"}
        res1 = sqlite_loom.update_one(
            instance=Post,
            filters=Filter(
                column="id",
                value=1,
                operator="eq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res2 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=1,
                operator="neq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res4 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="lt",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res3 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="leq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res5 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="gt",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res6 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=3,
                operator="geq",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res7 = sqlite_loom.update_bulk(
            instance=Post,
            filters=Filter(
                column="id",
                value=[1, 2],
                operator="in",
            ),
            values=[ColumnValue(name="title", value="Bob")],
        )
        res8 = sqlite_loom.update_bulk(
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
        assert res4 == 2
        assert res3 == 3
        assert res5 == 1
        assert res6 == 2
        assert res7 == 2
        assert res8 == 2

        conn.close()
