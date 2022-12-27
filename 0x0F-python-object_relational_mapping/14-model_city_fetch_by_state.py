#!/usr/bin/python3
"""
1: Take mysql username, mysql password, database, statename
2: deletes all State objects with a name containing the letter a
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).\
        filter(City.state_id == State.id).order_by(City.id)
    for cities, states in query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
