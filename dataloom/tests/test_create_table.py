# class TestCreatingTablePG:
#     def test_2_pk_error(self):
#         from dataloom.db import Database
#         from dataloom.model.column import Column, PrimaryKeyColumn
#         from dataloom.model.model import Model
#         from dataloom.keys import password, database, user
#         import pytest

#         db = Database(database, password=password, user=user)
#         conn = db.connect()

#         class User(Model):
#             __tablename__ = "users"
#             _id = PrimaryKeyColumn(type="bigint", auto_increment=True)
#             id = PrimaryKeyColumn(type="bigint", auto_increment=True)
#             username = Column(type="text", nullable=False, default="Hello there!!")
#             name = Column(type="varchar", unique=True, length=255)

#         with pytest.raises(Exception) as exc_info:
#             db.sync([User], drop=True, force=True)

#         assert (
#             str(exc_info.value)
#             == 'You have defined many field as primary keys which is not allowed. Fields ("_id", "id") are primary keys.'
#         )
#         conn.close()

#     def test_no_pk_error(self):
#         from dataloom.db import Database
#         from dataloom.model.column import Column
#         from dataloom.model.model import Model
#         from dataloom.keys import password, database, user
#         import pytest

#         db = Database(database, password=password, user=user)
#         conn = db.connect()

#         class User(Model):
#             __tablename__ = "users"
#             username = Column(type="text", nullable=False, default="Hello there!!")
#             name = Column(type="varchar", unique=True, length=255)

#         with pytest.raises(Exception) as exc_info:
#             db.sync([User], drop=True, force=True)

#         assert str(exc_info.value) == "Your table does not have a primary key column."
#         conn.close()

#     def test_table_name(self):
#         from dataloom.db import Database
#         from dataloom.model.column import Column, PrimaryKeyColumn
#         from dataloom.model.model import Model
#         from dataloom.keys import database, password, user

#         db = Database(database, password=password, user=user)
#         conn = db.connect()

#         class Todos(Model):
#             id = PrimaryKeyColumn(type="bigint", auto_increment=True)
#             completed = Column(type="boolean", default=False)
#             title = Column(type="varchar", length=255, nullable=False)

#         class User(Model):
#             __tablename__ = "users"
#             username = Column(type="text", nullable=False, default="Hello there!!")
#             name = Column(type="varchar", unique=True, length=255)

#         assert User._get_name() == '"users"'
#         assert Todos._get_name() == '"todos"'
#         conn.close()

#     def test_connect_sync(self):
#         from dataloom.db import Database
#         from dataloom.keys import password, database, user
#         from dataloom.model.model import Model
#         from dataloom.model.column import Column, PrimaryKeyColumn

#         class User(Model):
#             __tablename__ = "users"
#             id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
#             username = Column(type="text", nullable=False)
#             name = Column(type="varchar", unique=False, length=255)

#         class Post(Model):
#             __tablename__ = "posts"

#             id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
#             title = Column(type="text", nullable=False, default="Hello there!!")

#         db = Database(database, password=password, user=user)
#         conn, tables = db.connect_and_sync([User, Post], drop=True, force=True)

#         assert len(tables) == 2
#         assert conn.status == 1
#         assert sorted(tables) == sorted(["users", "posts"])

#         conn.close()

#     def test_syncing_tables(self):
#         from dataloom.db import Database
#         from dataloom.keys import password, database, user
#         from dataloom.model.model import Model
#         from dataloom.model.column import Column, PrimaryKeyColumn

#         class User(Model):
#             __tablename__ = "users"
#             id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
#             username = Column(type="text", nullable=False)
#             name = Column(type="varchar", unique=False, length=255)

#         class Post(Model):
#             __tablename__ = "posts"

#             id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
#             title = Column(type="text", nullable=False, default="Hello there!!")

#         db = Database(database, password=password, user=user)
#         conn = db.connect()
#         tables = db.sync([User, Post], drop=True, force=True)
#         assert len(tables) == 2
#         assert tables == ["users", "posts"]
#         conn.close()
