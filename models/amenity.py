#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    name = Column(String(128), nullable=False)
