#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from os import getenv
from models.user import User
from models.service_request import ServiceRequest
from models.service import Service
from models.equipment_listing import EquipmentListing
from models.message import Message
from models.authentication_token import AuthenticationToken
from models.feedback import Feedback
from models.suggestion import Suggestion
from models.admin import Admin
from models.notification import Notification

# Create a dictionary with class names as keys and corresponding classes as values
classes = {
    "User": User,
    "ServiceRequest": ServiceRequest,
    "Service": Service,
    "EquipmentListing": EquipmentListing,
    "Message": Message,
    "AuthenticationToken": AuthenticationToken,
    "Feedback": Feedback,
    "Suggestion": Suggestion,
    "Admin": Admin,
    "Notification": Notification
}

class DBstorage:
    """This class manages the MySQL database for DLA Instrumentation Hub"""
    __engine = None
    __session = None

    def __init__(self):
        db_user = getenv('TEK_MYSQL_USER')
        db_pwd = getenv('TEK_MYSQL_PWD')
        db_host = getenv('TEK_MYSQL_HOST', default='localhost')
        db_name = getenv('TEK_MYSQL_DB')
        env = getenv('TEK_ENV')

        connection_str = f"mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}/{db_name}"

        self.__engine = create_engine(connection_str, pool_pre_ping=True)

        if env == "tektest":
            Base.metadata.drop_all(self.__engine)

        
    def all(self, cls=None):
        """Return a dictionary of objects"""
        obj_dict = {}
        if cls is None:
            for obj in self.__session.query(*classes.values()).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        else:
            for obj in self.__session.query(classes.get(cls)).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session to force reload"""
        self.__session.remove()

    def get(self, cls, id):
        """Get object based on class and id"""
        objs = self.__session.query(classes[cls]).all()
        for obj in objs:
            if obj.__class__.__name__ == cls and obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if cls is None:
            return self.__session.query(*classes.values()).count()
        else:
            return self.__session.query(classes.get(cls)).count()
