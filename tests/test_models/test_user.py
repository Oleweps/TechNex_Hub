#!/usr/bin/python3
"""
Contains the TestUserFormDocs, TestUserForm,
TestLogoutForm, TestRegisterForm, TestUserDocs, and TestUser classes
"""

import inspect
from models.user import UserForm, User
import unittest
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from sqlalchemy.orm import relationship  # Import relationship

# Define LogoutForm and RegisterForm classes
class LogoutForm:
    """Mock class for LogoutForm"""
    pass

class RegisterForm:
    """Mock class for RegisterForm"""
    pass

class TestUserFormDocs(unittest.TestCase):
    """Tests to check the documentation and style of UserForm class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.form_f = inspect.getmembers(UserForm, inspect.isfunction)

    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = UserForm()
        self.assertIsInstance(form.username, StringField)
        self.assertIsInstance(form.email, StringField)
        self.assertIsInstance(form.password, PasswordField)
        self.assertIsInstance(form.contact_details, TextAreaField)
        self.assertIsInstance(form.is_technician, BooleanField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = UserForm()
        self.assertTrue(isinstance(form.username.validators[0], DataRequired))
        self.assertTrue(isinstance(form.email.validators[0], DataRequired))
        self.assertTrue(isinstance(form.email.validators[1], Email))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestUserForm(unittest.TestCase):
    """Test the UserForm class"""
    def test_attributes(self):
        """Test that UserForm has the required attributes"""
        form_instance = UserForm()
        self.assertTrue(hasattr(form_instance, "username"))
        self.assertTrue(hasattr(form_instance, "email"))
        self.assertTrue(hasattr(form_instance, "password"))
        self.assertTrue(hasattr(form_instance, "contact_details"))
        self.assertTrue(hasattr(form_instance, "is_technician"))
        self.assertTrue(hasattr(form_instance, "submit"))

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestLogoutForm(unittest.TestCase):
    """Test the LogoutForm class"""
    def test_attributes(self):
        """Test that LogoutForm has the required attributes"""
        form_instance = LogoutForm()
        self.assertTrue(hasattr(form_instance, "user_id"))
        self.assertTrue(hasattr(form_instance, "token"))
        self.assertTrue(hasattr(form_instance, "submit"))

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestRegisterForm(unittest.TestCase):
    """Test the RegisterForm class"""
    def test_attributes(self):
        """Test that RegisterForm has the required attributes"""
        form_instance = RegisterForm()
        self.assertTrue(hasattr(form_instance, "username"))
        self.assertTrue(hasattr(form_instance, "email"))
        self.assertTrue(hasattr(form_instance, "password"))
        self.assertTrue(hasattr(form_instance, "confirm_password"))
        self.assertTrue(hasattr(form_instance, "contact_details"))
        self.assertTrue(hasattr(form_instance, "submit"))

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(User.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_attributes(self):
        """Test that User has the required attributes"""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "username"))
        self.assertTrue(hasattr(user_instance, "email"))
        self.assertTrue(hasattr(user_instance, "password"))
        self.assertTrue(hasattr(user_instance, "contact_details"))
        self.assertTrue(hasattr(user_instance, "is_technician"))

    def test_relationships(self):
        """Test relationships with ServiceRequest, Service, and EquipmentListing"""
        user_instance = User()
        self.assertIsInstance(user_instance.service_requests, relationship)
        self.assertIsInstance(user_instance.services, relationship)
        self.assertIsInstance(user_instance.equipment_listings, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        user_instance = User()
        user_dict = user_instance.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(user_dict['username'], user_instance.username)
        self.assertEqual(user_dict['email'], user_instance.email)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        user_instance = User()
        string = f"[User] ({user_instance.id}) {user_instance.__dict__}"
        self.assertEqual(string, str(user_instance))
