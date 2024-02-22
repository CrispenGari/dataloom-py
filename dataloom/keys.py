# Configuration file for unit testing.


push = True


class PgConfig:
    if push:
        password = "postgres"
        database = "postgres"
        user = "postgres"
        host = "0.0.0.0"
        port = 5432
        db = "hi"
        connection_uri = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    else:
        database = "postgres"
        user = "postgres"
        password = "root"
        host = "localhost"
        port = 5432
        db = "hi"
        connection_uri = f"postgresql://{user}:{password}@{host}:{port}/{db}"


class MySQLConfig:
    if push:
        password = "testrootpass"
        database = "testdb"
        user = "root"
        host = "0.0.0.0"
        port = 3306
        db = "hi"
        connection_uri = f"mysql://{user}:{password}@{host}:{port}/{db}"
    else:
        database = "hi"
        user = "root"
        password = "root"
        host = "localhost"
        port = 3306
        db = "hi"
        connection_uri = f"mysql://{user}:{password}@{host}:{port}/{db}"


class SQLiteConfig:
    if push:
        connection_uri = "sqlite:///database.db"
    else:
        connection_uri = r"C:\\Users\\RGaridzirai\\OneDrive - Walter Sisulu University\Desktop\\TINASHE CRISPEN G\\orm\\dataloom-py\\hi.db"
