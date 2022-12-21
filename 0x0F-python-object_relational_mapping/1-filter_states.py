#!/usr/bin/python3
"""
Get States that start with the letter n
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name REGEXP '^[n]'""")

    for i in c:
        print(i)
