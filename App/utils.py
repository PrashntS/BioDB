#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

from pymongo import MongoClient
from config import config

class Database:
    """
    This class gets the database instance, and exposes the collections.
    """

    def __init__(self, uri = False):
        if type(uri) is str:
            self.client = MongoClient(uri)
        else:
            self.client = MongoClient(config['MONGODB_URL'])

        self.db = self.client[config['Database']]

    @property
    def user(self):
        """
        Returns the User Database collection
        """
        return self.db['user']

    @property
    def state(self):
        return self._state

    #@_state.setter
    def set_state(self, key, value):
        pass

    