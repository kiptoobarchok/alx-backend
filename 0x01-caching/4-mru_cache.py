#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - a caching system that follows the MRU algorithm
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.access_order = []  # List to track access order of keys

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the most recently used item (MRU algorithm)
        and print DISCARD: <key>
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove existing key from access order
            self.access_order.remove(key)

        # Add key to the end to mark as most recently used
        self.access_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop(-2)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Get an item by key
        If key is None or
        if the key doesn’t exist in self.cache_data, return None
        """
        if key is None or key not in self.cache_data:
            return None

        # Remove and append the accessed key to update its position as MRU
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
