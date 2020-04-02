#!/usr/bin/python3
"""This is the state class"""
import os
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",  backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get the cities form the state.
            """
            all_cities = models.engine.all(City)
            st_cities = []
            for k, city in all_cities.items():
                if city.state_id == self.id:
                    st_cities.append(city)
            return st_cities
