# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
from popianotest.items import PopianotestItem
import pdb

class PopianotestPipeline(object):
    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        db = "popdb"
        user = "root"
        passwd = "password"
        self.conn = MySQLdb.connect(host=host, user = user, passwd = passwd, db = db, port= port, charset="utf8", use_unicode = True)
        self.cursor = self.conn.cursor()
        # pdb.set_trace()
    def process_item(self, item, spider):    
        # pdb.set_trace()
        try:
            
            print "commit db !!!!(%d,%s)" % (item['link_num'], item['link'])  
            self.cursor.execute("INSERT INTO poptable (link_num, link) VALUES (%s, %s)", (item['link_num'], item['link'].encode('utf-8')))
            self.conn.commit()

        except MySQLdb.Error, e:
            print "!!!Error %d: %s" % (e.args[0], e.args[1])


        return item
