import Vehicle

class Train(Vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self._top_speed = 268
        self.description = "Trains follow tracks and are mainly electric."
        self.has_wheels = False

    def accel(self, accel: str = ''):
        accel = accel.lower

        accelfac = float(4.5)

        if self._speed < self.top_speed and self._speed >= 0:
            self._speed = (self._speed + 1) * accelfac
        if self._speed >= self.top_speed:
            self._speed = self.top_speed
        print("Current speed: ", self._speed)

    def decel(self, decel: str = ''):
        decel = decel.lower
        decelfac = float(1 /4.5)

        if self._speed <= self.top_speed and self._speed > 0:
            self._speed = (self._speed - 1) * decelfac
        if self._speed <= 0:
            self._speed = 0
        print("Current speed: ", self._speed)

    def horn(self):
        print("HOONK HOOONK!")

