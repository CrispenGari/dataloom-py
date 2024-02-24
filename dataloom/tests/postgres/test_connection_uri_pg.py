import pytest


class TestConnectionURIPG:
    def test_connect_with_non_existing_database(self):
        from dataloom import Loom
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            connection_uri=f"postgresql://{PgConfig.user}:{PgConfig.password}@{PgConfig.host}:{PgConfig.port}/mew",
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()
        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "mew" does not exist'
        )

    def test_connect_with_wrong_password(self):
        from dataloom import Loom
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            connection_uri=f"postgresql://{PgConfig.user}:{PgConfig.password+'-'}@{PgConfig.host}:{PgConfig.port}/{PgConfig.database}",
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "postgres"'
        )

    def test_connect_with_wrong_user(self):
        from dataloom import Loom
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            connection_uri=f"postgresql://postgre-u:{PgConfig.password}@{PgConfig.host}:{PgConfig.port}/{PgConfig.database}",
        )
        with pytest.raises(Exception) as exc_info:
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value.args[0]).strip()
            == 'connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "postgre-u"'
        )

    def test_connect_with_wrong_dialect(self):
        from dataloom import Loom
        from dataloom.exceptions import UnsupportedDialectException
        from dataloom.keys import PgConfig

        with pytest.raises(UnsupportedDialectException) as exc_info:
            pg_loom = Loom(
                dialect="peew",
                connection_uri=f"postgresql://{PgConfig.user}:{PgConfig.password}@{PgConfig.host}:{PgConfig.port}/{PgConfig.database}",
            )
            conn = pg_loom.connect()
            conn.close()
        assert (
            str(exc_info.value)
            == "The dialect passed is not supported the supported dialects are: {'postgres', 'mysql', 'sqlite'}"
        )

    def test_connect_correct_connection(self):
        from dataloom import Loom
        from dataloom.keys import PgConfig

        pg_loom = Loom(
            dialect="postgres",
            connection_uri=f"postgresql://{PgConfig.user}:{PgConfig.password}@{PgConfig.host}:{PgConfig.port}/{PgConfig.database}",
        )
        conn = pg_loom.connect()
        conn.close()

        assert conn is not None

    def test_wrong_connection_uri(self):
        from dataloom import Loom
        from dataloom.keys import PgConfig
        from dataloom.exceptions import InvalidConnectionURI

        with pytest.raises(InvalidConnectionURI) as exc_info:
            pg_loom = Loom(
                dialect="postgres",
                connection_uri=f"postgresl://{PgConfig.user}:{PgConfig.password}@{PgConfig.host}:{PgConfig.port}/{PgConfig.database}",
            )
            conn = pg_loom.connect()
            conn.close()

        assert (
            str(exc_info.value)
            == "Invalid connection uri for the dialect 'postgres' valid examples are ('postgresql://user:password@localhost:5432/dbname')."
        )
