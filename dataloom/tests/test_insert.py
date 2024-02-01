class TestInsertingOnPG:
    def test_insetting_single_document(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import Model, PrimaryKeyColumn
        from dataloom.keys import password, database, user

        db = Database(database, password=password, user=user)
        conn = db.connect()

        class Users(Model):
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False, default="Hello there!!")
            name = Column(type="varchar", unique=True, length=255)

        db.sync([Users], drop=True, force=True)

        user = Users(name="Crispen", username="heyy")
        userId = db.create(user)
        assert userId == 1
        conn.close()

    def test_insetting_multiple_document(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import (
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            PrimaryKeyColumn,
        )
        from dataloom.keys import password, database, user

        db = Database(database, password=password, user=user)

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__ = "posts"

            id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")

        conn, _ = db.connect_and_sync([User, Post], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = db.create(user)
        posts = [
            Post(userId=userId, title="What are you thinking"),
            Post(userId=userId, title="What are you doing?"),
            Post(userId=userId, title="What are we?"),
        ]
        row_count = db.create_bulk(posts)

        assert row_count == 3
        conn.close()

    def test_relational_instances(self):
        from dataloom.db import Database
        from dataloom.model.column import Column
        from dataloom.model.model import (
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            PrimaryKeyColumn,
        )
        from dataloom.keys import password, database, user

        db = Database(database, password=password, user=user)

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__ = "posts"

            id = PrimaryKeyColumn(type="bigint", auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            userId = ForeignKeyColumn(User, onDelete="CASCADE", onUpdate="CASCADE")

        db = Database("hi", password="root", user="postgres")
        conn, _ = db.connect_and_sync([User, Post], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = db.create(user)
        postId = db.create(
            Post(userId=userId, title="What are you thinking"),
        )
        now = db.find_by_pk(Post, postId)
        assert userId == now.userId
        conn.close()
