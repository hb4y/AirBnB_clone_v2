#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from models.base_model import Base
from models.base_model import BaseModel


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
