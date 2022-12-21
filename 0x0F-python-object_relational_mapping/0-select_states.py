#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(host=sys.argv[1], port=3306,
                     password=sys.argv[2], database=sys.argv[3])
c = db.cursor()
c.execute("""SELECT * FROM states""")
for i in c:
    print(i)
