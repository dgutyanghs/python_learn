#coding=utf-8

from flask_script import Manager
from app import app, db
from models import Pianonews
from models import Videoslist
from models import Flashmoblist


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
        print u
        # pass

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

@manager.command
def save_flashmob():
    # item = Flashmoblist('布基上校进行曲','http://120.25.207.78:8080/vod/Colonel Bogey.jpg', 'http://120.25.207.78:8080/vod/Colonel Bogey.mp4', '《布基上校进行曲》（英语：Colonel Bogey March）为有“英国进行曲之王”（The British March King）之称的军官作曲家肯尼斯·约瑟夫·阿尔福特（Kenneth Joseph Alford）[1]创作于1914年，后来于1957年被电影《桂河大桥》采用并改编为电影主题曲《桂河进行曲》（The River Kwai March），此曲也随着该部电影的成功而广为世人所熟悉。')

    item2 = Flashmoblist('魔笛 女高音花腔','http://120.25.207.78:8080/vod/Magic Flute.jpg', 'http://120.25.207.78:8080/vod/Magic Flute.mp4', '《仇恨的火焰(Der Hölle Rache)》是一首极为华丽的花腔咏叹调，可以说是花腔女高音咏叹调史上数一数二的名曲')
    # db.session.add(item)
    db.session.add(item2)
    db.session.commit()

@manager.command
def query_flashmob():
    flashs = Flashmoblist.query.all()
    for item in flashs:
        print item

if __name__ == '__main__':
    manager.run()
