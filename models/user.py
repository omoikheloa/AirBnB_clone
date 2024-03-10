#!/usr/bin/python3
"""
Contains User class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization of User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
