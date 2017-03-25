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
    item = Videoslist(1, 'NHK 钢琴秘话', 'http://120.25.207.78:8080/vod/nhk_piano.jpg',  'http://120.25.207.78:8080/vod/nhk_piano.u3m8', '日本力图加入西方文明国家行列的明治时代，与欧美列强比肩、自信满满的大正时代，以及动荡的昭和，钢琴声回荡在各个时代，今天讲述的是日本的钢琴秘话.')
    # item = Videoslist(101, '中国钢琴', 'httptest','httpvideo','descvideos')
    db.session.add(item)


    item2 = Videoslist(2, 'Steinway钢琴制造流程', 'http://120.25.207.78:8080/vod/steinway.jpg',  'http://120.25.207.78:8080/vod/steinway.u3m8', '史坦威公司（德语：Steinway & Sons）,或译施坦威公司,是一家美国及德国钢琴制造公司. 史坦威钢琴的价格一直是同行中最高的.音色明亮通透.')

    # db.session.add(item2)
    db.session.commit()

@manager.command
def query_videos():
    videos = Videoslist.query.all()
    for item in videos:
        print item

if __name__ == '__main__':
    manager.run()
