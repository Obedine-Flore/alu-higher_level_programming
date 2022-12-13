#!/usr/bin/python3
"""This script changes the name of a State object
from the database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "_main_":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)
    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    
    # Close session
    session.commit()
    session.close()
