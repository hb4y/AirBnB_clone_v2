#!/usr/bin/python3
"""Defines unnittests for dbstorage
"""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                 "Don´t run if is file storage")
class TestDBStorage(unittest.TestCase):
    """
        Test cases for DB for AirBnB replica
    """

    @classmethod
    def connect(self):
        """Connect to the DB"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_DB"))

            self.cursor = self.db.cursor()
            self.storage = DBStorage()
            self.storage.reload()

    @classmethod
    def closeAll(self):
        """Close db"""
        self.cursor.close()
        self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'Wrong DB')
    def pep8_test(self):
        """Check pep8 Style"""
        check = pep8.StyleGuide(quiet=True)
        storage_py = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'Wrong DB')
    def attr_place_DBStorage(self):
        self.assertTrue(hasattr(DBStorage, 'name'))

if __name__ == "__main__":
    unittest.main()
