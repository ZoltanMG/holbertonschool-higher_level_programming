#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_city import City, Base
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    a = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for city, state in a:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
    session.close()
