#!/usr/bin/python3
'''Defines the State class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Class for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
