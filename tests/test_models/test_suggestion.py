#!/usr/bin/python3
"""
Contains the TestSuggestionFormDocs and TestSuggestionForm,
TestSuggestionDocs, and TestSuggestion classes
"""

import inspect
from models.suggestion import SuggestionForm, Suggestion
import unittest
from sqlalchemy.orm import relationship
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import SelectField, TextAreaField, SubmitField, StringField, DateTimeField

class TestSuggestionFormDocs(unittest.TestCase):
    """Tests to check the documentation and style of SuggestionForm class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.form_f = inspect.getmembers(SuggestionForm, inspect.isfunction)

    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = SuggestionForm()
        self.assertIsInstance(form.title, StringField)
        self.assertIsInstance(form.category, SelectField)
        self.assertIsInstance(form.content, TextAreaField)
        self.assertIsInstance(form.user_id, StringField)
        self.assertIsInstance(form.timestamp, DateTimeField)
        self.assertIsInstance(form.status, StringField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = SuggestionForm()
        self.assertTrue(isinstance(form.title.validators[0], DataRequired))
        self.assertTrue(isinstance(form.category.validators[0], DataRequired))
        self.assertTrue(isinstance(form.content.validators[0], DataRequired))
        self.assertTrue(isinstance(form.user_id.validators[0], DataRequired))
        self.assertTrue(isinstance(form.timestamp.validators[0], DataRequired))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestSuggestionForm(unittest.TestCase):
    """Test the SuggestionForm class"""
    def test_attributes(self):
        """Test that SuggestionForm has the required attributes"""
        form_instance = SuggestionForm()
        self.assertTrue(hasattr(form_instance, "title"))
        self.assertTrue(hasattr(form_instance, "category"))
        self.assertTrue(hasattr(form_instance, "content"))
        self.assertTrue(hasattr(form_instance, "user_id"))
        self.assertTrue(hasattr(form_instance, "timestamp"))
        self.assertTrue(hasattr(form_instance, "status"))

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestSuggestionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Suggestion class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.suggestion_f = inspect.getmembers(Suggestion, inspect.isfunction)

    def test_suggestion_module_docstring(self):
        """Test for the suggestion.py module docstring"""
        self.assertIsNot(Suggestion.__doc__, None,
                         "suggestion.py needs a docstring")
        self.assertTrue(len(Suggestion.__doc__) >= 1,
                        "suggestion.py needs a docstring")

    def test_suggestion_class_docstring(self):
        """Test for the Suggestion class docstring"""
        self.assertIsNot(Suggestion.__doc__, None,
                         "Suggestion class needs a docstring")
        self.assertTrue(len(Suggestion.__doc__) >= 1,
                        "Suggestion class needs a docstring")

    def test_suggestion_func_docstrings(self):
        """Test for the presence of docstrings in Suggestion methods"""
        for func in self.suggestion_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestSuggestion(unittest.TestCase):
    """Test the Suggestion class"""
    def test_attributes(self):
        """Test that Suggestion has the required attributes"""
        suggestion_instance = Suggestion()
        self.assertTrue(hasattr(suggestion_instance, "user_id"))
        self.assertTrue(hasattr(suggestion_instance, "content"))
        self.assertTrue(hasattr(suggestion_instance, "timestamp"))
        self.assertTrue(hasattr(suggestion_instance, "title"))
        self.assertTrue(hasattr(suggestion_instance, "category"))
        self.assertTrue(hasattr(suggestion_instance, "status"))

    def test_relationships(self):
        """Test relationships with User"""
        suggestion_instance = Suggestion()
        self.assertIsInstance(suggestion_instance.user, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        suggestion_instance = Suggestion()
        suggestion_dict = suggestion_instance.to_dict()
        self.assertEqual(suggestion_dict['__class__'], 'Suggestion')
        self.assertIsInstance(suggestion_dict['created_at'], str)
        self.assertIsInstance(suggestion_dict['updated_at'], str)
        self.assertEqual(suggestion_dict['user_id'], suggestion_instance.user_id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        suggestion_instance = Suggestion()
        string = f"[Suggestion] ({suggestion_instance.id}) {suggestion_instance.__dict__}"
        self.assertEqual(string, str(suggestion_instance))
