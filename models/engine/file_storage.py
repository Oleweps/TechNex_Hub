#!/usr/bin/python
"""
Contains the FileStorage class
"""
import models
import json
from models.admin import Admin
from models.authentication_token import AuthenticationToken
from models.base_model import BaseModel, Base
from models.equipment_listing import EquipmentListing
from models.feedback import Feedback
from models.message import Message
from models.notification import Notification
from models.service import Service
from models.service_request import ServiceRequest
from models.suggestion import Suggestion
from models.user import User

# Dictionary mapping class names to corresponding classes
classes = {
    "Admin": Admin,
    "AuthenticationToken": AuthenticationToken,
    "BaseModel": BaseModel,
    "EquipmentListing": EquipmentListing,
    "Feedback": Feedback,
    "Message": Message,
    "Notification": Notification,
    "Service": Service,
    "ServiceRequest": ServiceRequest,
    "Suggestion": Suggestion,
    "User": User
}

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    def __init__(self):
        # Path to the JSON file
        self.__file_path = "file.json"
        # Dictionary to store all objects by <class name>.id
        self.__objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)

        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                class_name = jo[key]["__class__"]
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or None if not found"""
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value

        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count
