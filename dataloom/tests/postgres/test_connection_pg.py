import pytest


class TestConnectionPG:
    def test_connect_with_non_existing_database(self):
        from dataloom import Dataloom

        pg_loom = Dataloom(
            dialect="postgres", database="mew", password="root", user="postgres"
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()
        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "mew" does not exist'
        )

    def test_connect_with_wrong_password(self):
        from dataloom import Dataloom

        pg_loom = Dataloom(
            dialect="postgres", database="hi", password="root-", user="postgres"
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "postgres"'
        )

    def test_connect_with_wrong_user(self):
        from dataloom import Dataloom

        pg_loom = Dataloom(
            dialect="postgres", database="hi", password="root", user="postgre-u"
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "postgre-u"'
        )

    def test_connect_with_wrong_dialect(self):
        from dataloom import Dataloom, UnsupportedDialectException

        with pytest.raises(UnsupportedDialectException) as exc_info:
            pg_loom = Dataloom(
                dialect="peew", database="hi", password="root", user="postgres"
            )
            conn = pg_loom.connect()
            conn.close()
        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Dataloom

        pg_loom = Dataloom(
            dialect="postgres", database="hi", password="root", user="postgres"
        )
        conn = pg_loom.connect()
        conn.close()

        assert conn is not None
