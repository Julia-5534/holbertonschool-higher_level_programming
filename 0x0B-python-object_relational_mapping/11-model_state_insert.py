#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Start connection to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(mysql_user, mysql_pwd, db_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new state
    new_state = State(name="Louisiana")

    # Add state to session and commit changes to database
    session.add(new_state)
    session.commit()

    # Print new state id
    print(new_state.id)
