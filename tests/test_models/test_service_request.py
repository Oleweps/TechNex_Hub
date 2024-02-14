#!/usr/bin/python3
"""
Contains the TestServiceRequestFormDocs and TestServiceRequestForm,
TestServiceRequestDocs, and TestServiceRequest classes
"""

import inspect
from models.service_request import ServiceRequestForm, ServiceRequest
import unittest
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import SelectField, TextAreaField, SubmitField, StringField
from sqlalchemy.orm import relationship  # Import relationship

class TestServiceRequestFormDocs(unittest.TestCase):
    """Tests to check the documentation and style of ServiceRequestForm class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.form_f = inspect.getmembers(ServiceRequestForm, inspect.isfunction)

    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = ServiceRequestForm()
        self.assertIsInstance(form.service_type, SelectField)
        self.assertIsInstance(form.equipment_details, TextAreaField)
        self.assertIsInstance(form.user_comments, TextAreaField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = ServiceRequestForm()
        self.assertTrue(isinstance(form.service_type.validators[0], DataRequired))
        self.assertTrue(isinstance(form.equipment_details.validators[0], DataRequired))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestServiceRequestForm(unittest.TestCase):
    """Test the ServiceRequestForm class"""
    def test_attributes(self):
        """Test that ServiceRequestForm has the required attributes"""
        form_instance = ServiceRequestForm()
        self.assertTrue(hasattr(form_instance, "service_type"))
        self.assertTrue(hasattr(form_instance, "equipment_details"))
        self.assertTrue(hasattr(form_instance, "user_comments"))

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestServiceRequestDocs(unittest.TestCase):
    """Tests to check the documentation and style of ServiceRequest class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.service_request_f = inspect.getmembers(ServiceRequest, inspect.isfunction)

    def test_service_request_module_docstring(self):
        """Test for the service_request.py module docstring"""
        self.assertIsNot(ServiceRequest.__doc__, None,
                         "service_request.py needs a docstring")
        self.assertTrue(len(ServiceRequest.__doc__) >= 1,
                        "service_request.py needs a docstring")

    def test_service_request_class_docstring(self):
        """Test for the ServiceRequest class docstring"""
        self.assertIsNot(ServiceRequest.__doc__, None,
                         "ServiceRequest class needs a docstring")
        self.assertTrue(len(ServiceRequest.__doc__) >= 1,
                        "ServiceRequest class needs a docstring")

    def test_service_request_func_docstrings(self):
        """Test for the presence of docstrings in ServiceRequest methods"""
        for func in self.service_request_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestServiceRequest(unittest.TestCase):
    """Test the ServiceRequest class"""
    def test_attributes(self):
        """Test that ServiceRequest has the required attributes"""
        service_request_instance = ServiceRequest()
        self.assertTrue(hasattr(service_request_instance, "user_id"))
        self.assertTrue(hasattr(service_request_instance, "service_type"))
        self.assertTrue(hasattr(service_request_instance, "equipment_details"))
        self.assertTrue(hasattr(service_request_instance, "user_comments"))
        self.assertTrue(hasattr(service_request_instance, "status"))

    def test_relationships(self):
        """Test relationships with User"""
        service_request_instance = ServiceRequest()
        self.assertIsInstance(service_request_instance.user, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        service_request_instance = ServiceRequest()
        service_request_dict = service_request_instance.to_dict()
        self.assertEqual(service_request_dict['__class__'], 'ServiceRequest')
        self.assertIsInstance(service_request_dict['created_at'], str)
        self.assertIsInstance(service_request_dict['updated_at'], str)
        self.assertEqual(service_request_dict['user_id'], service_request_instance.user_id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        service_request_instance = ServiceRequest()
        string = f"[ServiceRequest] ({service_request_instance.id}) {service_request_instance.__dict__}"
        self.assertEqual(string, str(service_request_instance))
