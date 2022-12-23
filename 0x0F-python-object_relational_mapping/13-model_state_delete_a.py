#!/usr/bin/python3
"""
1: Take mysql username, mysql password, database, statename
2: deletes all State objects with a name containing the letter a
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%'))
    for instance in query:
        session.delete(instance)
    session.commit()
