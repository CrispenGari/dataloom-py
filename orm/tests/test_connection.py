class TestConnectionPG:
    def test_connection(self):
        from orm.db import Database

        database = Database("hi", password="root", user="postgres")
        conn = database.connect()
        assert conn.status == 1
