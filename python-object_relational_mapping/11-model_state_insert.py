#!/usr/bin/python3
"""This script adds the State of "Louisiana" to the database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if _name_ == "_main_":
    # Create engine
    engine = cretae_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)
    # Create session
    Base.metadata.cretae_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    new_state = State(name+"Louisiana")
    session.add(new_state)
    state = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(state.id))
    session.commit()
    # Close session
    session.close()
