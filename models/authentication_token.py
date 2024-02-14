#!/usr/bin/python3
"""This module creates the AuthenticationToken class"""
from models.base_model import BaseModel, Base
from models import storage
from os import getenv
import models
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class AuthenticationToken(BaseModel, Base):
    """A class named AuthenticationToken
    Attributes:
    - user_id (str): The ID of the user associated with the token
    - token (str): The authentication token string
    - expiration_time (DateTime): The timestamp indicating token expiration
    - user (relationship): Many-to-one relationship with User
    """

    if storage.storage_t == 'db':
        __tablename__ = 'authentication_tokens'

        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        token = Column(String(255), nullable=False, unique=True)
        expiration_time = Column(DateTime, nullable=False)

        user = relationship('User', backref='authentication_tokens')

    else:
        user_id = ""
        token = ""
        expiration_time = ""

    def __init__(self, *args, **kwargs):
        """initializes AuthenticationToken"""
        super().__init__(*args, **kwargs)
