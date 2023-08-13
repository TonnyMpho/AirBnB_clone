#!/usr/bin/python3
"""Definition of the Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represents an amenity.
    Attributes:
    name (str): the name of the amenity.
    """
    name = ""
