import pytest


class TestConnectionURISQLite:
    def test_connect_with_wrong_dialect(self):
        from dataloom import Loom
        from dataloom.exceptions import UnsupportedDialectException
        from dataloom.keys import SQLiteConfig

        with pytest.raises(UnsupportedDialectException) as exc_info:
            sqlite_loom = Loom(
                dialect="hay", connection_uri=SQLiteConfig.connection_uri
            )
            conn = sqlite_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Loom
        from dataloom.keys import SQLiteConfig

        sqlite_loom = Loom(dialect="sqlite", connection_uri=SQLiteConfig.connection_uri)
        conn = sqlite_loom.connect()
        conn.close()
        assert conn is not None
