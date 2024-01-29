from orm.db import Database


class TestConnection:
    def test_connection(self):
        database = Database("hi", password="root", user="postgres")
        conn = database.connect()
        assert conn.status == 1
