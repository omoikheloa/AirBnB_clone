#!/usr/bin/python3
"""
Contains User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
