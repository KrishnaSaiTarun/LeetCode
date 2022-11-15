class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache_size = 0
        self.keyToNode = dict()

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode.keys():
            return -1
        
        value = self.keyToNode[key].value
        self.delete(key)
        self.addToTail(key, value)
        return value 


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyToNode.keys():
            self.delete(key)
            self.addToTail(key, value)
            return 
        
        if self.cache_size==self.capacity:
            self.delete(self.head.next.key)

        self.addToTail(key, value)

        

    def delete(self, key):
        node = self.keyToNode[key]
        del self.keyToNode[key]
        right = node.next
        left = node.prev 
        left.next = right
        right.prev = left 
        self.cache_size -= 1

    def addToTail(self, key, val):
        # head and tail do not have vals
        # they just are there to assist memeory 
        node = Node(key, val)
        actual_tail = self.tail.prev
        node.prev = actual_tail
        node.next = self.tail
        actual_tail.next = node
        self.tail.prev = node
        self.keyToNode[key] = node
        self.cache_size += 1        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
