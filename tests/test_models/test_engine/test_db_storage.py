#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import inspect
from models import storage
from models.engine.db_storage import Storage
from models.user import User
from models.service_request import ServiceRequest
from models.service import Service
from models.equipment_listing import EquipmentListing
from models.message import Message
from models.auth_token import AuthenticationToken
from models.feedback import Feedback
from models.suggestion import Suggestion
from models.admin import Admin
from models.notification import Notification
from sqlalchemy.orm.exc import NoResultFound
import os
import pep8
import unittest

classes = {"User": User, "ServiceRequest": ServiceRequest, "Service": Service,
           "EquipmentListing": EquipmentListing, "Message": Message,
           "AuthenticationToken": AuthenticationToken, "Feedback": Feedback,
           "Suggestion": Suggestion, "Admin": Admin, "Notification": Notification}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of Storage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.storage_f = inspect.getmembers(Storage, inspect.isfunction)

    def test_pep8_conformance_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(Storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(Storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_storage_class_docstring(self):
        """Test for the Storage class docstring"""
        self.assertIsNot(Storage.__doc__, None,
                         "Storage class needs a docstring")
        self.assertTrue(len(Storage.__doc__) >= 1,
                        "Storage class needs a docstring")

    def test_storage_func_docstrings(self):
        """Test for the presence of docstrings in Storage methods"""
        for func in self.storage_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the Storage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the Storage tests"""
        storage._FileStorage__objects = {}
        cls.storage = Storage()

    def test_all(self):
        """Test the all method"""
        obj_dict = self.storage.all()
        self.assertEqual(type(obj_dict), dict)

    def test_new(self):
        """Test the new method"""
        user = User(username="test_user", email="test@example.com", password="test_password")
        user.save()
        storage.reload()
        self.assertTrue("User." + user.id in storage.all(User))

    def test_save(self):
        """Test the save method"""
        user = User(username="test_user2", email="test2@example.com", password="test_password2")
        user.save()
        storage.reload()
        self.assertTrue("User." + user.id in storage.all(User))

    def test_delete(self):
        """Test the delete method"""
        user = User(username="test_user3", email="test3@example.com", password="test_password3")
        user.save()
        user_id = user.id
        storage.reload()
        self.assertTrue("User." + user_id in storage.all(User))
        storage.delete(user)
        storage.reload()
        self.assertTrue("User." + user_id not in storage.all(User))

    def test_reload(self):
        """Test the reload method"""
        user = User(username="test_user4", email="test4@example.com", password="test_password4")
        user.save()
        storage.reload()
        new_storage = Storage()
        self.assertTrue("User." + user.id in new_storage.all(User))

    def test_get(self):
        """Test the get method"""
        user = User(username="test_user5", email="test5@example.com", password="test_password5")
        user.save()
        user_id = user.id
        storage.reload()
        get_user = storage.get(User, user_id)
        self.assertEqual(user, get_user)

    def test_count(self):
        """Test the count method"""
        count_before = storage.count()
        user = User(username="test_user6", email="test6@example.com", password="test_password6")
        user.save()
        count_after = storage.count()
        self.assertEqual(count_before + 1, count_after)
