# 1.未使用ORM
# # encodeing = utf-8

# from flask_script import Manager
# from app import app

# from models import User


# manager = Manager(app)

# @manager.command
# def save():
#     user = User('jike', 'helloworld@qq.com')
#     user.save()

# @manager.command
# def query_users():
#     users = User.query_users()
#     for user in users:
#         print (user)

# if __name__  == '__main__':
#     manager.run()




# encodeing = utf-8
# 2. 使用ORM

from flask_script import Manager
from app import app

from models import User


manager = Manager(app)

@manager.command
def save():
    # user = User('jike', 'helloworld@qq.com')
    # user.save()
    user = User(name = 'hello2', email = 'hello2@qq.com')
    user.save()

@manager.command
def query_users():
    # users = User.query_users()
    users = User.objects.all()
    for user in users:
        print (user)

if __name__  == '__main__':
    manager.run()
