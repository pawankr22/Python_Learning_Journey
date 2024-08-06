# Looping through all key value pairs
user_0 = {
    'username' : 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favourite_cars = {
    'rohan' : 'audi',
    'avinash': 'porche',
    'tushar': 'mercedes',
    'suraj': 'ferari',
    'rajesh': 'batmobile',
}

for name, car in favourite_cars.items():
    print(f"{name.title()}'s favourite car is {car.title()}.")

# Looping through all the keys in a dictionary

favourite_cars = {
    'rohan' : 'audi',
    'avinash': 'porche',
    'tushar': 'mercedes',
    'suraj': 'ferari',
    'rajesh': 'batmobile',
}

for name in favourite_cars.keys():
    print(name.title())

# printing a message to the couple of friends

friends = ['avinash', 'rohan']
for name in favourite_cars.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        car = favourite_cars[name].title()
        print(f"\t{name.title()}, I see you love {car}!")

# We can also use the keys() method to find out if a particular person was polled.

if 'rittu' not in favourite_cars.keys():
    print("Rittu, please our poll!")

# Looping through a dictonary's keys in a particular order

for name in sorted(favourite_cars.keys()):
    print(f"{name.title()}, Thank you ! for taking the poll.")

# Looping through all the values in a dictionary

print("The following car has been mentioned:")
for car in favourite_cars.values():
    print(car.title())

# TO see each car chosen without repetition, we use a "set". A set is a collection in which each item must be unique:
print("The following car has been mentioned:")
for car in set(favourite_cars.values()):
    print(car.title())