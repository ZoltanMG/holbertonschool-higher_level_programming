#!/usr/bin/python3
"""
script that lists all State objects from
the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id)[0]
    print('{}: {}'.format(first_state.id, first_state.name))
    session.close()
