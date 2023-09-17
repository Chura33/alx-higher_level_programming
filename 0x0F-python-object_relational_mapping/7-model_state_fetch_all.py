#!/usr/bin/python3
""" This module lists all states in DB"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def list_states(user, password, db_name):
    """ This function lists all states"""

    try:
        engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@localhost/'
            f'{db_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).all()
        for state in states:
            print(f"{state.id}: {state.name}")
        session.close()
    except SQLAlchemyError as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)  # Exit the program with an error code


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <user> <password> <db_name>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(user, password, db_name)
