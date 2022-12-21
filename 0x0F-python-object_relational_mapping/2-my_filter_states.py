#!/usr/bin/python3
"""
Get listed State in the command line
and print
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT *
                FROM states
                WHERE name = '{}'""".format(sys.argv[4]))
    [print(i) for i in c.fetchall()]
