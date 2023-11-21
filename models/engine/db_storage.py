#!/usr/bin/python3
"""SQL database"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage():
    """A sql database storage engine"""

    __engine = None
    __session = None

    def __innit__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        env = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{db}", pool_pre_ping=True)


        if env == "test":
            Base.metadata.drop_all(self.__engine)