#!/usr/bin/python3
"""
1: Take mysql username, mysql password and database
2: Fetch all the rows that contain the letter a
"""
import sys
import MySQLdb
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT states.name, cities.id, cities.name
                FROM cities
                JOIN states ON state_id = states.id""")
    for row in c:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
