#!/usr/bin/python3
'''
A script that lists the id of a State object with a given name
from the database hbtn_0e_6_usa.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database\
              state_name".format(sys.argv[0]))
        exit(1)

    username, password, database, state_name = sys.argv[1],\
        sys.argv[2], sys.argv[3], sys.argv[4]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given state_name
    state = session.query(State).filter_by(name=state_name).first()

    # Print the result
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
