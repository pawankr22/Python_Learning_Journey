'''Q. Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.'''

alien_color = ['green', 'yellow', 'red']

''' Write an if statement to test whether the alien’s color is green. If it is, print 
a message that the player just earned 5 points.'''

# passing version
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")

''' Write one version of this program that passes the if test and another that 
fails. (The version that fails will have no output.)'''
# failing version
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points.")

'''Q.2 : Choose a color for an alien as you did in Exercise 5-3, and 
write an if-else chain.'''

alien_color = 'yellow'

if alien_color == 'green':
    point = 5
elif alien_color == 'red':
    point = 0
else:
    point = 10

print(f"\nYou have earned {point} points.")

print("\n")

alien_color = 'green'

if alien_color == 'green':
    point = 5
elif alien_color == 'red':
    point = 0
else:
    point = 10

print(f"\nYou have earned {point} points.")

'''Q.. Stages of Life: Write an if-elif-else chain that determines a person’s 
stage of life. Set a value for the variable age, and then:'''

# Enter your age to check in which category you fall.
age = 0

# 	 If the person is less than 2 years old, print a message that the person is a baby.
if age < 2:
    print("You are a baby.")

#  If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
elif age < 4:
    print("You are a toddler.")

# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
elif age< 13:
    print("You are a kid.")

# If the person is at least 13 years old but less than 20, print a message that the person is a teenager
elif age < 20:
    print("You are a teenager.")

# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
elif age < 65:
    print("You are an adult.")

# If the person is age 65 or older, print a message that the person is an elder
else:
    print("You are an elder.")


'''Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list.'''

# Make a list of your three favorite fruits and call it favorite_fruits.

favourite_fruits = ['banana', 'apple', 'orange']

# Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!'''

if 'banana' in favourite_fruits:
    print("You really like bananas!")
if 'apple' in favourite_fruits:
    print("You really like apples!")
if 'orange' in favourite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favourite_fruits:
    print("You really like kiwis!")
if 'peaches' in favourite_fruits:
    print("You really like peaches!")