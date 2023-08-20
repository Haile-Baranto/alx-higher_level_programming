#!/usr/bin/python3
"""
This script adds a new City object to the State object
"California" in the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Construct the database URI
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create a connection to the database
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Create a new State object "California" and City object "San Francisco"
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')

    # Associate the City object with the State object
    cal_state.cities.append(sfr_city)

    # Add the State object to the session and commit changes
    session.add(cal_state)
    session.commit()

    # Close the session
    session.close()
