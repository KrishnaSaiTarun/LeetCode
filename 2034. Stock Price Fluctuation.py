class StockPrice:

    def __init__(self):
        self.hashmap = collections.defaultdict(int)
        self.maxheap = []
        self.minheap = []
        self.max_timestamp = 0
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)

    def update(self, timestamp: int, price: int) -> None:

        self.hashmap[timestamp] = price 

        self.max_timestamp = max(timestamp, self.max_timestamp)
        heapq.heappush(self.minheap, (price, timestamp))
        heapq.heappush(self.maxheap, (-1*price, timestamp))

        
    def current(self) -> int:
        return self.hashmap[self.max_timestamp]
        

    def maximum(self) -> int:
        while self.maxheap and (-1* self.maxheap[0][0] != self.hashmap[self.maxheap[0][1]]):
            heapq.heappop(self.maxheap)
        
        if self.maxheap:
            return -1 * self.maxheap[0][0]
        return -1

    def minimum(self) -> int:
        while self.minheap and (self.minheap[0][0] != self.hashmap[self.minheap[0][1]]):
            heapq.heappop(self.minheap)
        
        if self.minheap:
            return self.minheap[0][0]
        return -1
     


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
