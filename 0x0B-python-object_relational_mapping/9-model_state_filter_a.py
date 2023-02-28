#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create a new Engine instance.
    # The Engine is the starting point for any SQLAlchemy application.
    # It’s “home base” for the actual database and its DBAPI, delivered
    # to the SQLAlchemy application through a connection pool and a Dialect.
    # The connection pool provides a source of distinct Connection objects
    # that are owned by the application, for use with the database.
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # This is the function that allows you to interact with the database
    # In order to do so, you need a session, which is an abstraction
    # layer over the transactional system
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects that contain the letter a
    states = session.query(State).filter(State.name.like("%a%")).order_by(State.id)

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
