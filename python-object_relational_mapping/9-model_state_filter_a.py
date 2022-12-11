#!/usr/bin/python3
"""This script lists all objects from state that
contain the letter a from the hbtn_0e_6_usa database"""

from sy import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

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
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Close session
    session.close()
