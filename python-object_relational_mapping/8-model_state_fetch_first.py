#!/usr/bin/python3



import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if _name_ == "_main_":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], arg[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.querry(Stae).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
