#!/usr/bin/env python3
""" Defines a class 'FIFOCache' """
from base_caching import BaseCaching


BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BaseCaching):
    """ Defines a FIFO cache replacement algorithm """
    def __init__(self):
        """ Initializes the class """
        super().__init__()

    def put(self, key, item):
        """ Adds data to the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_del = list(self.cache_data)[0]
                self.cache_data.pop(key_del)
                print("DISCARD: {}".format(key_del))

    def get(self, key):
        """ Returns the item on the cache linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
