#coding=utf-8

from flask_script import Manager
from app import app, db
from models import Pianonews
from models import Videoslist
from models import Flashmoblist
from models import Bachinventioninfo


manager = Manager(app)


@manager.command
def save_pianonews():
    user = Pianonews(5, 'Yamaha 古典钢琴', '/images/yamaha_1.jpeg')
    db.session.add(user)

    user2 = Pianonews(6, 'Kawai 古典钢琴', '/images/kawai_1.jpeg')

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
    item1 = Videoslist('从大键琴到现在钢琴(上集)',
                       '/vod/pianoHistory1.jpeg',\
                       '/vod/pianoHistory1.m3u8',\
                       '简述钢琴的进化过程')

    item2 = Videoslist('从大键琴到现在钢琴(下集)',
                       '/vod/pianoHistory2.jpeg',\
                       '/vod/pianoHistory2.m3u8',\
                       '简述钢琴的进化过程')

    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()

@manager.command
def query_videos():
    videos = Videoslist.query.all()
    for item in videos:
        print item

@manager.command
def save_flashmob():
     item = Flashmoblist('《龙猫》快闪 宫崎骏电影',
                         '/vod/longMiao.jpeg',
                         '/vod/longMiao.mp4',
                         '东京街头的龙猫主题曲快闪')

     db.session.add(item)

     item2 = Flashmoblist('饮酒歌"茶花女"',
                         '/vod/LaTraviata.jpeg',
                         '/vod/LaTraviata.mp4',
                         '作于1853年。为所作的歌剧《茶花女》中第一幕唱段。\
                         当时男主角阿尔弗雷多在女主人公薇奥莱塔举行的宴会中举杯祝贺，\
                         用歌声表达对薇奥莱塔的爱慕之心，薇奥莱塔也在祝酒时作了巧妙回答。')

     db.session.add(item2)


     item3 = Flashmoblist('欢乐颂 快闪',
                         '/vod/Odetojoy.jpeg',
                         '/vod/Odetojoy.mp4',
                         '该作品是古典音乐中最为人所熟知的作品之一，亦属于贝多芬最杰出的作品。')

     db.session.add(item3)

     item4 = Flashmoblist('<You Raise Me Up> 街头快闪Martin Hurkens',
                         '/vod/youRaiseMeup.jpeg',
                         '/vod/youRaiseMeup.mp4',
                         '2010年荷兰好声音(Holland’s Got Talent)冠军\
                         MartinHurkens!他生于1953年12月16日。\
                         2010年,以57岁祖父级的年龄参赛,并夺得冠军,优雅的男高音,令众人惊艳。\
                         他追求梦想的勇气令人佩服不已,他的声音可说是天使的声音洗涤人心!\
                         寒街里的歌声~听了令人感动!')

     db.session.add(item4)

     item5 = Flashmoblist('歌德堡变奏曲第一变奏',
                          '/vod/goldbergVar1.jpeg',
                          '/vod/goldbergVar1.mp4',
                          '哥德堡变奏被视为巴赫作品中最重要的变奏曲之一, \
                          1955年加拿大钢琴家格伦·古尔德将其选作自己的第一张录音作品。')

     db.session.add(item5)

     db.session.commit()

@manager.command
def query_flashmob():
    flashs = Flashmoblist.query.all()
    for item in flashs:
        print item



@manager.command
def save_bachinvention():
    for i in range(772, 786):
            name = "bwv"+str(i)
            imageName = name + '.jpg'
            videoName = name + '.mp4'
            item = Bachinventioninfo('Invention ' + name,
                                     '/vod/' + imageName,
                                     '/vod/' + videoName,
                                     'Johann Sebastian Bach, inventions ' + name)

            db.session.add(item)
            db.session.commit()


@manager.command
def query_bachinvention():
    info = Bachinventioninfo.query.all()
    for item in info:
        print item

if __name__ == '__main__':
    manager.run()
