#coding=utf-8

from flask_script import Manager
from app import app, db
from models import Pianonews
from models import Videoslist


manager = Manager(app)


@manager.command
def save_pianonews():
    user = Pianonews(5, 'Yamaha 古典钢琴', 'https://120.25.207.78/images/yamaha_1.jpg')
    db.session.add(user)

    user2 = Pianonews(6, 'Kawai 古典钢琴', 'https://120.25.207.78/images/kawai_1.jpg')

    db.session.add(user2)
    db.session.commit()



@manager.command
def query_pianonews():
    news = Pianonews.query.all()
    for u in news:
        # print u
        pass

@manager.command
def save_videos():
    item2 = Videoslist('钢琴历史演进过程', 'http://120.25.207.78:8080/vod/Evolutionofthepiano.jpg',  'http://120.25.207.78:8080/vod/Evolutionofthepiano.m3u8', '钢琴的故事在1709年在意大利帕多瓦开始，在大键琴制造商名为Bartolomeo di Francesco Cristofori（1655-1731）的店里。 许多其他弦乐和键盘乐器都在钢琴之前，导致我们今天所知道的乐器的发展。本片简述钢琴历史演进过程')

    db.session.add(item2)
    db.session.commit()

@manager.command
def query_videos():
    videos = Videoslist.query.all()
    for item in videos:
        print item

if __name__ == '__main__':
    manager.run()
