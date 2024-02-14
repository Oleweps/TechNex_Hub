#!/usr/bin/python3
"""
Contains the TestEquipmentListingForm and TestEquipmentListingDocs and TestEquipmentListing classes
"""

import inspect
from models.equipment_listing import EquipmentListing, EquipmentListingForm
import unittest
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import StringField, FloatField, TextAreaField, SelectField, SubmitField
from sqlalchemy.orm import relationship  # Import relationship

class TestEquipmentListingForm(unittest.TestCase):
    """Tests for the EquipmentListingForm class"""
    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = EquipmentListingForm()
        self.assertIsInstance(form.equipment_name, StringField)
        self.assertIsInstance(form.description, TextAreaField)
        self.assertIsInstance(form.condition, SelectField)
        self.assertIsInstance(form.price, FloatField)
        self.assertIsInstance(form.contact_details, StringField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = EquipmentListingForm()
        self.assertTrue(isinstance(form.equipment_name.validators[0], DataRequired))
        self.assertTrue(isinstance(form.equipment_name.validators[1], Length))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestEquipmentListingDocs(unittest.TestCase):
    """Tests to check the documentation and style of EquipmentListing class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.equipment_listing_f = inspect.getmembers(EquipmentListing, inspect.isfunction)

    def test_equipment_listing_module_docstring(self):
        """Test for the equipment_listing.py module docstring"""
        self.assertIsNot(EquipmentListing.__doc__, None,
                         "equipment_listing.py needs a docstring")
        self.assertTrue(len(EquipmentListing.__doc__) >= 1,
                        "equipment_listing.py needs a docstring")

    def test_equipment_listing_class_docstring(self):
        """Test for the EquipmentListing class docstring"""
        self.assertIsNot(EquipmentListing.__doc__, None,
                         "EquipmentListing class needs a docstring")
        self.assertTrue(len(EquipmentListing.__doc__) >= 1,
                        "EquipmentListing class needs a docstring")

    def test_equipment_listing_func_docstrings(self):
        """Test for the presence of docstrings in EquipmentListing methods"""
        for func in self.equipment_listing_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestEquipmentListing(unittest.TestCase):
    """Test the EquipmentListing class"""
    def test_attributes(self):
        """Test that EquipmentListing has the required attributes"""
        equipment_listing_instance = EquipmentListing()
        self.assertTrue(hasattr(equipment_listing_instance, "user_id"))
        self.assertTrue(hasattr(equipment_listing_instance, "equipment_name"))
        self.assertTrue(hasattr(equipment_listing_instance, "description"))
        self.assertTrue(hasattr(equipment_listing_instance, "condition"))
        self.assertTrue(hasattr(equipment_listing_instance, "price"))
        self.assertTrue(hasattr(equipment_listing_instance, "contact_details"))

    def test_relationship_with_user(self):
        """Test the relationship with User"""
        equipment_listing_instance = EquipmentListing()
        self.assertIsInstance(equipment_listing_instance.user, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        equipment_listing_instance = EquipmentListing()
        equipment_listing_dict = equipment_listing_instance.to_dict()
        self.assertEqual(equipment_listing_dict['__class__'], 'EquipmentListing')
        self.assertIsInstance(equipment_listing_dict['created_at'], str)
        self.assertIsInstance(equipment_listing_dict['updated_at'], str)
        self.assertEqual(equipment_listing_dict['user_id'], equipment_listing_instance.user_id)
        self.assertEqual(equipment_listing_dict['equipment_name'], equipment_listing_instance.equipment_name)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        equipment_listing_instance = EquipmentListing()
        string = f"[EquipmentListing] ({equipment_listing_instance.id}) {equipment_listing_instance.__dict__}"
        self.assertEqual(string, str(equipment_listing_instance))
