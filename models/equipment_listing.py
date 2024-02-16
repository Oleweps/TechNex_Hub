#!/usr/bin/python3
"""This module creates the equipmentlisting class"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from models.base_model import BaseModel, Base
from models import storage
from os import getenv
from sqlalchemy import Column, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship

class EquipmentListingForm(FlaskForm):
    equipment_name = StringField('Equipment Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=255)])
    condition = SelectField('Condition', choices=[('new', 'New'), ('used', 'Used')], validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    contact_details = StringField('Contact Details', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('List Equipment')

class EquipmentListing(BaseModel, Base):
    """A class named EquipmentListing
    Attributes:
    - user_id (str): The ID of the user listing the equipment
    - equipment_name (str): The name of the equipment
    - description (str): Description of the equipment
    - condition (str): The condition of the equipment (e.g., new, used)
    - price (float): The price of the equipment
    - contact_details (str): Contact details of the seller
    - user (relationship): Many-to-one relationship with User
    """

    if storage.storage_t == 'db':
        __tablename__ = 'equipment_listings'

        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        equipment_name = Column(String(50), nullable=False)
        description = Column(String(255), nullable=False)
        condition = Column(Enum('new', 'used', name='equipment_condition'), nullable=False)
        price = Column(Float, nullable=False)
        contact_details = Column(String(255), nullable=False)

        user = relationship('User', backref='equipment_listings')

    else:
        user_id = ""
        equipment_name = ""
        description = ""
        condition = ""
        price = 0.0
        contact_details = ""

    def __init__(self, *args, **kwargs):
        """initializes EquipmentListing"""
        super().__init__(*args, **kwargs)
