#coding=utf-8

from flask_script import Manager
from app import app, db
from models import Pianonews


manager = Manager(app)


@manager.command
def save():
    user = Pianonews(3, 'Yamaha 古典钢琴', 'https://120.25.207.78/images/yamaha_1.jpg')
    db.session.add(user)

    user2 = Pianonews(4, 'Kawai 古典钢琴', 'https://120.25.207.78/images/kawai_1.jpg')

    db.session.add(user2)
    db.session.commit()



@manager.command
def query_all():
    news = Pianonews.query.all()
    for u in users:
        print u

if __name__ == '__main__':
    manager.run()
