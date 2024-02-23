#!/usr/bin/python3
"""
Contains class BaseModel
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
import models
from os import getenv

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel(Base):
    """A class named BaseModel
    Attributes:
    attr1(id): object id
    attr2(created_at): datetime instance is created
    attr3(updated_at): datetime instance is created and updated when changed
    """
    __abstract__ = True  # Set as abstract class

    id = Column(String(60), primary_key=True, nullable=False, unique=True, default=str(uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initiliazes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        if not self.id:
            self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        newdict = self.__dict__.copy()
        newdict['created_at'] = datetime.isoformat(newdict['created_at'])
        newdict['updated_at'] = datetime.isoformat(newdict['updated_at'])
        newdict['__class__'] = self.__class__.__name__
        newdict.pop('_sa_instance_state', None)
        return newdict

    def save(self):
        """updates public instance attr updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def delete(self):
        """deletes the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()
