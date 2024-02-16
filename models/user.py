#!/usr/bin/python3
"""This module creates the User class"""

from models.base_model import BaseModel, Base
from models import storage
from os import getenv
from models.message import Message
from models.feedback import Feedback
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import hashlib  # Import hashlib for password hashing

class UserForm(FlaskForm):
    """Form class for User"""
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])
    contact_details = TextAreaField('Contact Details', validators=[Length(max=255)])
    is_technician = BooleanField('Is Technician')

class LogoutForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Logout')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    contact_details = StringField('Contact Details')
    submit = SubmitField('Register')

class User(BaseModel, Base):
    """A class named User
    Attributes:
    - username (str): The username of the user
    - email (str): The email address of the user
    - password (str): The hashed password of the user (MD5)
    - contact_details (str): The contact details of the user
    - is_technician (bool): Indicates whether the user is a technician
    - service_requests (relationship): One-to-many relationship with ServiceRequest
    - services (relationship): One-to-many relationship with Service
    - equipment_listings (relationship): One-to-many relationship with EquipmentListing
    - suggestions (relationship): One-to-many relationship with Suggestion
    - sent_messages (relationship): One-to-many relationship with Message (sender)
    - received_messages (relationship): One-to-many relationship with Message (receiver)
    - given_feedbacks (relationship): One-to-many relationship with Feedback (user)
    - received_feedbacks (relationship): One-to-many relationship with Feedback (technician)
    - authentication_tokens (relationship): One-to-many relationship with AuthenticationToken
    """

    if storage.storage_t == 'db':
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key column
        username = Column(String(50), nullable=False)
        email = Column(String(100), nullable=False, unique=True)
        password = Column(String(100), nullable=False)
        contact_details = Column(String(255), nullable=True)
        is_technician = Column(String(10), nullable=False, default=False)

        service_requests = relationship('ServiceRequest', backref='user', cascade='all, delete-orphan')
        services = relationship('Service', backref='user', cascade='all, delete-orphan')
        equipment_listings = relationship('EquipmentListing', backref='user', cascade='all, delete-orphan')
        suggestions = relationship('Suggestion', backref='user', cascade='all, delete-orphan')
        sent_messages = relationship('Message', foreign_keys=[Message.sender_id], backref='sender', cascade='all, delete-orphan')
        received_messages = relationship('Message', foreign_keys=[Message.receiver_id], backref='receiver', cascade='all, delete-orphan')
        given_feedbacks = relationship('Feedback', foreign_keys=[Feedback.user_id], backref='user', cascade='all, delete-orphan')
        received_feedbacks = relationship('Feedback', foreign_keys=[Feedback.technician_id], backref='technician', cascade='all, delete-orphan')
        authentication_tokens = relationship('AuthenticationToken', backref='user', cascade='all, delete-orphan')

    else:
        id = 0
        username = ""
        email = ""
        password = ""
        contact_details = ""
        is_technician = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of User"""
        super().__init__(*args, **kwargs)
        # Hash the password to MD5 whenever a new User object is created or password is updated
        if 'password' in kwargs:
            self.password = hashlib.md5(kwargs['password'].encode()).hexdigest()

    def update_password(self, new_password):
        """Updates the password to a new hashed value"""
        self.password = hashlib.md5(new_password.encode()).hexdigest()
