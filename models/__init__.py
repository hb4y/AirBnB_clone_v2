#!/usr/bin/python3
"""
Create an instance of DBStorage and store it in the variable storage or create
an instance of FileStorage and store it in the variable storage. This according
to the HBNB_TYPE_STORAGE value.
"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
