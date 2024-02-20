class TestExperimentalDecoratorsOnMySQL:
    def test_initialize_decorator_fn(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
        )
        from dataloom.decorators import initialize
        from dataloom.keys import MySQLConfig

        mysql_loom = Dataloom(
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
            tokenVersion = Column(type="int", default=0)

        @initialize(repr=True, to_dict=True, init=True, repr_identifier="id")
        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            avatar = Column(type="text", nullable=False)
            userId = ForeignKeyColumn(
                User,
                maps_to="1-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = mysql_loom.connect_and_sync(
            [
                User,
                Profile,
            ],
            drop=True,
            force=True,
        )
        userId = mysql_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        profileId = mysql_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )

        res = mysql_loom.find_by_pk(Profile, pk=profileId, select={"id", "avatar"})

        profile = Profile(**res)
        assert str(profile) == "<Profile:id=1>"
        assert profile.avatar == "hello.jpg"
        assert profile.id == 1
        assert profile.to_dict == {"avatar": "hello.jpg", "id": 1, "userId": None}
        conn.close()
