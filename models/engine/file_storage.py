#!/usr/bin/python3
"""
Contains FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    """#string - path to JSON file"""
    __file_path = "file.json"
    """ dictionary - empty but stores all objects by <class name>.id"""
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                class_name = jo[key]["__class__"]
                obj_dict = jo[key]
                self.__objects[key] = self.classes[class_name](**obj_dict)
        except FileNotFoundError:
            pass
