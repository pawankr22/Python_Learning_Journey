'''Q. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:'''


cars = ['bmw' , 'audi' , 'bentley' , 'ferrari' , 'range rover' , 'aston martin']
print(cars[:5])

# Print the message, The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
print("The first four cars are: ")
for car in cars[:5]:
    print(car.title())

print("My favourite cars are : ")
for car in cars[2:5]:
    print(car.title())

# Print the message, Three items from the middle of the list are:. Use a slice 
# to print three items from the middle of the list.

cars = ['bmw' , 'audi' , 'bentley' , 'ferrari' , 'range rover' , 'aston martin']
print("Three items from the middle of the list are: ")
for car in cars [2:5]:
    print(car.title())

# Print the message, The last three items in the list are:. Use a slice to print 
# the last three items in the list.'''
cars = ['bmw' , 'audi' , 'bentley' , 'ferrari' , 'range rover' , 'aston martin']
print("The last three items in the list are: ")
for car in cars [-3:]:
    print(car.title())


'''Q. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list. Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.'''

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


'''Q. More Loops: All versions of foods.py in this section have avoided using 
for loops when printing to save space. Choose a version of foods.py, and 
write two for loops to print each list of foods.'''