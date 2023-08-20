#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects
from the database `hbtn_0e_101_usa`.
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

    # Query all State objects with their corresponding City objects
    data = session.query(State).order_by(State.id).all()

    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
