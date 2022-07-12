#!/usr/bin/env python3
""" Module defines a class 'BasicCache' """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines a basic caching system without a size limit """
    def __init__(self):
        """ Initializes the class """
        super().__init__()

    def put(self, key, item):
        """ Adds data to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache, using its key """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
