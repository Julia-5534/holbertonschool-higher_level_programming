#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # Set up database connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all cities and states
    cities = session.query(City).order_by(City.id).all()
    states = session.query(State).order_by(State.id).all()

    # Print cities grouped by state
    for state in states:
        cities_in_state = [city for city in cities if city.state_id == state.id]
        city_names = [city.name for city in cities_in_state]
        if city_names:
            print(f'{state.name}: {", ".join(city_names)}')
