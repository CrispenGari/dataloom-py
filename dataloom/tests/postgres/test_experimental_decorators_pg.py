class TestExperimentalDecoratorsOnPG:
    def test_initialize_decorator_fn(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
        )
        from dataloom.decorators import initialize
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

        conn, tables = pg_loom.connect_and_sync(
            [
                User,
                Profile,
            ],
            drop=True,
            force=True,
        )
        userId = pg_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )
        profileId = pg_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )

        res = pg_loom.find_by_pk(Profile, pk=profileId, select={"id", "avatar"})

        profile = Profile(**res)
        assert str(profile) == "<Profile:id=1>"
        assert profile.avatar == "hello.jpg"
        assert profile.id == 1
        assert profile.to_dict == {"avatar": "hello.jpg", "id": 1, "userId": None}
        conn.close()
