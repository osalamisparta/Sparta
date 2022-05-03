class Vehicle:
    def __init__(self):
        self._speed = 0
        self.has_wheels = True

    def get_speed(self):
        return self._speed

    def set_speed(self, set_value: float):
        self._speed = set_value
