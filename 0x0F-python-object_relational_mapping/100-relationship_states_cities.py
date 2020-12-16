#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California", cities=[City(name="San Francisco")])
    session.add(state)
    session.commit()
    session.close()
