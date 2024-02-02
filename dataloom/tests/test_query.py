# class TestQueryingPG:
#     def test_querying_data(self):
#         from dataloom.db import Database
#         from dataloom.model.column import Column, PrimaryKeyColumn
#         from dataloom.model.model import Model
#         from dataloom.keys import password, database, user

#         db = Database(database, password=password, user=user)
#         conn = db.connect()

#         class User(Model):
#             __tablename__ = "users"
#             id = PrimaryKeyColumn(type="bigint", nullable=False, auto_increment=True)
#             username = Column(type="text", nullable=False, default="Hello there!!")
#             name = Column(
#                 type="varchar",
#                 unique=True,
#                 length=255,
#             )

#             def __str__(self) -> str:
#                 return f"User<{self.id}>"

#             def __repr__(self) -> str:
#                 return f"User<{self.id}>"

#             def to_dict(self):
#                 return {"id": self.id, "name": self.name, "username": self.username}

#         db.sync([User], drop=True, force=True)

#         user = User(name="Crispen", username="heyy")
#         db.create(user)
#         users = db.find_all(User)
#         me = db.find_by_pk(User, 1).to_dict()
#         her = db.find_by_pk(User, 2)
#         many_0 = db.find_many(User, {"id": 5})
#         many_1 = db.find_many(User, {"id": 1})
#         many_2 = db.find_many(User, {"id": 1, "name": "Crispen"})
#         many_3 = db.find_many(User, {"id": 5, "username": "hey"})
#         many_4 = db.find_many(User, {"name": "Crispen", "username": "heyy"})

#         one_0 = db.find_one(User, {"id": 5})
#         one_1 = db.find_one(User, {"id": 1})
#         one_2 = db.find_one(User, {"id": 1, "name": "Crispen"})
#         one_3 = db.find_one(User, {"id": 5, "username": "hey"})
#         one_4 = db.find_one(User, {"name": "Crispen", "username": "heyy"})

#         assert [u.to_dict() for u in users] == [
#             {"id": 1, "name": "Crispen", "username": "heyy"}
#         ]
#         assert [u.to_dict() for u in many_0] == []
#         assert [u.to_dict() for u in many_3] == []
#         assert [u.to_dict() for u in many_1] == [
#             {"id": 1, "name": "Crispen", "username": "heyy"}
#         ]
#         assert [u.to_dict() for u in many_2] == [
#             {"id": 1, "name": "Crispen", "username": "heyy"}
#         ]
#         assert [u.to_dict() for u in many_4] == [
#             {"id": 1, "name": "Crispen", "username": "heyy"}
#         ]

#         assert one_0 is None
#         assert one_3 is None
#         assert one_1.to_dict() == {"id": 1, "name": "Crispen", "username": "heyy"}
#         assert one_2.to_dict() == {"id": 1, "name": "Crispen", "username": "heyy"}
#         assert one_4.to_dict() == {"id": 1, "name": "Crispen", "username": "heyy"}
#         assert her is None
#         conn.close()
