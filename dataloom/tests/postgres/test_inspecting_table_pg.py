class TestInspectTableOnPG:
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
        from dataloom.keys import PgConfig
        from dataloom.exceptions import UnknownColumnException
        import pytest

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

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        conn, _ = pg_loom.connect_and_sync([User], drop=True, force=True)
        res = pg_loom.inspect(instance=User, fields=["name", "type"], print_table=False)
        assert len(res) == 5
        res = pg_loom.inspect(instance=User, fields=["name", "type"], print_table=True)
        assert res is None

        with pytest.raises(UnknownColumnException) as exc_info:
            pg_loom.inspect(
                instance=User, fields=["name", "type", "hi"], print_table=False
            )
        assert (
            str(exc_info.value)
            == "You can not select 'hi' when inspecting table 'users' allowed fields are (name, type, nullable, default)."
        )
        conn.close()
