#!/usr/bin/python3
"""This module creates the Message class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_wtf import FlaskForm
from os import getenv
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    sender_id = StringField('Sender ID', validators=[DataRequired(), Length(max=60)])
    receiver_id = StringField('Receiver ID', validators=[DataRequired(), Length(max=60)])
    timestamp = DateTimeField('Timestamp', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Send Message')

class Message(BaseModel, Base):
    """A class named Message
    Attributes:
    - sender_id (str): The ID of the message sender (user or technician)
    - receiver_id (str): The ID of the message receiver (user or technician)
    - timestamp (DateTime): The timestamp of the message
    - content (str): The content of the message
    - sender (relationship): Many-to-one relationship with User
    - receiver (relationship): Many-to-one relationship with User
    """

    if models.storage_t == 'db':
        __tablename__ = 'messages'

        sender_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        receiver_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        timestamp = Column(DateTime, nullable=False)
        content = Column(String(255), nullable=False)

        sender = relationship('User', foreign_keys=[sender_id], backref='sent_messages')
        receiver = relationship('User', foreign_keys=[receiver_id], backref='received_messages')

    else:
        sender_id = ""
        receiver_id = ""
        timestamp = None
        content = ""

    def __init__(self, *args, **kwargs):
        """initializes Message"""
        super().__init__(*args, **kwargs)
