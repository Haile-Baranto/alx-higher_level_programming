#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(connection.format(username, password, database),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    query = session.query(State, City).\
        filter(City.state_id == State.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
