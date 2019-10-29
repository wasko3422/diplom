"""Simple lru caches implementation."""


class LRU_Cache:

    def __init__(self, maxsize=128):
        # Link structure: [PREV, NEXT, KEY, VALUE]
        self.root = [None, None, None, None]
        self.root[0] = self.root[1] = self.root
        self.maxsize = maxsize
        self.mapping = {}

    def __call__(self, *key):
        root = self.root
        link = self.mapping.get(key)
        if link is None: return None
        link_prev, link_next, link_key, value = link
        link_prev[1] = link_next
        link_next[0] = link_prev
        last = root[0]
        last[1] = root[0] = link
        link[0] = last
        link[1] = root
        return value

    def add(self, value, *key):
        mapping = self.mapping
        root = self.root
        if len(mapping) >= self.maxsize:
            oldest = root[1]
            next_oldest = oldest[1]
            root[1] = next_oldest
            next_oldest[0] = root
            del mapping[oldest[2]]
        last = root[0]
        last[1] = root[0] = mapping[key] = [last, root, key, value]
        print(len(mapping))
        return value


if __name__ == '__main__':
    p = LRU_Cache(maxsize=128)
    for c in range(1000):
        p.add("test", c)
        print(c, p(c))