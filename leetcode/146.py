# https://leetcode.com/problems/lru-cache/
# 146. LRU Cache

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.d.get(key) is None:
            return -1
        else:
            res = self.d[key]
            del self.d[key]
            self.d[key] = res
            return res

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        elif len(self.d) == self.capacity:
            self.d.popitem(last = False)
        self.d[key] = value