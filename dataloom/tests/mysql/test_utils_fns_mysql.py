class TestUtilsFunctionsMySQL:
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
        from dataloom.keys import MySQLConfig
        from typing import Optional

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
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

        conn, _ = mysql_loom.connect_and_sync([Post, User], drop=True, force=True)
        userId = mysql_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            mysql_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        count = mysql_loom.count(
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

        avg = mysql_loom.avg(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert avg == 2.5
        sum = mysql_loom.sum(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert sum == 10
        min = mysql_loom.min(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert min == 1
        max = mysql_loom.max(
            instance=Post,
            column="id",
            distinct=True,
        )
        assert max == 4
        conn.close()
