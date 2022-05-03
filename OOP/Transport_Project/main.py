from Vehicle import Vehicle
from Car import Car
from Boat import Boat
from Space_ship import Spaceship
from Train import Train
from Skateboard import Skateboard



tony_hawks_car = Car()
print(tony_hawks_car.get_speed())
tony_hawks_car.accel()
tony_hawks_car.accel()
tony_hawks_car.accel()
print(tony_hawks_car.get_speed())

skateboard = Skateboard()
print(skateboard.description)
skateboard.ollie()
skateboard.christ_air()
skateboard.accel()
print(skateboard.get_speed())

shuttle = Spaceship()
print(shuttle.description)
shuttle.take_off()