#!/usr/bin/python3
'''
A script that changes the name of a State object in the database hbtn_0e_6_usa.
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

    # Query the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Change the name of the state
    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
