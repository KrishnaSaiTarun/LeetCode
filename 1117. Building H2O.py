import threading
class H2O:
    def __init__(self):
        self.oxylock = threading.Lock()
        self.hydrolock = threading.Lock()
        self.oxylock.acquire()
        self.released_hydrogens = 0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrolock.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.released_hydrogens+=1
        if self.released_hydrogens % 2 == 0:
            self.oxylock.release()
        else:
            self.hydrolock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxylock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.hydrolock.release()
