#!/usr/bin/python3
"""
Contains the TestNotificationDocs and TestNotification classes
"""

import inspect
from models.notification import Notification
import unittest
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import StringField
from datetime import datetime
from sqlalchemy.orm import relationship

class TestNotificationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Notification class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.notification_f = inspect.getmembers(Notification, inspect.isfunction)

    def test_notification_module_docstring(self):
        """Test for the notification.py module docstring"""
        self.assertIsNot(Notification.__doc__, None,
                         "notification.py needs a docstring")
        self.assertTrue(len(Notification.__doc__) >= 1,
                        "notification.py needs a docstring")

    def test_notification_class_docstring(self):
        """Test for the Notification class docstring"""
        self.assertIsNot(Notification.__doc__, None,
                         "Notification class needs a docstring")
        self.assertTrue(len(Notification.__doc__) >= 1,
                        "Notification class needs a docstring")

    def test_notification_func_docstrings(self):
        """Test for the presence of docstrings in Notification methods"""
        for func in self.notification_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestNotification(unittest.TestCase):
    """Test the Notification class"""
    def test_attributes(self):
        """Test that Notification has the required attributes"""
        notification_instance = Notification()
        self.assertTrue(hasattr(notification_instance, "user_id"))
        self.assertTrue(hasattr(notification_instance, "content"))
        self.assertTrue(hasattr(notification_instance, "timestamp"))

    def test_relationships(self):
        """Test relationships with User"""
        notification_instance = Notification()
        self.assertIsInstance(notification_instance.user, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        notification_instance = Notification()
        notification_dict = notification_instance.to_dict()
        self.assertEqual(notification_dict['__class__'], 'Notification')
        self.assertIsInstance(notification_dict['created_at'], str)
        self.assertIsInstance(notification_dict['updated_at'], str)
        self.assertEqual(notification_dict['user_id'], notification_instance.user_id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        notification_instance = Notification()
        string = f"[Notification] ({notification_instance.id}) {notification_instance.__dict__}"
        self.assertEqual(string, str(notification_instance))
