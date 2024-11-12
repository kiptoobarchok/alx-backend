#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - a caching system that stores items without any eviction policy
    """

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key if key is None or
        if the key doesn’t exist in self.cache_data, return None
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
