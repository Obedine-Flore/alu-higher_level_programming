#!/usr/bin/python3
"""This script lists all State objects from hbtn_0e_6_usa database"""

import sys
import sqlalchemy
from model-stae import Base, State
form sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    my_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)

    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    for state in session.querry(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
