# Importing multiple classes from a module

from car import Car , ElectricCar

my_audi = Car('audi','Q7', 2020)
print(my_audi.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'cybertruck', 2024)
print(my_tesla.get_descriptive_name())

# Importing an entire module

import car

my_audi = car.Car('audi', 'Q7', 2020)
print(my_audi.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'cybertruck', 2024)
print(my_tesla.get_descriptive_name())