#!/usr/bin/python3
"""
This module  prints the
first State object from the
database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state(username, password, db_name, state_name):
    """
    Finds and prints the ID of a State object
    with the given name from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """

    try:
        # Create a MySQL database engine
        engine = create_engine(
            f'mysql+mysqldb://{username}'
            f':{password}@localhost:3306/{db_name}')

        # Create a Session class
        Session = sessionmaker(bind=engine)

        # Create a Session instance
        session = Session()

        # Query for the State object with the specified name
        state = session.query(State).filter_by(name=state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session when done
        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py \
        <username> <password>\
        <db_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Execute the function to find the state
    find_state(username, password, db_name, state_name)
