class TestAlterTableOnMySQL:
    def test_alter_connect_and_sync(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            bio = Column(
                type="varchar", unique=False, length=200, default="Hello world"
            )
            tokenVersion = Column(type="int", default=0)

            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

            profileId = ForeignKeyColumn(
                Profile,
                type="int",
                maps_to="1-1",
                onDelete="CASCADE",
                onUpdate="CASCADE",
                required=False,
            )

        conn, tables = mysql_loom.connect_and_sync([Profile, User], alter=True)

        assert len(mysql_loom.inspect(Profile, print_table=False)) == 2
        assert len(mysql_loom.inspect(User, print_table=False)) == 8
        conn.close()

    def test_alter_sync(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            bio = Column(
                type="varchar", unique=False, length=200, default="Hello world"
            )
            tokenVersion = Column(type="int", default=0)

            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

            profileId = ForeignKeyColumn(
                Profile,
                type="int",
                maps_to="1-1",
                onDelete="CASCADE",
                onUpdate="CASCADE",
                required=False,
            )

        conn = mysql_loom.connect()
        _tables = mysql_loom.sync([Profile, User], alter=True)
        assert len(mysql_loom.inspect(Profile, print_table=False)) == 2
        assert len(mysql_loom.inspect(User, print_table=False)) == 8
        conn.close()
