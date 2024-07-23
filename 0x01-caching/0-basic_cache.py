#!/usr/bin/env python3
"""
A class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """A class for caching system"""
    def __init__(self):
        """Initialize the cache data"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
