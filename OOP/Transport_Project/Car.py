import Vehicle

class Car(Vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.top_speed = 253.81
        self.description = "Cars accelerate on roads and follow road laws."
        self.has_wheels = True

    def accel(self, accel: str = ''):
        accel = accel.lower

        accelfac = float(1.5)

        if self._speed < self.top_speed and self._speed >= 0:
            self._speed = (self._speed + 1) * accelfac
        if self._speed >= self.top_speed:
            self._speed = self.top_speed
        print("Current speed: ", self._speed)

    def decel(self, decel: str = ''):

        decel = decel.lower
        decelfac = float(1/1.5)

        if self._speed <= self.top_speed and self._speed > 0:
            self._speed = (self._speed - 1) * decelfac
        if self._speed <= 0 :
            self._speed = 0
        print("Current speed: ", self._speed)

    def horn(self):
        print ("BEEP BEEP!")
