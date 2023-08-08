#!/usr/bin/env python3
import uuid
from datetime import datetime
"""
BaseModel that defines all common
attributes/methods for other classes
"""

class BaseModel():
    """
    BaseModel that defines all common
    ttributes/methods for other classes
    """
    def __init__(self):
        """Class constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return string representation of the class """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__
