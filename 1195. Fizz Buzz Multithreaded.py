import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False 
        self.fizzLock = threading.Lock()
        self.buzzLock = threading.Lock()
        self.fizzbuzzLock = threading.Lock()
        self.mainLock = threading.Lock()

        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzbuzzLock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizzLock.acquire()
            if self.done:
                return 
            printFizz()
            self.mainLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzzLock.acquire()
            if self.done:
                return 
            printBuzz()
            self.mainLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzzLock.acquire()
            if self.done:
                return 
            printFizzBuzz()
            self.mainLock.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n+1):
            self.mainLock.acquire()

            if i % 15 == 0:
                self.fizzbuzzLock.release()
            
            elif i % 3 == 0:
                self.fizzLock.release()
            
            elif i % 5 == 0:
                self.buzzLock.release()
            
            else:
                printNumber(i)
                self.mainLock.release()
        
        self.mainLock.acquire()
        self.done = True
        self.buzzLock.release()
        self.fizzLock.release()
        self.fizzbuzzLock.release()
