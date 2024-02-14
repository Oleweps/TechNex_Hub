#!/usr/bin/python3
"""
Contains the class TestTekHubConsoleDocs
"""

import console
import models
import pep8
import unittest

TekHubConsole = console.TekHubConsole


class TestTekHubConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_TekHubConsole_class_docstring(self):
        """Test for the TekHubConsole class docstring"""
        self.assertIsNot(TekHubConsole.__doc__, None,
                         "TekHubConsole class needs a docstring")
        self.assertTrue(len(TekHubConsole.__doc__) >= 1,
                        "TekHubConsole class needs a docstring")


if __name__ == '__main__':
    unittest.main()
