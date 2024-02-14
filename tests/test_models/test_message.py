#!/usr/bin/python3
"""
Contains the TestMessageForm and TestMessageDocs and TestMessage classes
"""

import inspect
from models.message import Message, MessageForm
import unittest
from wtforms import ValidationError, DateTimeField
from wtforms.validators import DataRequired, Length
from wtforms import StringField, TextAreaField, SubmitField
from sqlalchemy.orm import relationship  # Import relationship

class TestMessageForm(unittest.TestCase):
    """Tests for the MessageForm class"""
    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = MessageForm()
        self.assertIsInstance(form.sender_id, StringField)
        self.assertIsInstance(form.receiver_id, StringField)
        self.assertIsInstance(form.timestamp, DateTimeField)
        self.assertIsInstance(form.content, TextAreaField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = MessageForm()
        self.assertTrue(isinstance(form.sender_id.validators[0], DataRequired))
        self.assertTrue(isinstance(form.sender_id.validators[1], Length))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestMessageDocs(unittest.TestCase):
    """Tests to check the documentation and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.message_f = inspect.getmembers(Message, inspect.isfunction)

    def test_message_module_docstring(self):
        """Test for the message.py module docstring"""
        self.assertIsNot(Message.__doc__, None,
                         "message.py needs a docstring")
        self.assertTrue(len(Message.__doc__) >= 1,
                        "message.py needs a docstring")

    def test_message_class_docstring(self):
        """Test for the Message class docstring"""
        self.assertIsNot(Message.__doc__, None,
                         "Message class needs a docstring")
        self.assertTrue(len(Message.__doc__) >= 1,
                        "Message class needs a docstring")

    def test_message_func_docstrings(self):
        """Test for the presence of docstrings in Message methods"""
        for func in self.message_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestMessage(unittest.TestCase):
    """Test the Message class"""
    def test_attributes(self):
        """Test that Message has the required attributes"""
        message_instance = Message()
        self.assertTrue(hasattr(message_instance, "sender_id"))
        self.assertTrue(hasattr(message_instance, "receiver_id"))
        self.assertTrue(hasattr(message_instance, "timestamp"))
        self.assertTrue(hasattr(message_instance, "content"))

    def test_relationships(self):
        """Test relationships with User"""
        message_instance = Message()
        self.assertIsInstance(message_instance.sender, relationship)
        self.assertIsInstance(message_instance.receiver, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        message_instance = Message()
        message_dict = message_instance.to_dict()
        self.assertEqual(message_dict['__class__'], 'Message')
        self.assertIsInstance(message_dict['created_at'], str)
        self.assertIsInstance(message_dict['updated_at'], str)
        self.assertEqual(message_dict['sender_id'], message_instance.sender_id)
        self.assertEqual(message_dict['receiver_id'], message_instance.receiver_id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        message_instance = Message()
        string = f"[Message] ({message_instance.id}) {message_instance.__dict__}"
        self.assertEqual(string, str(message_instance))
