#!/usr/bin/python3
"""
Creates a State with a City using SQLAlchemy relationships
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create the tables defined in the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create a new State object named "California"
    new_state = State(name='California')

    # Create a new City object named "San Francisco"
    new_city = City(name='San Francisco')

    # Associate the new City with the new State using relationships
    new_state.cities.append(new_city)

    # Add the State object to the session and commit the changes
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
