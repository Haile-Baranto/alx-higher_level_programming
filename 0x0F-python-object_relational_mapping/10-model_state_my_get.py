#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} username password database\
              state_name".format(argv[0]))
        exit(1)

    username, password, database, state_name = argv[1],
    argv[2], argv[3], argv[4]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given state_name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
