#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    # Arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    # Dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, pwd, db), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query
    states = session.query(State).order_by(State.id).all()

    # Print
    for state in states:
        print("{}: {}".format(state.id, state.name))
