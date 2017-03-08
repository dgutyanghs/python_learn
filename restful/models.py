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




