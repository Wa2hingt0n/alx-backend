#!/usr/bin/env python3
""" Defines a class 'LFUCache' """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines an LFU cache replacement algorithm """
    def __init__(self):
        """ Initializes class instances """
        super().__init__()
        self.access_count = {}

    def put(self, key, item):
        """ Assigns item to key in the cache data structure """
        if key and item:
            count = 0
            if key in self.cache_data.keys():
                count = self.access_count.get(key)
                self.access_count.pop(key)
                self.cache_data.pop(key)
            count += 1
            self.access_count[key] = count
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                temp_dict = self.access_count.copy()
                temp_dict.pop(key)
                max_count = min(temp_dict.values())
                max_keys = []
                for k, v in self.access_count.items():
                    if v == max_count:
                        max_keys.append(k)
                if len(max_keys) > 1:
                    i = 0
                    for key_max in max_keys:
                        while i < len(self.access_count):
                            if key_max == list(self.access_count)[i]:
                                self.cache_data.pop(key_max)
                                self.access_count.pop(key_max)
                                print("DISCARD: {}".format(key_max))
                                break
                            i += 1
                        if key_max not in self.access_count.keys():
                            break
                elif len(max_keys) == 1:
                    key_del = max_keys[0]
                    self.cache_data.pop(key_del)
                    self.access_count.pop(key_del)
                    print("DISCARD: {}".format(key_del))

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        count = self.access_count.pop(key)
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        count += 1
        self.access_count[key] = count
        return item
