# # encodeing = utf-8
# 1.未使用ORM

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
    user = User(name = 'hello3', email = 'hello3@qq.com')
    user.save()

@manager.command
def query_users():
    # users = User.query_users()
    users = User.objects.all()
    for user in users:
        print (user)

@manager.command
def find_user(var):
    # user = User.objects(__raw__ = {'name':<var>})
    # user = User.objects(name='hello3', email = 'hello3@qq.com')
    #查询具体某个user 
    user = User.objects(name=var)
    print (user)
    # users = User.objects.all()
    # for user in users:
    #     if user.name == name:
    #         print (user)

if __name__  == '__main__':
    manager.run()
