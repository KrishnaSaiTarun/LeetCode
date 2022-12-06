import threading 

class TrafficLight:
    def __init__(self):
        self.greenroad = 1
        self.turnGreenLock = threading.Lock()

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:

        self.turnGreenLock.acquire()

        if roadId == self.greenroad:
            crossCar()
            self.turnGreenLock.release()
            return 
        
        turnGreen()
        self.greenroad = roadId
        crossCar()
        self.turnGreenLock.release()
