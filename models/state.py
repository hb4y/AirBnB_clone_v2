#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """Get the cities form the state.
            """
            cl = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cl.append(city)
            return cl
