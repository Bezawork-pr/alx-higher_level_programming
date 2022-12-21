#!/usr/bin/python3
"""
Get username, password and database from command line
print all rows from the database
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                        password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    for i in c:
        print(i)
