#!/usr/bin/env python3
"""
Problem:

Implement a simple in memory cache with the following interface.

public interface Cache {
    public string get(key);
    public void set(key, value);
    public void setMaxSize(size);
    public int getCurrentCacheSize();
}

"""
import random

class SimpleCache(object):

    keys = None
    values = None
    maxSize = 50

    def __init__(self):
        self.keys = []
        self.values = {}

    def get(self, key):
        """ get a key """
        return self.values[key]

    def set(self, key, value):
        """ set a key """

        # if the cache is full, drop the oldest entry
        if len(self.keys) >= self.maxSize:
            self.values.pop(self.keys.pop(0))

        if key not in self.keys:
            self.keys.append(key)

        self.values[key] = value

    def getMaxSize(self):
        """ return max size of cache in items """
        return self.maxSize

    def setMaxSize(self, size):
        """ set max size of cache in items """
        self.maxSize = size

        # if the new maxSize is less than the current size of the cache, purge all the oldest entries
        while len(self.keys) > self.maxSize:
            self.values.pop(self.keys.pop(0))

    def getCurrentCacheSize(self):
        """ get current amount of items in cache """
        return len(self.keys)

if __name__ == "__main__":

    cache = SimpleCache()

    # fill up the cache (default is 50)
    for x in range(200):
        cache.set("key_{}".format(x), 'lhslksdhflksdhfkldh!!!{}'.format(random.randint(0,500)))

    print("I have {} items in cache".format(cache.getCurrentCacheSize()))

    # old entries got bumped off
    try:
        value = cache.get("key_1")
    except KeyError:
        print("key_1 was expired")
        pass

    print("key_160 value is : {}".format(cache.get("key_160")))

    cache.setMaxSize(10)

    print("I have {} items in cache".format(cache.getCurrentCacheSize()))

    # old entries got bumped off
    try:
        value = cache.get("key_160")
    except KeyError:
        print("key_160 was expired")
        pass


