#!/usr/bin/python3
"""
This module  prints the
first State object from the
database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def print_first_state(user, passwd, db):
    """
    - prints the first State object from
    - the database hbtn_0e_6_usa
    """

    try:  # establish a connection with db
        engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{db}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State)\
            .filter(State.name.like('%a%'))\
            .order_by(State.id).all()
        for state in states:
            print(f'{state.id}: {state.name}')
        session.close()
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    print_first_state(user, passwd, db)
