#!/usr/bin/python3
"""This module creates the Service class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float

class Service(BaseModel, Base):
    """A class named Service
    Attributes:
    - name (str): The name of the service
    - description (str): Description of the service
    - cost (float): The cost associated with the service
    """

    if models.storage_t == 'db':
        __tablename__ = 'services'

        name = Column(String(50), nullable=False, unique=True)
        description = Column(String(255), nullable=False)
        cost = Column(Float, nullable=False)

    else:
        name = ""
        description = ""
        cost = 0.0

    def __init__(self, *args, **kwargs):
        """initializes Service"""
        super().__init__(*args, **kwargs)
