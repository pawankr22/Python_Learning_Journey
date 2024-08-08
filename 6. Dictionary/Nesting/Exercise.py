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

