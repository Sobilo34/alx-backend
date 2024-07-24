from base_caching import BaseCaching

#!/usr/bin/env python3
"""
A class LFUCache that inherits from
BaseCaching and is a caching system
"""


class LFUCache(BaseCaching):
    """
    A class for LFU caching system
    """
    def __init__(self):
        super().__init__()
        self.lfu = []
        self.lfu_count = {}

    def put(self, key, item):
        """
        A function that assigns key to item and handles LFU eviction
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.lfu_count[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_count = min(self.lfu_count.values())
                lfu_keys = [k for k, v in self.lfu_count.items() if v == min_count]
                lfu_key = min(self.lfu, key=lambda x: self.lfu.index(x) if x in self.lfu else float('inf'))
                self.lfu.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.lfu_count[lfu_key]
                print("DISCARD: " + lfu_key)

            self.cache_data[key] = item
            self.lfu_count[key] = 1
            self.lfu.append(key)

    def get(self, key):
        """
        A function that returns the value of key from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.lfu_count[key] += 1
        self.lfu.remove(key)
        self.lfu.append(key)

        return self.cache_data[key]
