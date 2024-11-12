#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - a caching system that follows the LRU algorithm
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the least recently used item (LRU algorithm)
        and print DISCARD: <key>
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key
        If key is None or
        if the key doesn’t exist in self.cache_data, return None
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
