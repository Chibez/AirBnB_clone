#!/usr/bin/python3
'''Defines the City class.'''

from models.base_model import BaseModel

class City(BaseModel):
    '''Class for managing city objects'''

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the City class'''
        super().__init__(*args, **kwargs)
