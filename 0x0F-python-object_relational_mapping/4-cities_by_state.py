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
    c.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON state_id = states.id
                ORDER BY cities.id""")
    [print(i) for i in c.fetchall()]
