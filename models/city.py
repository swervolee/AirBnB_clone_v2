#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states_id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)