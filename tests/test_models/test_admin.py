#!/usr/bin/python3

"""
Contains the TestAdminDocs and TestAdmin classes
"""

from datetime import datetime
import inspect
import models
from models import admin
from models.base_model import BaseModel
import pep8
import unittest
Admin = admin.Admin

class TestAdminDocs(unittest.TestCase):
    """Tests to check the documentation and style of Admin class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.admin_f = inspect.getmembers(Admin, inspect.isfunction)

    def test_pep8_conformance_admin(self):
        """Test that models/admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_admin(self):
        """Test that tests/test_models/test_admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_admin_module_docstring(self):
        """Test for the admin.py module docstring"""
        self.assertIsNot(admin.__doc__, None,
                         "admin.py needs a docstring")
        self.assertTrue(len(admin.__doc__) >= 1,
                        "admin.py needs a docstring")

    def test_admin_class_docstring(self):
        """Test for the Admin class docstring"""
        self.assertIsNot(Admin.__doc__, None,
                         "Admin class needs a docstring")
        self.assertTrue(len(Admin.__doc__) >= 1,
                        "Admin class needs a docstring")

    def test_admin_func_docstrings(self):
        """Test for the presence of docstrings in Admin methods"""
        for func in self.admin_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAdmin(unittest.TestCase):
    """Test the Admin class"""
    def test_is_subclass(self):
        """Test that Admin is a subclass of BaseModel"""
        admin_instance = Admin()
        self.assertIsInstance(admin_instance, BaseModel)
        self.assertTrue(hasattr(admin_instance, "id"))
        self.assertTrue(hasattr(admin_instance, "created_at"))
        self.assertTrue(hasattr(admin_instance, "updated_at"))

    def test_attributes(self):
        """Test that Admin has the required attributes"""
        admin_instance = Admin()
        self.assertTrue(hasattr(admin_instance, "username"))
        self.assertTrue(hasattr(admin_instance, "email"))
        self.assertTrue(hasattr(admin_instance, "password"))

    def test_is_subclass(self):
        """Test that Admin is a subclass of BaseModel"""
        admin_instance = Admin()
        self.assertIsInstance(admin_instance, BaseModel)
        self.assertTrue(hasattr(admin_instance, "id"))
        self.assertTrue(hasattr(admin_instance, "created_at"))
        self.assertTrue(hasattr(admin_instance, "updated_at"))

    def test_attributes(self):
        """Test that Admin has the required attributes"""
        admin_instance = Admin()
        self.assertTrue(hasattr(admin_instance, "username"))
        self.assertTrue(hasattr(admin_instance, "email"))
        self.assertTrue(hasattr(admin_instance, "password"))

    def test_to_dict(self):
        """Test the to_dict method"""
        admin_instance = Admin()
        admin_dict = admin_instance.to_dict()
        self.assertEqual(admin_dict['__class__'], 'Admin')
        self.assertIsInstance(admin_dict['created_at'], str)
        self.assertIsInstance(admin_dict['updated_at'], str)
        self.assertEqual(admin_dict['username'], admin_instance.username)
        self.assertEqual(admin_dict['email'], admin_instance.email)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        admin_instance = Admin()
        string = f"[Admin] ({admin_instance.id}) {admin_instance.__dict__}"
        self.assertEqual(string, str(admin_instance))