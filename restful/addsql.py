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
    # item = Videoslist(1, 'NHK 钢琴秘话', 'http://120.25.207.78:8080/vod/nhk_piano.jpg',  'http://120.25.207.78:8080/vod/nhk_piano.m3u8', '日本力图加入西方文明国家行列的明治时代，与欧美列强比肩、自信满满的大正时代，以及动荡的昭和，钢琴声回荡在各个时代，今天讲述的是日本的钢琴秘话.')
    # db.session.add(item)


    # item2 = Videoslist(2, 'Steinway钢琴制造流程', 'http://120.25.207.78:8080/vod/steinway.jpg',  'http://120.25.207.78:8080/vod/steinway.m3u8', '史坦威公司（德语：Steinway & Sons）,或译施坦威公司,是一家美国及德国钢琴制造公司. 史坦威钢琴的价格一直是同行中最高的.音色明亮通透.')

    # db.session.add(item2)

    # item = Videoslist(3, 'bosendorfer钢琴制造流程', 'http://120.25.207.78:8080/vod/bosendorfer.jpg',  'http://120.25.207.78:8080/vod/bosendorfer.m3u8', '贝森朵夫钢琴厂是世界上最古老的钢琴制造商之一，该品牌由伊格纳茨·贝森朵夫于1828年在奥地利维也纳创立。其制造的三角钢琴以顶级的品质闻名于世。1839年，公司接受当时奥地利皇帝斐迪南一世的皇家委任状专门为皇室提供顶级三角钢琴。伊格纳茨去世后，他的儿子路德维希贝森朵夫于1859年接管公司的运营并于1860年将公司迁至新址，后来成为贝森朵夫音乐厅。从1872年至1913年关闭，它一直是维也纳首屈一指的音乐厅。1909年，公司被一名叫卡尔·胡特尔斯特拉瑟的商人买下，并于1966年售予晶宝国际公司。直至2002年，公司被奥地利Bawag P.S.K.银行购得，公司股权又回到了奥地利人手中。但是2007年12月20日，Bawag P.S.K.银行又把公司所有的股权卖给了日本的山叶株式会社。')
    # item2 = Videoslist(4, '电影mozart片段', 'http://120.25.207.78:8080/vod/mozart.jpg',  'http://120.25.207.78:8080/vod/mozart.m3u8', '在文艺复兴时期和巴洛克时期，大键琴是非常普及的乐器，它既可作为独奏乐器，亦可作为伴奏乐器；而在合奏（如最初期的室乐团）中亦担当重要的角色，可视为全队中的指挥。进入古典乐派初期，合奏的规模渐渐扩大，并慢慢形成为现代管弦乐团的雏型，一些著名的作曲家，例如海顿、C.P.E.巴赫，及早期的莫扎特管弦作品等，仍将大键琴放置在内，但由18世纪中后期开始，随着现代钢琴开始成型，大键琴在极短时间内遭淘汰，它的重要性一下子就取代掉，莫扎特中期作品起已经不再放入大键琴，而自贝多芬年代起，欧洲几乎再没有任何人会为大键琴写曲。大键琴就在音乐历史发展上近乎消失近150年，直至二十世纪中期，由于开始对早期音乐有较多的研究，大键琴才重新得到留意，亦开始重新生产及改良大键琴的结构')

    # db.session.add(item)
    # db.session.add(item2)
    # db.session.commit()

    item2 = Videoslist(5, '钢琴历史演进过程', 'http://120.25.207.78:8080/vod/Evolutionofthepiano.jpg',  'http://120.25.207.78:8080/vod/Evolutionofthepiano.m3u8', '钢琴的故事在1709年在意大利帕多瓦开始，在大键琴制造商名为Bartolomeo di Francesco Cristofori（1655-1731）的店里。 许多其他弦乐和键盘乐器都在钢琴之前，导致我们今天所知道的乐器的发展。本片简述钢琴历史演进过程')

    db.session.add(item2)
    db.session.commit()

@manager.command
def query_videos():
    videos = Videoslist.query.all()
    for item in videos:
        print item

if __name__ == '__main__':
    manager.run()
