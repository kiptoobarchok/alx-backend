#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - a caching system that follows the FIFO algorithm
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the first item put in cache (FIFO algorithm)
        and print DISCARD: <key>
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key
        If key is None or
        if the key doesn’t exist in self.cache_data, return None
        """
        return self.cache_data.get(key, None)
