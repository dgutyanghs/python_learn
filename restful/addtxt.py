#coding=utf-8

from flask_script import Manager
from app import app, db
from models import Pianonews
from models import Videoslist
from app import json

manager = Manager(app)


@manager.command
def save_videos():
    item2 = Videoslist(5, '钢琴历史演进过程', 'http://120.25.207.78:8080/vod/Evolutionofthepiano.jpg',  'http://120.25.207.78:8080/vod/Evolutionofthepiano.m3u8', '钢琴的故事在1709年在意大利帕多瓦开始，在大键琴制造商名为Bartolomeo di Francesco Cristofori（1655-1731）的店里。 许多其他弦乐和键盘乐器都在钢琴之前，导致我们今天所知道的乐器的发展。本片简述钢琴历史演进过程')

    db.session.add(item2)
    db.session.commit()

@manager.command
def query_videos():
    videos = Videoslist.query.all()
    for item in videos:
        print item

@manager.command
def save_video_item(item):
    video = Videoslist(item["title"], item["cover"], item["link"], item["desc"])
    db.session.add(video)
    db.session.commit()

@manager.command
def add_jsonfile(name):
    with open(name, "r") as f :
        alldata = json.load(f)
        items = alldata["videos"]
        for item in items:
           save_video_item(item) 



if __name__ == '__main__':
    manager.run()
