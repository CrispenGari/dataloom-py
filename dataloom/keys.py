push = True


class PgConfig:
    if push:
        password = "postgres"
        database = "postgres"
        user = "postgres"
    else:
        database = "postgres"
        user = "postgres"
        password = "root"


class MySQLConfig:
    if push:
        password = "root"
        database = "test"
        user = "root"
    else:
        database = "hi"
        user = "root"
        password = "root"