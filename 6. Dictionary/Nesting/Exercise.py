'''Q.1 People: Start with the program you wrote for Exercise 6-1 (page 99). 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person.'''

# Make an empty list to store friend in.
People = []

# Friend 1
friend = {
    'first_name' : 'Ramesh',
    'last_name' : 'shah',
    'age' : 19,
    'city' : 'faridabad',
    }
People.append(friend)


# friend 2
friend = {
    'first_name' : 'Mukesh',
    'last_name' : 'sahu',
    'age' : 22,
    'city' : 'Gaziabad',
    }
People.append(friend)

# friend 3
friend = {
    'first_name' : 'Vinesh',
    'last_name' : 'Thakural',
    'age' : 29,
    'city' : 'Noida-west',
    }
People.append(friend)

# Display all the information of the dictionary
for friend in People:
    name = f"{friend['first_name'].title()} {friend['last_name'].title()}"
    age = friend['age']
    city = friend['city'].title()

    print(f"{name}, of the {city}, is {age} years old.")

'''Q.2 Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as 
you do, print everything you know about each pet.'''

# Make an empty list to store pet
pets = []

# pet 1
pet = {
    'animal type' : 'dog',
    'name' : 'salu',
    'age' : 5,
    'owner' : 'salman'
}
pets.append(pet)

# pet 2
pet = {
    'animal type' : 'cat',
    'name' : 'jerry',
    'age' : 3,
    'owner' : 'Tom'
}
pets.append(pet)

# pet 3
pet = {
    'animal type' : 'snake',
    'name' : 'python',
    'age' : 35,
    'owner' : 'jake'
}
pets.append(pet)

# pet 4
pet = {
    'animal type' : 'cow',
    'name' : 'dhano',
    'age' : 22,
    'owner' : 'rohan',
}
pets.append(pet)

# Display all informantion of the dictionary
for pet in pets:
    print(f"Here is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")


'''Q3. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places.'''

favourite_places = {
    'verma' : ['shimla', 'goa', 'manali'],
    'tony': ['kanyakumari', 'bangkok', 'london'],
    'ronit': ['singapur', 'srinagar', 'jammu'],
}

for name , places in favourite_places.items():
    print(f"\n{name.title()} likes the following places to tour:")
    for place in places:
        print(f"- {place.title()}")

'''Q 4. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.'''

favourite_numbers = {
    'sneha' : [43 , 45],
    'ramesh' : [69 , 89],
    'dinesh' : [23 , 45],
}

for name , numbers in favourite_numbers.items(): 
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"-{number}")


'''Q.5 Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information 
you have stored about it.'''

cities = {
    'faridabad': {
        'country' : 'india',
        'population' : 2_34_0000,
        'known-for' : 'new-delhi',
    },

    'mumbai': {
        'country' : 'india',
        'population' : 23_34_9090,
        'known-for' : 'bollywood',
    },

    'kolkata': {
        'country' : 'india',
        'population' : 85_54_09_322,
        'known-for' : 'mamta-banarji'
    } 
}

for city , city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    popularity = city_info['known-for']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"\tIt has a population of about {population}.")
    print(f"\tThe city is known for {popularity.title()}.")