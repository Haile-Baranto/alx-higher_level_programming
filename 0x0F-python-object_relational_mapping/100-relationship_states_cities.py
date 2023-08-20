#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State with the City and add them to the session
    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
