# encodeing = utf-8

from flask_script import Manager
from app import app

from models import User


manager = Manager(app)

@manager.command
def save():
    user = User('jike', 'helloworld@qq.com')
    user.save()

@manager.command
def query_users():
    users = User.query_users()
    for user in users:
        print (user)

if __name__  == '__main__':
    manager.run()


