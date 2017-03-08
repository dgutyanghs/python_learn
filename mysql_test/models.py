# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)


#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email


#     def __repr__(self):
#         return '<User %r>' % (self.name)
    

import MySQLdb
from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String)


    def __init__ (self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name


    def __repr__(self):
        return "id:{} - name:{}".format(self.user_id, self.user_name)



