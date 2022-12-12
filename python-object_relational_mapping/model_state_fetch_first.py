#!/usr/bin/python3
""" This script lists all State objects from hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if _name_ == "_main_":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argn[2], sys.argv[3]),
                            pool_pre_ping=True)

    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    state = session.query(State).first()
    if satte is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # Close session
    session.close()
