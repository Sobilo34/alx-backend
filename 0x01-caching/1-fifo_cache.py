#!/usr/bin/env python3
"""
A class FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class for FIFO caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """
        A function that is used to assing key to item
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: "+ oldest_key)

    def get(self, key):
        """
        A method that gets the value of a particular key value
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
