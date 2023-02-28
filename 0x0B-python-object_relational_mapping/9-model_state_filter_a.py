#!/usr/bin/python3
""" Task 9 """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects that contain the letter a
    states = session.query(State).filter(State.name.like("%a%")).order_by(State.id)

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
