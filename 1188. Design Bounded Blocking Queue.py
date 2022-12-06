import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.producerLock = threading.Lock()
        self.consumerLock = threading.Lock()
        self.queue = []
        self.consumerLock.acquire()

    def enqueue(self, element: int) -> None:

        self.producerLock.acquire()
        self.queue.append(element)

        if len(self.queue) < self.capacity:
            self.producerLock.release()
        if self.consumerLock.locked():
            self.consumerLock.release()


    def dequeue(self) -> int:
        
        self.consumerLock.acquire()
        element = self.queue.pop(0)

        if len(self.queue):
            self.consumerLock.release()
        if self.producerLock.locked():
            self.producerLock.release()
        
        return element

    def size(self) -> int:
        return len(self.queue)
