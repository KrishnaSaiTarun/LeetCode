import threading 

class Foo:
    def __init__(self):
        self.secondLock = threading.Lock()
        self.thirdLock = threading.Lock()
        self.secondLock.acquire()
        self.thirdLock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.secondLock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.secondLock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.thirdLock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.thirdLock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        return 
