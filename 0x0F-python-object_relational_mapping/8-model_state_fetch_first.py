#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
if __name__ == "__main__":
    """
    cript that prints the first State object from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()
    if (result):
        print("{}: {}".format(result.id, result.name))

    session.close()
