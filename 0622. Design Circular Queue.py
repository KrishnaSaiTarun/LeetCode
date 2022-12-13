class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = -1
        self.tail = -1
        self.queue = [None]* k
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        
        if self.isEmpty():
            self.head += 1

        if self.tail + 1 == self.capacity:
            self.tail = -1
        
        self.tail += 1
        self.count += 1
        self.queue[self.tail] = value
        return True 
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        
        self.queue[self.head] = None

        self.count -= 1
        if self.count == 0:
            self.head = self.tail = -1
            return True 

        if self.head + 1 == self.capacity:
            self.head = -1
        
        self.head += 1
        return True 
        

    def Front(self) -> int:
        if self.head == -1:
            return -1
        return self.queue[self.head]
        
        
    def Rear(self) -> int:
        if self.tail == -1:
            return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False 
        

    def isFull(self) -> bool:
        return True if self.count == self.capacity else False 
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
