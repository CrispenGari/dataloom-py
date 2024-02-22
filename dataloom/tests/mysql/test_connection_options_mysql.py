import pytest
from mysql import connector


class TestConnectionOptionsMySQL:
    def test_connect_with_non_existing_database(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database="non-exists",
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()
        assert exc_info.value.msg == "Unknown database 'non-exists'"
        assert exc_info.value.errno == 1049

    def test_connect_with_wrong_password(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password="user",
            user=MySQLConfig.user,
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()

        assert str(exc_info.value.msg).startswith(
            "Access denied for user 'root'@'"
        ) and str(exc_info.value.msg).endswith("(using password: YES)")
        assert exc_info.value.errno == 1045

    def test_connect_with_wrong_user(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user="hey",
        )
        with pytest.raises(connector.errors.ProgrammingError) as exc_info:
            conn = mysql_loom.connect()
            conn.close()
        assert str(exc_info.value.msg).startswith(
            "Access denied for user 'hey'@"
        ) and str(exc_info.value.msg).endswith("(using password: YES)")
        assert exc_info.value.errno == 1045

    def test_connect_with_wrong_dialect(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig
        from dataloom.exceptions import UnsupportedDialectException

        with pytest.raises(UnsupportedDialectException) as exc_info:
            mysql_loom = Loom(
                dialect="peew",
                database=MySQLConfig.database,
                password="user",
                user=MySQLConfig.user,
            )
            conn = mysql_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            database=MySQLConfig.database,
            password=MySQLConfig.password,
            user=MySQLConfig.user,
        )
        conn = mysql_loom.connect()
        conn.close()
        assert conn is not None
