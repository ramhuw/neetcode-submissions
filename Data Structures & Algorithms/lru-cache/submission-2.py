from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = deque(maxlen=capacity)
        self.n = 0

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                v = self.cache[i]
                self.cache.remove(v)
                self.cache.appendleft(v)
                return v[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                m0 = self.cache[i]
                m = (self.cache[i][0], value)
                self.cache.remove(m0)
                self.cache.appendleft(m)
                return
        self.cache.appendleft((key, value))
        self.n += 1

