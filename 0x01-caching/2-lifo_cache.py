#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - a caching system that follows the LIFO algorithm
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the last item put in cache (LIFO algorithm)
        and print DISCARD: <key>
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.stack.remove(key)
        self.stack.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)  # Discard the second-to-last key
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key
        If key is None or
        if the key doesn’t exist in self.cache_data, return None
        """
        return self.cache_data.get(key, None)
