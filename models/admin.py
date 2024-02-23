#!/usr/bin/python
"""This module creates the Admin class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Admin(BaseModel, Base):
    """A class named Admin
    Attributes:
    - username (str): The username of the admin
    - email (str): The email of the admin
    - password (str): The hashed password of the admin
    """

    if models.storage_t == 'db':
        __tablename__ = 'admins'
        username = Column(String(60), nullable=False)
        email = Column(String(60), nullable=False)
        password = Column(String(60), nullable=False)
        

    else:
        username = ""
        email = ""
        password = ""

    def __init__(self, *args, **kwargs):
        """initializes Admin"""
        super().__init__(*args, **kwargs)
