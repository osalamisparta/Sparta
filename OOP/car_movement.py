class car:

    def __init__(self, model:str, colour:str, top_speed):
        self._speed = 0
        self.model = model
        self.colour = colour
        self.top_speed = top_speed

    def get_speed(self):
        return self._speed

    def set_speed(self,x):
        self._speed = x

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


my_car = car('bugatti','blue', 170 )
my_car.get_speed()
