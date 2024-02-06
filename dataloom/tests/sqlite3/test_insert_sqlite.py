class TestInsertingOnSQLite:
    def test_insetting_single_document(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
        )

        from typing import Optional

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        user = User(username="@miller")
        userId = sqlite_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        post_id = sqlite_loom.insert_one(post)
        assert userId == 1
        assert post_id == 1
        conn.close()

    def test_insetting_multiple_document(self):
        from dataloom import (
            Dataloom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            UpdatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
        )
        from typing import Optional

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)

            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__: Optional[TableColumn] = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
        user = User(username="@miller")
        userId = sqlite_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        count = sqlite_loom.insert_bulk([post for i in range(5)])
        assert count == 5
        conn.close()

    def test_relational_instances(self):
        from dataloom import (
            Model,
            CreatedAtColumn,
            UpdatedAtColumn,
            ForeignKeyColumn,
            PrimaryKeyColumn,
            Column,
            Dataloom,
        )

        sqlite_loom = Dataloom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__ = "users"
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            username = Column(type="text", nullable=False)
            name = Column(type="varchar", unique=False, length=255)
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()

        class Post(Model):
            __tablename__ = "posts"

            id = PrimaryKeyColumn(type="int", auto_increment=True)
            title = Column(type="text", nullable=False, default="Hello there!!")
            createAt = CreatedAtColumn()
            updatedAt = UpdatedAtColumn()
            userId = ForeignKeyColumn(
                User, type="int", onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = sqlite_loom.connect_and_sync([User, Post], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = sqlite_loom.insert_one(user)
        postId = sqlite_loom.insert_one(
            Post(userId=userId, title="What are you thinking"),
        )
        now = sqlite_loom.find_by_pk(Post, postId)
        assert userId == now["userId"]
        conn.close()
