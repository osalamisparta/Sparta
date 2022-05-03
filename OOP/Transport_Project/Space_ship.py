import Vehicle


class Spaceship(Vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.top_speed = 17500
        self.description = "Space shuttle are used for travel in space"
        self.has_wheels = False

    def accel(self, accel: str = ''):
        accel = accel.lower

        accelfac = float(50)

        if self._speed < self.top_speed and self._speed >= 0:
            self._speed = (self._speed + 1) * accelfac
        if self._speed >= self.top_speed:
            self._speed = self.top_speed
        print("Current speed: ", self._speed)

    def decel(self, decel: str = ''):

        decel = decel.lower
        decelfac = float(1/50)

        if self._speed <= self.top_speed and self._speed > 0:
            self._speed = (self._speed - 1) * decelfac
        if self._speed <= 0 :
            self._speed = 0
        print("Current speed: ", self._speed)

    def take_off(self):
        print ("Euston, we have lift off!")

