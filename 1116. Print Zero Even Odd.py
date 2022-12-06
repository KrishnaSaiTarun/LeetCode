import threading 

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.evenLock = threading.Lock()
        self.oddLock = threading.Lock()
        self.zeroLock = threading.Lock()

        self.evenLock.acquire()
        self.oddLock.acquire()

        self.printNum = 1
        self.done = False 
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.printNum <= self.n:
            self.zeroLock.acquire()
            if self.printNum > self.n:
                self.zeroLock.release()
                break

            printNumber(0)

            if self.printNum % 2 != 0:
                self.oddLock.release()

            else:
                self.evenLock.release()


        self.zeroLock.acquire()
        self.done = True
        self.evenLock.release()
        self.oddLock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.evenLock.acquire()
            if self.done:
                return 
            printNumber(self.printNum)
            self.printNum += 1
            self.zeroLock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.oddLock.acquire()
            if self.done:
                return 
            printNumber(self.printNum)
            self.printNum += 1
            self.zeroLock.release()
        
        
