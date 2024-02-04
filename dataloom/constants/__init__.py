from datetime import datetime

CURRENT_TIME_STAMP = datetime.now()
SQLITE_CURRENT_TIME_STAMP = 'datetime("now")'
instances = {
    "postgres": {
        "type": "postgres",
        "port": 5432,
        "user": "postgres",
        "password": "postgres",
        "host": "localhost" or "127.0.0.1",
    },
    "mysql": {
        "type": "mysql",
        "port": 3306,
        "user": "root",
        "password": "root",
        "host": "127.0.0.1" or "localhost",
    },
    "sqlite": {"database": "dataloom_instance.db", "type": "sqlite"},
}
