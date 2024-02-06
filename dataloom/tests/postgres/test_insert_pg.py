class TestInsertingOnPG:
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
        from dataloom.keys import PgConfig
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

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

        conn, _ = pg_loom.connect_and_sync([Post, User], drop=True, force=True)
        user = User(username="@miller")
        userId = pg_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        post_id = pg_loom.insert_one(post)
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
        from dataloom.keys import PgConfig
        from typing import Optional

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

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

        conn, _ = pg_loom.connect_and_sync([Post, User], drop=True, force=True)
        user = User(username="@miller")
        userId = pg_loom.insert_one(user)
        post = Post(title="What are you doing?", userId=userId)
        count = pg_loom.insert_bulk([post for i in range(5)])
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
        from dataloom.keys import PgConfig

        pg_loom = Dataloom(
            dialect="postgres",
            database=PgConfig.database,
            password=PgConfig.password,
            user=PgConfig.user,
        )

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
            userId = ForeignKeyColumn(
                User, type="bigint", onDelete="CASCADE", onUpdate="CASCADE"
            )

        conn, _ = pg_loom.connect_and_sync([User, Post], drop=True, force=True)
        user = User(name="Crispen", username="heyy")
        userId = pg_loom.insert_one(user)
        postId = pg_loom.insert_one(
            Post(userId=userId, title="What are you thinking"),
        )
        now = pg_loom.find_by_pk(Post, postId)
        assert userId == now["userId"]
        conn.close()
