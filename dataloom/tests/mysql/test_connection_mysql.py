import pytest
from mysql import connector


class TestConnectionMySQL:
    def test_connect_with_non_existing_database(self):
        from dataloom import Dataloom

        mysql_loom = Dataloom(
            dialect="mysql", database="non-exists", password="root", user="root"
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()
        assert exc_info.value.msg == "Unknown database 'non-exists'"
        assert exc_info.value.errno == 1049

    def test_connect_with_wrong_password(self):
        from dataloom import Dataloom

        mysql_loom = Dataloom(
            dialect="mysql", database="hi", password="user", user="root"
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()
        assert (
            exc_info.value.msg
            == "Access denied for user 'root'@'localhost' (using password: YES)"
        )
        assert exc_info.value.errno == 1045

    def test_connect_with_wrong_user(self):
        from dataloom import Dataloom

        mysql_loom = Dataloom(
            dialect="mysql", database="hi", password="root", user="hey"
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()
        assert (
            exc_info.value.msg
            == "Access denied for user 'hey'@'localhost' (using password: YES)"
        )
        assert exc_info.value.errno == 1045

    def test_connect_with_wrong_dialect(self):
        from dataloom import Dataloom, UnsupportedDialectException

        with pytest.raises(UnsupportedDialectException) as exc_info:
            mysql_loom = Dataloom(
                dialect="peew", database="hi", password="user", user="root"
            )
            conn = mysql_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Dataloom

        mysql_loom = Dataloom(
            dialect="mysql", database="hi", password="root", user="root"
        )
        conn = mysql_loom.connect()
        conn.close()
        assert conn is not None
