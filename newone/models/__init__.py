#!/usr/bin/python3
'''Initializes the package and sets up the file storage engine.'''

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
