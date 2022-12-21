#!/usr/bin/python3
"""
Get listed State in the command line
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT *
                FROM states""")
    for i in c:
        if i[1] == sys.argv[4]:
            print(i)
