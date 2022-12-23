#!/usr/bin/python3
"""
1: Take mysql username, mysql password and database
2: Fetch the row in table states
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_element = session.query(State.id, State.name).\
        order_by(State.id).first()
    if State is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_element.id, first_element.name))
