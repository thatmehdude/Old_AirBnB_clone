#!/usr/bin/python3
"""Defines a BaseModel class"""
import uuid
from datetime  import datetime

class BaseModel:
    """the consoles base model"""
    def __init__(self, *args, **kwargs):
        creation_time = datetime.now()
        update_time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = creation_time
        self.updated_at = update_time


    def save(self):
        """updates with current time"""
        update_time = datetime.now()
        self.updated_at = update_time

    def to_dict(self):
        """
        to dict function:
        return: dictionary representation
               """
        new_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = datetime.isoformat(value)
            elif key == "updated_at":
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        return new_dict

    def __str__(self):
        """prints class name and id"""
        return f"[{type(self).__name_}] ({self.id}) {self.__dict__}"
    
