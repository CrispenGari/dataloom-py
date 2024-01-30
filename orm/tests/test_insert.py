class TestInsertingOnePG:
    def test_2_pk_error(self):
        from orm.db import Database
        from orm.model.column import Column
        from orm.model.model import Model

        db = Database("postgres", password="postgres", user="postgres")
        conn = db.connect()

        class Users(Model):
            id = Column(
                type="bigint", primary_key=True, nullable=False, auto_increment=True
            )
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        db.sync([Users], drop=True, force=True)

        user = Users(name="Crispen", username="heyy")
        userId = db.commit(user)
        assert userId == 1
        conn.close()
