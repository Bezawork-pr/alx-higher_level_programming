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
    not_texas = session.query(State).\
        order_by(State.id).filter(State.name.like('%a%'))
    for row in not_texas:
        print("{}: {}".format(row.id, row.name))
