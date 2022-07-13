#!/usr/bin/env python3
""" Defines a class MRUCache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines an MRU cache replacement algorithm """
    def __init__(self):
        """ Initializes class instances """
        super().__init__()

    def put(self, key, item):
        """ Assigns item to key in the cache data structure (dictionary) """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_del = list(self.cache_data)[-2]
                self.cache_data.pop(key_del)
                print("DISCARD: {}".format(key_del))

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
