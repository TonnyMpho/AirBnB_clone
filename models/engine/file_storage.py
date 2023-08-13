#!/usr/bin/python3
""" serialization and deserialization of data """
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Private class attributes:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_data, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj = json.load(f)

                for key, val in obj.items():
                    cls_name, obj_id = key.split('.')
                    cls_name = eval(cls_name)
                    cls_instance = cls_name(**val)

                    self.__objects[key] = cls_instance
