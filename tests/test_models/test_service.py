#!/usr/bin/python3
"""
Contains the TestServiceDocs and TestService classes
"""

import inspect
from models.service import Service
import unittest
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import StringField, FloatField

class TestServiceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Service class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.service_f = inspect.getmembers(Service, inspect.isfunction)

    def test_service_module_docstring(self):
        """Test for the service.py module docstring"""
        self.assertIsNot(Service.__doc__, None,
                         "service.py needs a docstring")
        self.assertTrue(len(Service.__doc__) >= 1,
                        "service.py needs a docstring")

    def test_service_class_docstring(self):
        """Test for the Service class docstring"""
        self.assertIsNot(Service.__doc__, None,
                         "Service class needs a docstring")
        self.assertTrue(len(Service.__doc__) >= 1,
                        "Service class needs a docstring")

    def test_service_func_docstrings(self):
        """Test for the presence of docstrings in Service methods"""
        for func in self.service_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestService(unittest.TestCase):
    """Test the Service class"""
    def test_attributes(self):
        """Test that Service has the required attributes"""
        service_instance = Service()
        self.assertTrue(hasattr(service_instance, "name"))
        self.assertTrue(hasattr(service_instance, "description"))
        self.assertTrue(hasattr(service_instance, "cost"))

    def test_to_dict(self):
        """Test the to_dict method"""
        service_instance = Service()
        service_dict = service_instance.to_dict()
        self.assertEqual(service_dict['__class__'], 'Service')
        self.assertIsInstance(service_dict['created_at'], str)
        self.assertIsInstance(service_dict['updated_at'], str)
        self.assertEqual(service_dict['name'], service_instance.name)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        service_instance = Service()
        string = f"[Service] ({service_instance.id}) {service_instance.__dict__}"
        self.assertEqual(string, str(service_instance))
