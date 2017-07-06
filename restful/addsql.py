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
     # item = Flashmoblist('歌德堡变奏曲第1变奏',
     #                     'http://120.25.207.78:8080/vod/goldbergVar1.jpg',
     #                     'http://120.25.207.78:8080/vod/goldbergVar1.mp4',
     #                     '哥德堡变奏被视为巴赫作品中最重要的变奏曲之一, \
     #                     1955年加拿大钢琴家格伦·古尔德将其选作自己的第一张录音作品。')

     item = Flashmoblist('《龙猫》快闪 宫崎骏电影',
                         'http://120.25.207.78:8080/vod/longMiao.jpg',
                         'http://120.25.207.78:8080/vod/longMiao.mp4',
                         '东京街头的龙猫主题曲快闪')

     db.session.add(item)

     item2 = Flashmoblist('饮酒歌"茶花女"',
                         'http://120.25.207.78:8080/vod/LaTraviata.jpg',
                         'http://120.25.207.78:8080/vod/LaTraviata.mp4',
                         '作于1853年。为所作的歌剧《茶花女》中第一幕唱段。\
                         当时男主角阿尔弗雷多在女主人公薇奥莱塔举行的宴会中举杯祝贺，\
                         用歌声表达对薇奥莱塔的爱慕之心，薇奥莱塔也在祝酒时作了巧妙回答。')

     db.session.add(item2)


     item3 = Flashmoblist('欢乐颂 快闪',
                         'http://120.25.207.78:8080/vod/Odetojoy.jpg',
                         'http://120.25.207.78:8080/vod/Odetojoy.mp4',
                         '该作品是古典音乐中最为人所熟知的作品之一，亦属于贝多芬最杰出的作品。')

     db.session.add(item3)

     item4 = Flashmoblist('<You Raise Me Up> 街头快闪Martin Hurkens',
                         'http://120.25.207.78:8080/vod/youRaiseMeup.jpg',
                         'http://120.25.207.78:8080/vod/youRaiseMeup.mp4',
                         '2010年荷兰好声音(Holland’s Got Talent)冠军\
                         MartinHurkens!他生于1953年12月16日。\
                         2010年,以57岁祖父级的年龄参赛,并夺得冠军,优雅的男高音,令众人惊艳。\
                         他追求梦想的勇气令人佩服不已,他的声音可说是天使的声音洗涤人心!\
                         寒街里的歌声~听了令人感动!')

     db.session.add(item4)

     db.session.commit()

@manager.command
def query_flashmob():
    flashs = Flashmoblist.query.all()
    for item in flashs:
        print item

if __name__ == '__main__':
    manager.run()
