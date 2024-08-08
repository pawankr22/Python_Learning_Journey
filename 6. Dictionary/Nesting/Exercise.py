'''People: Start with the program you wrote for Exercise 6-1 (page 99). 
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