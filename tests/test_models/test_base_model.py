#!/usr/bin/python3
"""
Contains the TestBaseModelDocs and TestBaseModel classes
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest

class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_model_f = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance_base_model(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_model_module_docstring(self):
        """Test for the base_model.py module docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "base_model.py needs a docstring")

    def test_base_model_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_model_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_attributes(self):
        """Test that BaseModel has the required attributes"""
        base_model_instance = BaseModel()
        self.assertTrue(hasattr(base_model_instance, "id"))
        self.assertTrue(hasattr(base_model_instance, "created_at"))
        self.assertTrue(hasattr(base_model_instance, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method"""
        base_model_instance = BaseModel()
        base_model_dict = base_model_instance.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)
        self.assertEqual(base_model_dict['id'], base_model_instance.id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        base_model_instance = BaseModel()
        string = f"[BaseModel] ({base_model_instance.id}) {base_model_instance.__dict__}"
        self.assertEqual(string, str(base_model_instance))

    def test_save_updates_updated_at(self):
        """Test that the save method updates the updated_at attribute"""
        base_model_instance = BaseModel()
        initial_updated_at = base_model_instance.updated_at
        base_model_instance.save()
        self.assertNotEqual(initial_updated_at, base_model_instance.updated_at)
