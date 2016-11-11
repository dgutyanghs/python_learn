# 1. 未使用ORM
# import pymongo


# def get_coll():

#     # client = pymongo.mongo_client('127.0.0.1', 27017)
#     client = pymongo.MongoClient('127.0.0.1', 27017)
#     db = client.jikexueyuan
#     user = db.user_collection

#     return user


# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def save(self):
#         user = {"name":self.name, "email":self.email}
#         coll = get_coll()
#         id = coll.insert(user)
#         print (id)

#     @staticmethod
#     def query_users():
#         users = get_coll().find()
#         return users





#  2. 使用ORM

from app import db

class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def __str__(self):
        return "name:{} -- email:{}".format(self.name, self.email)


