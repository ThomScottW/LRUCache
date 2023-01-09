class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LRU:
    def __init__(self):
        self.head = None
        self.tail = None
        # Maps keys to pointers of their corresponding node.
        self.pointers = dict()
    
    def touch(self, key):
        """Move the key to the most recently used spot."""
        if key not in self.pointers:
            raise KeyError(f'The key {key} does not have a node, it may not be cached yet.')

        assert self.head is not None , "Attempted to touch uninitialized list."
        assert self.tail is not None, "Attempted to touch improperly intialized list."
        
        # Move it to the end.
        key_node = self.pointers[key]

        if key_node is self.tail or len(self.pointers) == 1:
            return  # This key is already the most recently used.
        
        if key_node is self.head:
            self.head = key_node.next
            self.head.prev = None
            
            key_node.next = None
            key_node.prev = self.tail
            self.tail.next = key_node
            self.tail = key_node
            return

        # General case.
        self.tail.next = key_node
        key_node.prev.next = key_node.next
        key_node.next.prev = key_node.prev
        key_node.prev = self.tail
        self.tail = key_node
        self.tail.next = None

    def add(self, key):
        assert key not in self.pointers, "Improper add, key {key} already in LRU"

        if self.tail:
            key_node = Node(key, self.tail, None)
            self.tail.next = key_node
            self.tail = key_node
        else:
            # The list is empty.
            key_node = Node(key, None, None)
            self.head = key_node
            self.tail = key_node

        self.pointers[key] = key_node
    
    def remove(self):
        """Remove head of linked list."""
        assert self.head is not None , f'Remove called on empty LRU.'
        del self.pointers[self.head.key]

        if self.head is self.tail:
            r = self.head
            self.head = None
            self.tail = None
            return r.key

        to_be_removed = self.head
        self.head = self.head.next
        self.head.prev = None
        return to_be_removed.key
    
    def __str__(self):
        string_representation = "["
        
        if cur.head is None:
            string_representation += "]"
            return string_representation

        cur = self.head

        while True:
            string_representation += f"<- | {cur.key} | ->"
            cur = cur.next
            if cur is None:
                string_representation += "]"
                return string_representation
    
    def __repr__(self):
        ans = "[]"

        if self.head is None:
            return ans
        
        ans = ""

        cur = self.head

        while True:
            ans += f'{cur.key}'
            cur = cur.next

            if cur is None:
                return ans

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.storage = dict()
        self.lru = LRU()
        
    def get(self, key: int) -> int:
        if key in self.storage:
            self.lru.touch(key)
            return self.storage[key]
        else:
            return -1     

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage[key] = value
            self.lru.touch(key)
            return
        
        if self.size == self.cap:
            # Remove least recently used item.
            lru_key = self.lru.remove()
            del self.storage[lru_key]
            self.size -=1
        
        self.storage[key] = value
        self.lru.add(key)
        self.size += 1



obj = LRUCache(10)
print(obj.put(10, 13), end=' ')
print(obj.put(3, 17), end=' ') 
print(obj.put(6, 11), end=' ') 
print(obj.put(10, 5), end=' ') 
print(obj.put(9, 10), end=' ') 
print(obj.get(13), end=' ')    
print(obj.put(2, 19), end=' ') 
print(obj.get(2), end=' ')     
print(obj.get(3), end=' ')     
print(obj.put(5, 25), end=' ')
print(obj.get(8), end=' ')
print(obj.put(9, 22), end=' ')
print(obj.put(5, 5), end=' ')
print(obj.put(1, 30), end=' ')
print(obj.get(11), end=' ')
print(obj.put(9, 12), end=' ')
print(obj.get(7), end=' ')
print(obj.get(5), end=' ')
print(obj.get(8), end=' ')
print(obj.get(9), end=' ')
print(obj.put(4, 30), end=' ')
print(obj.put(9, 3), end=' ')
print(obj.get(9), end=' ')
print(obj.get(10), end=' ')
print(obj.get(10), end=' ')
print(obj.put(6, 14), end=' ')
print(obj.put(3, 1), end=' ')
print(obj.get(3), end=' ')
print(obj.put(10, 11), end=' ')
print(obj.get(8), end=' ')
print(obj.put(2, 14), end=' ')
print(obj.get(1), end=' ')
print(obj.get(5), end=' ')
print(obj.get(4), end=' ')
print(obj.put(11, 4), end=' ')
print(obj.put(12, 24), end=' ')
print(obj.put(5, 18), end=' ')
print(obj.get(13), end=' ')
print(obj.put(7, 23), end=' ')
print(obj.get(8), end=' ')
print(obj.get(12), end=' ')
print(obj.put(3, 27), end=' ')
print(obj.put(2, 12), end=' ')
print(obj.get(5), end=' ')
print(obj.put(2, 9), end=' ')
print(obj.put(13, 4), end=' ')
print(obj.put(8, 18), end=' ')
print(obj.put(1, 7), end=' ')
print(obj.get(6), end=' ')
print(obj.put(9, 29), end=' ')
print(obj.put(8, 21), end=' ')
print(obj.get(5), end=' ')
print(obj.put(6, 30), end=' ')
print(obj.put(1, 12), end=' ')
print(obj.get(10), end=' ')
print(obj.put(4, 15), end=' ')
print(obj.put(7, 22), end=' ')
print(obj.put(11, 26), end=' ')
print(obj.put(8, 17), end=' ')
print(obj.put(9, 29), end=' ')
print(obj.get(5), end=' ')
print(obj.put(3, 4), end=' ')
print(obj.put(11, 30), end=' ')
print(obj.get(12), end=' ')
print(obj.put(4, 29), end=' ')
print(obj.get(3), end=' ')
print(obj.get(9), end=' ')
print(obj.get(6), end=' ')
print(obj.put(3, 4), end=' ')
print(obj.get(1), end=' ')
print(obj.get(10), end=' ')
print(obj.put(3, 29), end=' ')
print(obj.put(10, 28), end=' ')
print(obj.put(1, 20), end=' ')
print(obj.put(11, 13), end=' ')
print(obj.get(3), end=' ')
print(obj.put(3, 12), end=' ')
print(obj.put(3, 8), end=' ')
print(obj.put(10, 9), end=' ')
print(obj.put(3, 26), end=' ')
print(obj.get(8), end=' ')
print(obj.get(7), end=' ')
print(obj.get(5), end=' ')
print(obj.put(13, 17), end=' ')
print(obj.put(2, 27), end=' ')
print(obj.put(11, 15), end=' ')
print(obj.get(12), end=' ')
print(obj.put(9, 19), end=' ')
print(obj.put(2, 15), end=' ')
print(obj.put(3, 16), end=' ')
print(obj.get(1), end=' ')
print(obj.put(12, 17), end=' ')
print(obj.put(9, 1), end=' ')
print(obj.put(6, 19), end=' ')
print(obj.get(4), end=' ')
print(obj.get(5), end=' ')
print(obj.get(5), end=' ')
print(obj.put(8, 1), end=' ')
print(obj.put(11, 7), end=' ')
print(obj.put(5, 2), end=' ')
print(obj.put(9, 28), end=' ')
print(obj.get(1), end=' ')
print(obj.put(2, 2), end=' ')
print(obj.put(7, 4), end=' ')
print(obj.put(4, 22), end=' ')
print(obj.put(7, 24), end=' ')
print(obj.put(9, 26), end=' ')
print(obj.put(13, 28), end=' ')
print(obj.put(11, 26), end=' ')