#!/usr/bin/python3
"""This script prints objects in State with the name
as an argument"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if _name_ == "_main_":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)
    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    states = session.query(State).filter(State.name == argv[4]).all()
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
   # Close session
   session.close()
