#!/usr/bin/python3
"""This module creates the Notification class"""

from models.base_model import BaseModel, Base
from models import storage
from os import getenv
import models
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Notification(BaseModel, Base):
    """A class named Notification
    Attributes:
    - user_id (str): The ID of the user receiving the notification
    - content (str): The content of the notification
    - timestamp (DateTime): The timestamp of when the notification is sent
    - user (relationship): Many-to-one relationship with User
    """

    if storage.storage_t == 'db':
        __tablename__ = 'notifications'

        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        content = Column(String(255), nullable=False)
        timestamp = Column(DateTime, nullable=False)

        user = relationship('User', backref='notifications')

    else:
        user_id = ""
        content = ""
        timestamp = None

    def __init__(self, *args, **kwargs):
        """initializes Notification"""
        super().__init__(*args, **kwargs)
