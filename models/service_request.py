#!/usr/bin/python3
"""This module creates the ServiceRequest class"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from models.base_model import BaseModel, Base
from models import storage
from os import getenv
from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

class ServiceRequestForm(FlaskForm):
    service_type = SelectField('Service Type', choices=[('repair', 'Repair'), ('maintenance', 'Maintenance')],
                               validators=[DataRequired()])
    equipment_details = TextAreaField('Equipment Details', validators=[DataRequired(), Length(max=255)])
    user_comments = TextAreaField('User Comments', validators=[Length(max=255)])
    submit = SubmitField('Submit Service Request')

class ServiceRequest(BaseModel, Base):
    
    if storage.storage_t == 'db':
        __tablename__ = 'service_requests'
        
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        service_type = Column(String(50), nullable=False)
        equipment_details = Column(String(255), nullable=False)
        user_comments = Column(String(255), nullable=True)
        status = Column(Enum('pending', 'completed', name='service_request_status'), default='pending', nullable=False)

        user = relationship('User', backref='service_requests')

    else:
        user_id = ""
        service_type = ""
        equipment_details = ""
        user_comments = ""
        status = ""

    def __init__(self, *args, **kwargs):
        """initializes ServiceRequest"""
        super().__init__(*args, **kwargs)
