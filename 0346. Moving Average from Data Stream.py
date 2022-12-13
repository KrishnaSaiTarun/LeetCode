from collections import deque 

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.queue = deque()
        self.sum = 0
        
    def next(self, val: int) -> float:
        if self.isFull():
            pop_val = self.queue.popleft()
            self.queue.append(val)
            self.sum += val - pop_val
            return self.sum / self.count
    
        self.queue.append(val)
        self.sum+=val
        self.count += 1
        return self.sum/self.count 

    def isFull(self) -> bool:
        return True if self.count==self.size else False   


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
