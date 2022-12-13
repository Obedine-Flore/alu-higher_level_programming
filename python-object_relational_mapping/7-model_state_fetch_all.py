#!/usr/bin/python3
"""This script lists all State objectsfrom the hbtn_0e_6_usa database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    # Close session
    session.close()
