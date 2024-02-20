class TestEagerLoadingOnSQLite:
    def test_find_by_pk(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Include,
            Order,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            avatar = Column(type="text", nullable=False)
            userId = ForeignKeyColumn(
                User,
                maps_to="1-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Category(Model):
            __tablename__: TableColumn = TableColumn(name="categories")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            type = Column(type="varchar", length=255, nullable=False)

            postId = ForeignKeyColumn(
                Post,
                maps_to="N-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = sqlite_loom.connect_and_sync(
            [User, Profile, Post, Category], drop=True, force=True
        )

        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        userId2 = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="bob"),
        )

        profileId = sqlite_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )
        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        for cat in ["general", "education", "tech", "sport"]:
            sqlite_loom.insert_one(
                instance=Category,
                values=[
                    ColumnValue(name="postId", value=1),
                    ColumnValue(name="type", value=cat),
                ],
            )

        profile = sqlite_loom.find_by_pk(
            instance=Profile,
            pk=profileId,
            include=[
                Include(
                    model=User, select=["id", "username", "tokenVersion"], has="one"
                )
            ],
        )
        assert profile == {
            "avatar": "hello.jpg",
            "id": 1,
            "userId": 1,
            "user": {"id": 1, "username": "@miller", "tokenVersion": 0},
        }

        user = sqlite_loom.find_by_pk(
            instance=User,
            pk=userId,
            include=[Include(model=Profile, select=["id", "avatar"], has="one")],
        )
        assert user == {
            "id": 1,
            "name": "Bob",
            "tokenVersion": 0,
            "username": "@miller",
            "profile": {"id": 1, "avatar": "hello.jpg"},
        }

        user = sqlite_loom.find_by_pk(
            instance=User,
            pk=userId,
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    offset=0,
                    limit=2,
                    order=[
                        Order(column="createdAt", order="DESC"),
                        Order(column="id", order="DESC"),
                    ],
                ),
                Include(model=Profile, select=["id", "avatar"], has="one"),
            ],
        )
        assert user == {
            "id": 1,
            "name": "Bob",
            "tokenVersion": 0,
            "username": "@miller",
            "posts": [
                {"id": 4, "title": "Coding"},
                {"id": 3, "title": "What are you doing"},
            ],
            "profile": {"id": 1, "avatar": "hello.jpg"},
        }

        post = sqlite_loom.find_by_pk(
            instance=Post,
            pk=1,
            select=["title", "id"],
            include=[
                Include(
                    model=User,
                    select=["id", "username"],
                    has="one",
                    include=[
                        Include(model=Profile, select=["avatar", "id"], has="one")
                    ],
                ),
                Include(
                    model=Category,
                    select=["id", "type"],
                    has="many",
                    order=[Order(column="id", order="DESC")],
                ),
            ],
        )

        assert post == {
            "title": "Hey",
            "id": 1,
            "user": {
                "id": 1,
                "username": "@miller",
                "profile": {"avatar": "hello.jpg", "id": 1},
            },
            "categories": [
                {"id": 4, "type": "sport"},
                {"id": 3, "type": "tech"},
                {"id": 2, "type": "education"},
                {"id": 1, "type": "general"},
            ],
        }

        user = sqlite_loom.find_by_pk(
            instance=User,
            pk=userId2,
            select=["username", "id"],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    include=[
                        Include(
                            model=Category,
                            select=["type", "id"],
                            has="many",
                            order=[Order(column="id", order="DESC")],
                            limit=2,
                            offset=0,
                        )
                    ],
                ),
            ],
        )
        assert user == {"username": "bob", "id": 2, "posts": []}

        conn.close()

    def test_find_one(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Include,
            Order,
            Filter,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            avatar = Column(type="text", nullable=False)
            userId = ForeignKeyColumn(
                User,
                maps_to="1-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Category(Model):
            __tablename__: TableColumn = TableColumn(name="categories")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            type = Column(type="varchar", length=255, nullable=False)

            postId = ForeignKeyColumn(
                Post,
                maps_to="N-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = sqlite_loom.connect_and_sync(
            [User, Profile, Post, Category], drop=True, force=True
        )

        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        userId2 = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="bob"),
        )

        profileId = sqlite_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )
        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        for cat in ["general", "education", "tech", "sport"]:
            sqlite_loom.insert_one(
                instance=Category,
                values=[
                    ColumnValue(name="postId", value=1),
                    ColumnValue(name="type", value=cat),
                ],
            )

        profile = sqlite_loom.find_one(
            instance=Profile,
            filters=[Filter(column="userId", value=profileId)],
            include=[
                Include(
                    model=User, select=["id", "username", "tokenVersion"], has="one"
                )
            ],
        )
        assert profile == {
            "avatar": "hello.jpg",
            "id": 1,
            "userId": 1,
            "user": {"id": 1, "username": "@miller", "tokenVersion": 0},
        }

        user = sqlite_loom.find_one(
            instance=User,
            filters=[Filter(column="id", value=userId)],
            include=[Include(model=Profile, select=["id", "avatar"], has="one")],
        )
        assert user == {
            "id": 1,
            "name": "Bob",
            "tokenVersion": 0,
            "username": "@miller",
            "profile": {"id": 1, "avatar": "hello.jpg"},
        }

        user = sqlite_loom.find_one(
            instance=User,
            filters=[Filter(column="id", value=userId)],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    offset=0,
                    limit=2,
                    order=[
                        Order(column="createdAt", order="DESC"),
                        Order(column="id", order="DESC"),
                    ],
                ),
                Include(model=Profile, select=["id", "avatar"], has="one"),
            ],
        )
        assert user == {
            "id": 1,
            "name": "Bob",
            "tokenVersion": 0,
            "username": "@miller",
            "posts": [
                {"id": 4, "title": "Coding"},
                {"id": 3, "title": "What are you doing"},
            ],
            "profile": {"id": 1, "avatar": "hello.jpg"},
        }

        post = sqlite_loom.find_one(
            instance=Post,
            filters=[Filter(column="userId", value=userId)],
            select=["title", "id"],
            include=[
                Include(
                    model=User,
                    select=["id", "username"],
                    has="one",
                    include=[
                        Include(model=Profile, select=["avatar", "id"], has="one")
                    ],
                ),
                Include(
                    model=Category,
                    select=["id", "type"],
                    has="many",
                    order=[Order(column="id", order="DESC")],
                ),
            ],
        )
        assert post == {
            "title": "Hey",
            "id": 1,
            "user": {
                "id": 1,
                "username": "@miller",
                "profile": {"avatar": "hello.jpg", "id": 1},
            },
            "categories": [
                {"id": 4, "type": "sport"},
                {"id": 3, "type": "tech"},
                {"id": 2, "type": "education"},
                {"id": 1, "type": "general"},
            ],
        }
        user = sqlite_loom.find_one(
            instance=User,
            filters=[Filter(column="id", value=userId2)],
            select=["username", "id"],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    include=[
                        Include(
                            model=Category,
                            select=["type", "id"],
                            has="many",
                            order=[Order(column="id", order="DESC")],
                            limit=2,
                            offset=0,
                        )
                    ],
                ),
            ],
        )
        assert user == {"username": "bob", "id": 2, "posts": []}

        user = sqlite_loom.find_all(
            instance=User,
            select=["username", "id"],
            limit=1,
            offset=0,
            order=[Order(column="id", order="ASC")],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    limit=1,
                    offset=0,
                    order=[Order(column="id", order="ASC")],
                    include=[
                        Include(
                            model=Category,
                            select=["type", "id"],
                            has="many",
                            order=[Order(column="id", order="DESC")],
                            limit=2,
                            offset=0,
                        ),
                        Include(
                            model=User,
                            select=["username", "id"],
                            has="one",
                        ),
                    ],
                ),
            ],
        )
        assert user == [
            {
                "username": "@miller",
                "id": 1,
                "categories": [{"type": "sport", "id": 4}, {"type": "tech", "id": 3}],
                "user": {"username": "@miller", "id": 1},
                "posts": [
                    {
                        "id": 1,
                        "title": "Hey",
                        "categories": [
                            {"type": "sport", "id": 4},
                            {"type": "tech", "id": 3},
                        ],
                        "user": {"username": "@miller", "id": 1},
                    }
                ],
            }
        ]

        conn.close()

    def test_find_many(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Include,
            Order,
            Filter,
        )

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            avatar = Column(type="text", nullable=False)
            userId = ForeignKeyColumn(
                User,
                maps_to="1-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Category(Model):
            __tablename__: TableColumn = TableColumn(name="categories")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            type = Column(type="varchar", length=255, nullable=False)

            postId = ForeignKeyColumn(
                Post,
                maps_to="N-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = sqlite_loom.connect_and_sync(
            [User, Profile, Post, Category], drop=True, force=True
        )

        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        userId2 = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="bob"),
        )

        profileId = sqlite_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )
        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        for cat in ["general", "education", "tech", "sport"]:
            sqlite_loom.insert_one(
                instance=Category,
                values=[
                    ColumnValue(name="postId", value=profileId),
                    ColumnValue(name="type", value=cat),
                ],
            )

        profile = sqlite_loom.find_many(
            instance=Profile,
            filters=[Filter(column="userId", value=1)],
            include=[
                Include(
                    model=User, select=["id", "username", "tokenVersion"], has="one"
                )
            ],
        )

        assert profile == [
            {
                "avatar": "hello.jpg",
                "id": 1,
                "userId": 1,
                "user": {"id": 1, "username": "@miller", "tokenVersion": 0},
            }
        ]

        user = sqlite_loom.find_many(
            instance=User,
            filters=[Filter(column="id", value=userId)],
            include=[Include(model=Profile, select=["id", "avatar"], has="one")],
        )
        assert user == [
            {
                "id": 1,
                "name": "Bob",
                "tokenVersion": 0,
                "username": "@miller",
                "profile": {"id": 1, "avatar": "hello.jpg"},
            }
        ]

        user = sqlite_loom.find_many(
            instance=User,
            filters=[Filter(column="id", value=userId)],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    offset=0,
                    limit=2,
                    order=[
                        Order(column="createdAt", order="DESC"),
                        Order(column="id", order="DESC"),
                    ],
                ),
                Include(model=Profile, select=["id", "avatar"], has="one"),
            ],
        )
        assert user == [
            {
                "id": 1,
                "name": "Bob",
                "tokenVersion": 0,
                "username": "@miller",
                "posts": [
                    {"id": 4, "title": "Coding"},
                    {"id": 3, "title": "What are you doing"},
                ],
                "profile": {"id": 1, "avatar": "hello.jpg"},
            }
        ]
        post = sqlite_loom.find_many(
            instance=Post,
            filters=[Filter(column="userId", value=userId)],
            select=["title", "id"],
            limit=1,
            offset=0,
            order=[Order(column="id", order="DESC")],
            include=[
                Include(
                    model=User,
                    select=["id", "username"],
                    has="one",
                    include=[
                        Include(model=Profile, select=["avatar", "id"], has="one")
                    ],
                ),
                Include(
                    model=Category,
                    select=["id", "type"],
                    has="many",
                    order=[Order(column="id", order="DESC")],
                    limit=2,
                ),
            ],
        )

        assert post == [
            {
                "title": "Coding",
                "id": 4,
                "user": {
                    "id": 1,
                    "username": "@miller",
                    "profile": {"avatar": "hello.jpg", "id": 1},
                },
                "categories": [],
            }
        ]

        user = sqlite_loom.find_many(
            instance=User,
            filters=[Filter(column="id", value=userId2)],
            select=["username", "id"],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    include=[
                        Include(
                            model=Category,
                            select=["type", "id"],
                            has="many",
                            order=[Order(column="id", order="DESC")],
                            limit=2,
                            offset=0,
                        )
                    ],
                ),
            ],
        )
        assert user == [{"username": "bob", "id": 2, "posts": []}]
        posts = sqlite_loom.find_many(Post, select=["id", "completed"])
        assert posts == [
            {"id": 1, "completed": 0},
            {"id": 2, "completed": 0},
            {"id": 3, "completed": 0},
            {"id": 4, "completed": 0},
        ]
        user = sqlite_loom.find_many(
            instance=User,
            filters=[Filter(column="id", value=1)],
            select=["username", "id"],
            limit=1,
            offset=0,
            order=[Order(column="id", order="ASC")],
            include=[
                Include(
                    model=Post,
                    select=["id", "title"],
                    has="many",
                    limit=1,
                    offset=0,
                    order=[Order(column="id", order="ASC")],
                    include=[
                        Include(
                            model=Category,
                            select=["type", "id"],
                            has="many",
                            order=[Order(column="id", order="DESC")],
                            limit=2,
                            offset=0,
                        ),
                        Include(
                            model=User,
                            select=["username", "id"],
                            has="one",
                        ),
                    ],
                ),
            ],
        )
        assert user == [
            {
                "username": "@miller",
                "id": 1,
                "posts": [
                    {
                        "id": 1,
                        "title": "Hey",
                        "categories": [
                            {"type": "sport", "id": 4},
                            {"type": "tech", "id": 3},
                        ],
                        "user": {"username": "@miller", "id": 1},
                    }
                ],
            }
        ]

    def test_unknown_relations(self):
        from dataloom import (
            Loom,
            Model,
            Column,
            PrimaryKeyColumn,
            CreatedAtColumn,
            TableColumn,
            ForeignKeyColumn,
            ColumnValue,
            Include,
        )

        import pytest
        from dataloom.exceptions import UnknownRelationException

        sqlite_loom = Loom(dialect="sqlite", database="hi.db")

        class User(Model):
            __tablename__: TableColumn = TableColumn(name="users")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            name = Column(type="text", nullable=False, default="Bob")
            username = Column(type="varchar", unique=True, length=255)
            tokenVersion = Column(type="int", default=0)

        class Profile(Model):
            __tablename__: TableColumn = TableColumn(name="profiles")
            id = PrimaryKeyColumn(type="int", auto_increment=True)
            avatar = Column(type="text", nullable=False)
            userId = ForeignKeyColumn(
                User,
                maps_to="1-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Post(Model):
            __tablename__: TableColumn = TableColumn(name="posts")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            completed = Column(type="boolean", default=False)
            title = Column(type="varchar", length=255, nullable=False)
            # timestamps
            createdAt = CreatedAtColumn()
            # relations
            userId = ForeignKeyColumn(
                User,
                maps_to="1-N",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        class Category(Model):
            __tablename__: TableColumn = TableColumn(name="categories")
            id = PrimaryKeyColumn(
                type="int", auto_increment=True, nullable=False, unique=True
            )
            type = Column(type="varchar", length=255, nullable=False)

            postId = ForeignKeyColumn(
                Post,
                maps_to="N-1",
                type="int",
                required=True,
                onDelete="CASCADE",
                onUpdate="CASCADE",
            )

        conn, tables = sqlite_loom.connect_and_sync(
            [User, Profile, Post, Category], drop=True, force=True
        )

        userId = sqlite_loom.insert_one(
            instance=User,
            values=ColumnValue(name="username", value="@miller"),
        )

        profileId = sqlite_loom.insert_one(
            instance=Profile,
            values=[
                ColumnValue(name="userId", value=userId),
                ColumnValue(name="avatar", value="hello.jpg"),
            ],
        )
        for title in ["Hey", "Hello", "What are you doing", "Coding"]:
            sqlite_loom.insert_one(
                instance=Post,
                values=[
                    ColumnValue(name="userId", value=userId),
                    ColumnValue(name="title", value=title),
                ],
            )

        for cat in ["general", "education", "tech", "sport"]:
            sqlite_loom.insert_one(
                instance=Category,
                values=[
                    ColumnValue(name="postId", value=profileId),
                    ColumnValue(name="type", value=cat),
                ],
            )

        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_by_pk(
                Profile,
                pk=1,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=Category,
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The table "profiles" does not have relations "categories".'
        )
        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_many(
                Profile,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=Category,
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The table "profiles" does not have relations "categories".'
        )
        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_by_pk(
                Profile,
                pk=1,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=Category,
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The table "profiles" does not have relations "categories".'
        )
        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_all(
                Profile,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=Category,
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The table "profiles" does not have relations "categories".'
        )
        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_one(
                Profile,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=Category,
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The table "profiles" does not have relations "categories".'
        )
        with pytest.raises(UnknownRelationException) as exec_info:
            sqlite_loom.find_all(
                Profile,
                select=["avatar", "id"],
                include=[
                    Include(
                        model=User, has="many", include=[Include(model=Post, has="one")]
                    )
                ],
            )
        assert (
            str(exec_info.value)
            == 'The model "profiles" does not maps to "many" of "users".'
        )
        conn.close()

        conn.close()
