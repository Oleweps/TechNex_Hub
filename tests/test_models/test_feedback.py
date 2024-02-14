#!/usr/bin/python3
"""
Contains the TestFeedbackForm and TestFeedbackDocs and TestFeedback classes
"""

import inspect
from models.feedback import Feedback, FeedbackForm
import unittest
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length
from wtforms import FloatField, TextAreaField, SubmitField
from sqlalchemy.orm import relationship

class TestFeedbackForm(unittest.TestCase):
    """Tests for the FeedbackForm class"""
    def test_form_fields(self):
        """Test that form fields are defined correctly"""
        form = FeedbackForm()
        self.assertIsInstance(form.rating, FloatField)
        self.assertIsInstance(form.comments, TextAreaField)
        self.assertIsInstance(form.submit, SubmitField)

    def test_form_validators(self):
        """Test form validators"""
        form = FeedbackForm()
        self.assertTrue(isinstance(form.rating.validators[0], DataRequired))
        self.assertTrue(isinstance(form.comments.validators[0], DataRequired))
        self.assertTrue(isinstance(form.comments.validators[1], Length))
        # Add more assertions for other form fields as needed

    # Add more tests for form validation, e.g., invalid data, valid data, etc.


class TestFeedbackDocs(unittest.TestCase):
    """Tests to check the documentation and style of Feedback class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.feedback_f = inspect.getmembers(Feedback, inspect.isfunction)

    def test_feedback_module_docstring(self):
        """Test for the feedback.py module docstring"""
        self.assertIsNot(Feedback.__doc__, None,
                         "feedback.py needs a docstring")
        self.assertTrue(len(Feedback.__doc__) >= 1,
                        "feedback.py needs a docstring")

    def test_feedback_class_docstring(self):
        """Test for the Feedback class docstring"""
        self.assertIsNot(Feedback.__doc__, None,
                         "Feedback class needs a docstring")
        self.assertTrue(len(Feedback.__doc__) >= 1,
                        "Feedback class needs a docstring")

    def test_feedback_func_docstrings(self):
        """Test for the presence of docstrings in Feedback methods"""
        for func in self.feedback_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFeedback(unittest.TestCase):
    """Test the Feedback class"""
    def test_attributes(self):
        """Test that Feedback has the required attributes"""
        feedback_instance = Feedback()
        self.assertTrue(hasattr(feedback_instance, "user_id"))
        self.assertTrue(hasattr(feedback_instance, "technician_id"))
        self.assertTrue(hasattr(feedback_instance, "rating"))
        self.assertTrue(hasattr(feedback_instance, "comments"))
        self.assertTrue(hasattr(feedback_instance, "timestamp"))

    def test_relationships(self):
        """Test relationships with User"""
        feedback_instance = Feedback()
        self.assertIsInstance(feedback_instance.user, relationship)
        self.assertIsInstance(feedback_instance.technician, relationship)

    def test_to_dict(self):
        """Test the to_dict method"""
        feedback_instance = Feedback()
        feedback_dict = feedback_instance.to_dict()
        self.assertEqual(feedback_dict['__class__'], 'Feedback')
        self.assertIsInstance(feedback_dict['created_at'], str)
        self.assertIsInstance(feedback_dict['updated_at'], str)
        self.assertEqual(feedback_dict['user_id'], feedback_instance.user_id)
        self.assertEqual(feedback_dict['technician_id'], feedback_instance.technician_id)
        # Add more assertions for other attributes as needed

    def test_str(self):
        """Test the __str__ method"""
        feedback_instance = Feedback()
        string = f"[Feedback] ({feedback_instance.id}) {feedback_instance.__dict__}"
        self.assertEqual(string, str(feedback_instance))
