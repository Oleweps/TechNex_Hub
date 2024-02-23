#!/usr/bin/python3
"""This module creates the Suggestion class"""

import models
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SuggestionForm(FlaskForm):
    title = StringField('Suggestion Title', validators=[DataRequired(), Length(max=100)])
    category = SelectField('Suggestion Category', choices=[('feature', 'Feature Request'), ('bug', 'Bug Report')],
                           validators=[DataRequired()])
    content = TextAreaField('Suggestion Content', validators=[DataRequired(), Length(max=255)])
    user_id = StringField('User ID', validators=[DataRequired(), Length(max=60)])
    timestamp = DateTimeField('Timestamp', validators=[DataRequired()])
    status = StringField('Status', default='pending', validators=[Length(max=20)])
    submit = SubmitField('Submit Suggestion')

class Suggestion(BaseModel, Base):
    """A class named Suggestion
    Attributes:
    - user_id (str): The ID of the user submitting the suggestion
    - content (str): The content of the suggestion
    - timestamp (DateTime): The timestamp of when the suggestion is submitted
    - title (str): The title of the suggestion
    - category (str): The category of the suggestion (feature request, bug report)
    - status (str): The status of the suggestion (default is 'pending')
    - user (relationship): Many-to-one relationship with User
    """

    if models.storage_t == 'db':
        __tablename__ = 'suggestions'

        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        content = Column(String(255), nullable=False)
        timestamp = Column(DateTime, nullable=False)
        title = Column(String(100), nullable=False)
        category = Column(String(50), nullable=False)
        status = Column(String(20), default='pending', nullable=False)

        user = relationship('User', backref='suggestions')

    else:
        user_id = ""
        content = ""
        timestamp = None
        title = ""
        category = ""
        status = ""

    def __init__(self, *args, **kwargs):
        """initializes Suggestion"""
        super().__init__(*args, **kwargs)
