# Configuration file for unit testing.


push = True


class PgConfig:
    if push:
        password = "postgres"
        database = "postgres"
        user = "postgres"
        host = "localhost"
        port = 5432
        connection_uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    else:
        database = "postgres"
        user = "postgres"
        password = "root"
        host = "localhost"
        port = 5432
        connection_uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"


class MySQLConfig:
    if push:
        password = "testrootpass"
        database = "testdb"
        user = "root"
        host = "0.0.0.0"
        port = 3306
        connection_uri = f"mysql://{user}:{password}@{host}:{port}/{database}"
    else:
        database = "hi"
        user = "root"
        password = "root"
        host = "localhost"
        port = 3306
        connection_uri = f"mysql://{user}:{password}@{host}:{port}/{database}"


class SQLiteConfig:
    if push:
        connection_uri = "sqlite:///hi.db"
    else:
        connection_uri = "sqlite:///hi.db"
