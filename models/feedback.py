#!/usr/bin/python3
"""This module creates the feedback class"""

import models
from flask_wtf import FlaskForm
from wtforms import FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class FeedbackForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit Feedback')

class Feedback(BaseModel, Base):
    """A class named Feedback
    Attributes:
    - user_id (str): The ID of the user providing feedback
    - technician_id (str): The ID of the technician receiving feedback
    - rating (float): The rating provided by the user
    - comments (str): Comments or feedback text
    - timestamp (DateTime): The timestamp of when the feedback is submitted
    - user (relationship): Many-to-one relationship with User (feedback provider)
    - technician (relationship): Many-to-one relationship with User (feedback recipient)
    """

    if models.storage_t == 'db':
        __tablename__ = 'feedbacks'

        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        technician_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        rating = Column(Float, nullable=False)
        comments = Column(String(255), nullable=False)
        timestamp = Column(DateTime, nullable=False)

        user = relationship('User', foreign_keys=[user_id], backref='given_feedbacks')
        technician = relationship('User', foreign_keys=[technician_id], backref='received_feedbacks')

    else:
        user_id = ""
        technician_id = ""
        rating = 0.0
        comments = ""
        timestamp = None

    def __init__(self, *args, **kwargs):
        """initializes Feedback"""
        super().__init__(*args, **kwargs)
