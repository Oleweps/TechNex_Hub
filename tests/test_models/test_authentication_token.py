#!/usr/bin/python3
"""
Contains the TestAuthTokenDocs and TestAuthToken classes
"""

from sqlalchemy.orm import relationship  # Import relationship
from datetime import datetime
import inspect
import models
from models import authentication_token
from models.base_model import BaseModel
import pep8
import unittest

AuthenticationToken = authentication_token.AuthenticationToken
User = models.user.User  # Assuming you have a User model

class TestAuthTokenDocs(unittest.TestCase):
    """Tests to check the documentation and style of AuthenticationToken class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.auth_token_f = inspect.getmembers(AuthenticationToken, inspect.isfunction)

    def test_pep8_conformance_auth_token(self):
        """Test that models/authentication_token.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/authentication_token.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_auth_token(self):
        """Test that tests/test_models/test_authentication_token.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_authentication_token.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_auth_token_module_docstring(self):
        """Test for the authentication_token.py module docstring"""
        self.assertIsNot(authentication_token.__doc__, None,
                         "authentication_token.py needs a docstring")
        self.assertTrue(len(authentication_token.__doc__) >= 1,
                        "authentication_token.py needs a docstring")

    def test_auth_token_class_docstring(self):
        """Test for the AuthenticationToken class docstring"""
        self.assertIsNot(AuthenticationToken.__doc__, None,
                         "AuthenticationToken class needs a docstring")
        self.assertTrue(len(AuthenticationToken.__doc__) >= 1,
                        "AuthenticationToken class needs a docstring")

    def test_auth_token_func_docstrings(self):
        """Test for the presence of docstrings in AuthenticationToken methods"""
        for func in self.auth_token_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAuthToken(unittest.TestCase):
    """Test the AuthenticationToken class"""
    def test_is_subclass(self):
        """Test that AuthenticationToken is a subclass of BaseModel"""
        auth_token_instance = AuthenticationToken()
        self.assertIsInstance(auth_token_instance, BaseModel)
        self.assertTrue(hasattr(auth_token_instance, "id"))
        self.assertTrue(hasattr(auth_token_instance, "created_at"))
        self.assertTrue(hasattr(auth_token_instance, "updated_at"))

    def test_attributes(self):
        """Test that AuthenticationToken has the required attributes"""
        auth_token_instance = AuthenticationToken()
        self.assertTrue(hasattr(auth_token_instance, "user_id"))
        self.assertTrue(hasattr(auth_token_instance, "token"))
        self.assertTrue(hasattr(auth_token_instance, "expiration_time"))

    def test_relationship_with_user(self):
        """Test the relationship with User"""
        auth_token_instance = AuthenticationToken()
        self.assertIsInstance(auth_token_instance.user, relationship)
        self.assertEqual(auth_token_instance.user.property.mapper.class_, User)

    def test_to_dict(self):
        """Test the to_dict method"""
        auth_token_instance = AuthenticationToken()
        auth_token_dict = auth_token_instance.to_dict()
        self.assertEqual(auth_token_dict['__class__'], 'AuthenticationToken')
        self.assertIsInstance(auth_token_dict['created_at'], str)
        self.assertIsInstance(auth_token_dict['updated_at'], str)
        self.assertEqual(auth_token_dict['user_id'], auth_token_instance.user_id)
        self.assertEqual(auth_token_dict['token'], auth_token_instance.token)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        auth_token_instance = AuthenticationToken()
        string = f"[AuthenticationToken] ({auth_token_instance.id}) {auth_token_instance.__dict__}"
        self.assertEqual(string, str(auth_token_instance))
