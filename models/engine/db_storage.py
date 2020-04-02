#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
import os
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class stores info into database

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method for DBStorage class."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """On the curret database session get all objects of the given class.
        If None, queries all types of objects.
        Return:
            Dict of queried classes <class name>.<obj id> = obj.
        """
        instances = {}
        if cls is None:
            all_cls = ["State", "City", "User", "Place", "Review", "Amenity"]
            for cl in all_cls:
                objs = self.__session.query(eval(cl))
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    instances[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                instances[key] = obj

        return instances

    def new(self, obj):
        """Adds object to the current db session
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes to the db
        """
        self.__session.commit()

    def reload(self):
        """ reload all the objs
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """delete obj from db session
        """
        if obj is not None:
            self.__session.delete(obj)
