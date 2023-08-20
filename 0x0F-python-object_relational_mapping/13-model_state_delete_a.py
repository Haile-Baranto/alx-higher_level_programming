#!/usr/bin/python3
'''
A script that deletes all State objects with a name containing the
letter "a" from the database hbtn_0e_6_usa.
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

    # Query and delete State objects with names containing "a"
    states_to_delete = session.query(State).filter(State.name.
                                                   like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
