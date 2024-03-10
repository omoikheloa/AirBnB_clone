#!/usr/bin/python3
"""
Contains BaseModel class
"""

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time)
                if key != '__class__':
                    setattr(self, key, value)
            kwargs.pop('__class__', None)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values in the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
