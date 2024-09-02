
# Excercise

'''Q. Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.'''

# Names of friends
names = ['Rohan' , 'Siddharth' , 'Abhishek' , 'Rittu' , 'Kanahaiya' , 'Subodh' , 'Raushan']

# This will print Rohan
print(names[0])

# This will print Siddharth
print(names[1])

# This will print Abhishek
print(names[2])

# This will print Rittu
print(names[3])

# This will print Kanahaiya
print(names[4])

# This will print Subodh
print(names[5])

# This will print Raushan
print(names[6])


''' Q. Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.'''

# Names of friends
names = ['Rohan' , 'Siddharth' , 'Abhishek' , 'Rittu' , 'Kanahaiya' , 'Subodh' , 'Raushan']

# message to Rohan
message = f"{names[0].title()} is my best freind. "
print(message)

# message to Siddharth
message =  f"{names[1].title()} is my special freind. "
print(message)

# message to Abhishek
message = f"{names[2].title()} is my second freind. "
print(message)

# message to Rittu
message =  f"{names[3].title()} is my third freind. "
print(message)

# message to Kanahaiya
message = f"{names[4].title()} is my fourth freind. "
print(message)

# message to Subodh
message = f"{names[5].title()} is my fifth freind. "
print(message)

# message to Raushan
message =  f"{names[6].title()} is my sixth freind. "
print(message)

'''Q. Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.'''


# List of favorite modes of transportation
favourite_transportations = ["Range Rover Vellar", "Ninja", "Boing 777", "Range Rover Autobiography"]

# Print statements about each item in the list
print(f"I would like to drive a {favourite_transportations[3].title()}.")
print(f"I would like to ride a {favourite_transportations[1].title()}.")
print(f"I would like to fly a {favourite_transportations[2].title()}.")
print(f"I would like to drive a {favourite_transportations[0].title()}.")

