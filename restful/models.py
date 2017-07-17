import MySQLdb
from app import db

class Pianonews(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    icon = db.Column(db.String)
    
    def __init__ (self, index, title, icon):
        self.index = index
        self.title = title
        self.icon = icon


    def __repr__ (self):
        return "index:{} title:{} icon:{}".format(self.index, self.title, self.icon)

    @property
    def serialize(self):
        return {
            'index': self.index,
            'title': self.title,
            'icon': self.icon
        }

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]



class Videoslist(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    cover = db.Column(db.String)
    mp4_url = db.Column(db.String)
    desc = db.Column(db.String)

    
    def __init__ (self, title, cover, mp4_url, desc, index = None):
    # def __init__ (self, index, title, cover, mp4_url, desc):
        self.index = index
        self.title = title
        self.cover = cover
        self.mp4_url = mp4_url
        self.desc = desc
         


    def __repr__ (self):
        return "index:{} title:{} cover:{} mp4_url:{} desc:{}".format(self.index, self.title, self.cover, self.mp4_url, self.desc)

    @property
    def serialize(self):
        return {
            'index': self.index,
            'title': self.title,
            'cover': self.cover,
            'mp4_url':self.mp4_url,
            'desc':self.desc
        }

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]


class Flashmoblist(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    cover = db.Column(db.String)
    mp4_url = db.Column(db.String)
    desc = db.Column(db.String)

    
    def __init__ (self, title, cover, mp4_url, desc, index = None):
    # def __init__ (self, index, title, cover, mp4_url, desc):
        self.index = index
        self.title = title
        self.cover = cover
        self.mp4_url = mp4_url
        self.desc = desc
         


    def __repr__ (self):
        return "index:{} title:{} cover:{} mp4_url:{} desc:{}".format(self.index, self.title, self.cover, self.mp4_url, self.desc)

    @property
    def serialize(self):
        return {
            'index': self.index,
            'title': self.title,
            'cover': self.cover,
            'mp4_url':self.mp4_url,
            'desc':self.desc
        }

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]

class Bachinventioninfo(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    cover = db.Column(db.String)
    mp4_url = db.Column(db.String)
    desc = db.Column(db.String)

    
    def __init__ (self, title, cover, mp4_url, desc, index = None):
    # def __init__ (self, index, title, cover, mp4_url, desc):
        self.index = index
        self.title = title
        self.cover = cover
        self.mp4_url = mp4_url
        self.desc = desc
         


    def __repr__ (self):
        return "index:{} title:{} cover:{} mp4_url:{} desc:{}".format(self.index, self.title, self.cover, self.mp4_url, self.desc)

    @property
    def serialize(self):
        return {
            'index': self.index,
            'title': self.title,
            'cover': self.cover,
            'mp4_url':self.mp4_url,
            'desc':self.desc
        }

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]

