#!/usr/bin/python3
'''
A script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit changes
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
