#!/usr/bin/python3


import sys
import sqlalchemy
from model-stae import Base, State
form sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if _name_ == "_main_":
    my_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.querry(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
