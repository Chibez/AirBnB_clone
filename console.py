#!/usr/bin/python3
"""Module containing the command interpreter entry point."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches."""
        # Implementation details...

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()."""
        # Implementation details...

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        # Implementation details...

    def do_EOF(self, line):
        """Handles End Of File character."""
        # Implementation details...

    def do_quit(self, line):
        """Exits the program."""
        # Implementation details...

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        # Implementation details...

    def do_show(self, line):
        """Prints the string representation of an instance."""
        # Implementation details...

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        # Implementation details...

    def do_all(self, line):
        """Prints all string representation of all instances."""
        # Implementation details...

    def do_count(self, line):
        """Counts the instances of a class."""
        # Implementation details...

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        # Implementation details...

if __name__ == '__main__':
    HBNBCommand().cmdloop()
