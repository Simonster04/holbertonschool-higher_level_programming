#!/usr/bin/python3
"""
 Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    newstate = State(name="Louisiana")
    session.add(newstate)
    state = session.query(State).filter(State.name.like(newstate.name)).first()
    print(state.id)
    session.commit()
    session.close()
