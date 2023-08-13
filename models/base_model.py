#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
BaseModel that defines all common
attributes/methods for other classes
"""


class BaseModel():
    """
    BaseModel that defines all common
    ttributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Class constructor """
        self.id = str(uuid.uuid4())

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
                if key == "created_at":
                    self.created_at = datetime.strptime(val, time_format)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(val, time_format)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
