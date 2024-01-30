class TestConnectionPG:
    def test_connection(self):
        from orm.db import Database
        from orm.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()
        assert conn.status == 1
