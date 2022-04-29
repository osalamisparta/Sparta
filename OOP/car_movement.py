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

        if accel == 'slow':
            accelfac = float(1.1)
        if accel == 'fast':
            accelfac = float(2.0)
        else:
            accelfac = float(1.5)

        if self._speed < self.top_speed and self._speed >= 0:
            self._speed = (self._speed + 1) * accelfac
        if self._speed >= self.top_speed:
            self._speed = self.top_speed

        print("Current speed: ", self._speed)

    def decel(self, decel: str = ''):

        decel = decel.lower

        if decel == 'slow':
            decelfac = float(1/1.1)
        if decel == 'fast':
            decelfac = float(1/2.0)
        else:
            decelfac = float(1/1.5)

        if self._speed <= self.top_speed and self._speed > 0:
            self._speed = (self._speed - 1) * decelfac
        if self._speed <= 0 :
            self._speed = 0
        print("Current speed: ", self._speed)





my_car = car('bugatti','blue', 170 )
while True:
    my_car.accel()
    if my_car.get_speed() == my_car.top_speed:
        break

