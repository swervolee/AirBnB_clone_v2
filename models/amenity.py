#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class Amenity(BaseModel):
    name = ""
