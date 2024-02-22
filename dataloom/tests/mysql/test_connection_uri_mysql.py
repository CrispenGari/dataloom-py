import pytest
from mysql import connector


class TestConnectionURIMySQL:
    def test_connect_with_non_existing_database(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig

        mysql_loom = Loom(
            dialect="mysql",
            connection_uri=f"mysql://{MySQLConfig.user}:{MySQLConfig.password}@{MySQLConfig.host}:{MySQLConfig.port}/non-exists",
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
            connection_uri=f"mysql://{MySQLConfig.user}:{MySQLConfig.password+'me'}@{MySQLConfig.host}:{MySQLConfig.port}/{MySQLConfig.database}",
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
            connection_uri=f"mysql://hey:{MySQLConfig.password}@{MySQLConfig.host}:{MySQLConfig.port}/{MySQLConfig.database}",
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
                dialect="dialect",
                connection_uri=f"mysql://{MySQLConfig.user}:{MySQLConfig.password}@{MySQLConfig.host}:{MySQLConfig.port}/{MySQLConfig.database}",
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
            connection_uri=f"mysql://{MySQLConfig.user}:{MySQLConfig.password}@{MySQLConfig.host}:{MySQLConfig.port}/{MySQLConfig.database}",
        )
        conn = mysql_loom.connect()
        conn.close()
        assert conn is not None

    def test_wrong_connection_uri(self):
        from dataloom import Loom
        from dataloom.keys import MySQLConfig
        from dataloom.exceptions import InvalidConnectionURI

        with pytest.raises(InvalidConnectionURI) as exc_info:
            pg_loom = Loom(
                dialect="mysql",
                connection_uri=f"mysq://{MySQLConfig.user}:{MySQLConfig.password}@{MySQLConfig.host}:{MySQLConfig.port}/{MySQLConfig.database}",
            )
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "Invalid connection uri for the dialect 'mysql' valid examples are ('mysql://user:password@localhost:3306/dbname')."
        )
