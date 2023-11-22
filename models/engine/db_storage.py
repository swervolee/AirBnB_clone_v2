#!/usr/bin/python3
"""SQL database"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage():
    """A SQL database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        env = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{db}", pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of the query"""
        dictionary = {}
        if cls:
            if type(cls) == str:
                search = eval(cls)
            query = self.__session.query(cls)

            for item in query:
                k = f"{type(item).__name__}.{item.id}"
                dictionary[k] = item
        else:
            all = [State, City, User, Place, Review, Amenity]
            for i in all:
                query = self.__session.query(i)
                for item in query:
                    k = f"{type(item).__name__}.{item.id}"
                    dictionary[k] = item
        return dictionary

    def new(self, obj):
        """adds an object to the database"""
        self.__session.add(obj)

    def save(self):
        """saves the pending changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reads the database"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped_sess = scoped_session(sess)
        self.__session = scoped_sess()

    def close(self):
        """Closes the session"""
        self.__session.close()
