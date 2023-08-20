#!/usr/bin/python3
"""
Lists all State objects containing the letter a from the
database hbtn_0e_6_usa.
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

    # Query State objects containing the letter 'a' and sort by id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
