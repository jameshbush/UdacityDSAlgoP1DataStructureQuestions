class LRU_Cache_Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.hash = dict()
        self.size = 0
        self.max_size = max_size

    def get(self, key):
        try: node = self.__remove_key(key)
        except KeyError: return -1

        self.__enq(node.key, node.value)
        return node.value

    def set(self, key, value):
        self.__enq(key, value)

    def __enq(self, key, value):
        node = LRU_Cache_Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self.__is_full():
                self.__deq()
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.hash[key] = node
        self.size += 1

    def __deq(self):
        node = self.tail
        if self.tail is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
        del self.hash[node.key]
        self.size -= 1
        return node

    def __remove_key(self, key):
        node = self.hash[key]
        if node is self.tail:
            return self.__deq()

        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        del self.hash[key]
        self.size -= 1
        return node

    def __is_full(self):
        return self.size >= self.max_size

our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
assert(our_cache.get(1) is 1)
assert(our_cache.get(2) is 2)
assert(our_cache.get(9) is -1)
our_cache.set(5, 5) 
our_cache.set(6, 6)
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
assert(our_cache.get(3) is -1)

for k, v in our_cache.hash.items():
    print(k, ':', v.value)
