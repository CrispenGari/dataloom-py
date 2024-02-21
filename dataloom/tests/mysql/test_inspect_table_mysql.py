class TestInspectTableOnMysql:
    def testing_inspecting_table(self):
        from dataloom import (
            Column,
            PrimaryKeyColumn,
            Loom,
            TableColumn,
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
        )
        from dataloom.keys import MySQLConfig
        import pytest
        from dataloom.exceptions import UnknownColumnException

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

        conn, _ = mysql_loom.connect_and_sync([User], drop=True, force=True)
        res = mysql_loom.inspect(
            instance=User, fields=["name", "type"], print_table=False
        )
        assert len(res) == 5
        res = mysql_loom.inspect(
            instance=User, fields=["name", "type"], print_table=True
        )
        assert res is None

        with pytest.raises(UnknownColumnException) as exc_info:
            mysql_loom.inspect(
                instance=User, fields=["name", "type", "hi"], print_table=False
            )
        assert (
            str(exc_info.value)
            == "You can not select 'hi' when inspecting table 'users' allowed fields are (name, type, nullable, default)."
        )
        conn.close()
