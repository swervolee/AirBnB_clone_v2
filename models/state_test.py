"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex

if __name__ == "__main__":
    var = models.storage.all()
    lista = []
    result = []
    for key in var:
        city = key.replace('.', ' ')
        city = shlex.split(city)
        if (city[0] == 'City'):
            lista.append(var[key])
    print(lista)