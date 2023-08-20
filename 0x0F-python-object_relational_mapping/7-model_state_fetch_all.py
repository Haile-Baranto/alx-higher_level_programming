#!/usr/bin/python3
"""
Lists all states from the database using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State objects in ascending order by id
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
