#!/usr/bin/python3
"""Unit tests for the HBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand console."""

    attribute_values = {
        str: "foobar108",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }

    test_random_attributes = {
        "strfoo": "barfoo",
        "intfoo": 248,
        "floatfoo": 9.8
    }

    def setUp(self):
        """Set up test environment."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    # Additional test_help_... methods for other commands

    def test_do_quit(self):
        """Test quit command."""
        # Test quit without arguments
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        # Test quit with additional arguments
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Additional test methods for other commands

    def create_class(self, classname):
        """Create an instance of the specified class."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        return uid

    # Additional helper methods

if __name__ == "__main__":
    unittest.main()
