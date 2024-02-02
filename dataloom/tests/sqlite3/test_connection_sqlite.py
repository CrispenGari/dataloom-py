import pytest


class TestConnectionSQLite:
    def test_connect_with_wrong_dialect(self):
        from dataloom import Dataloom, UnsupportedDialectException

        with pytest.raises(UnsupportedDialectException) as exc_info:
            sqlite_loom = Dataloom(dialect="hay", database="hi.db")
            conn = sqlite_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Dataloom

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")
        conn = sqlite_loom.connect()
        conn.close()
        assert conn is not None
