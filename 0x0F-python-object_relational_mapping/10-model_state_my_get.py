#!/usr/bin/python3
"""
1: Take mysql username, mysql password and database
2: Fetch provided stated in the command lin
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
    get_id = session.query(State.id).filter(State.name == sys.argv[4]).first()
    if get_id is None:
        print("Not found")
    else:
        print(get_id[0])
