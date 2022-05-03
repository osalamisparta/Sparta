import Vehicle


class Skateboard(Vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.top_speed = 91.17
        self.description = "Skateboards are boards that rely on momentum pushed typically from a human."
        self.has_wheels = False

    def accel(self, accel: str = ''):
        accel = accel.lower

        accelfac = float(0.5)

        if self._speed < self.top_speed and self._speed >= 0:
            self._speed = (self._speed + 1) * accelfac
        if self._speed >= self.top_speed:
            self._speed = self.top_speed
        print("Current speed: ", self._speed)

    def decel(self, decel: str = ''):

        decel = decel.lower
        decelfac = float(1/0.5)

        if self._speed <= self.top_speed and self._speed > 0:
            self._speed = (self._speed - 1) * decelfac
        if self._speed <= 0 :
            self._speed = 0
        print("Current speed: ", self._speed)

    def ollie(self):
        print("Nice Ollie!")

    def christ_air(self):
        print("Nice Chist Air!")

    def kick_flip(self):
        print("Nice Kick Flip!")
