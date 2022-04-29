# Classes bring data and functionality together

class Dog:
    # class variable
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.animal_kind = "canine"

    @property
    def bark(self):  # method
        print(self.animal_kind)
        return print("woof!")


class Vehicle:
    # class variables
    def __init__(self, brand:str, model:str, colour:str, top_speed:int):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.top_speed = top_speed

    @property
    def racing(self):  # method
        if self.top_speed > 165:
            return "Race Car"
        else:
            return 'Family Car'

brand = input('Please enter your car brand: ')
model = input('Please enter your car model: ')
colour = input('Please enter your car colour: ')
top_speed = int(input('Please enter your cars top speed: '))

car = Vehicle(brand, model, colour, top_speed)
print(f'Your car is a {car.colour}, {car.brand} {car.model} and reaches {car.top_speed} mph.'
      f' It is a {car.racing}.')
