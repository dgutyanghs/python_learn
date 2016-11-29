#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

# try:
#     host = "127.0.0.1"
#     port = 3306
#     db = "popdb"
#     user = "root"
#     password = "password"

#     con = mdb.connect(host=host, user = user, passwd = password, db = db, port= port, charset="utf8" )

#     cur = con.cursor()
#     cur.execute("SELECT VERSION()")

#     ver = cur.fetchone()
#     print "Database version : %s " % ver
    
# except mdb.Error, e:
#     print "Error %d: %s" % (e.args[0],e.args[1])
#     sys.exit(1)

# finally:    
#     if con:    
#         con.close()


host = "127.0.0.1"
port = 3306
db = "popdb"
user = "root"
password = "password"

con = mdb.connect(host=host, user = user, passwd = password, db = db, port= port, charset="utf8" )

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

