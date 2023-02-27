#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the connection engine to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)

    # Create all the tables in the database
    Base.metadata.create_all(engine)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states with 'a' in their names and delete them
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    # Commit the changes and close the session
    session.commit()
    session.close()
