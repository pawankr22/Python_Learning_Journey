'''•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 
5 tests evaluate to False.'''


'''Q. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:'''

# Test no. 1
car = 'velar'
print ("Is car == 'velar'? I predict True")
print(car == 'velar')

print ("Is car == 'audi'? I predict false.")
print (car == 'audi')

# Test no. 2
bike = 'ninja'
print("Is bike == 'ninja'? I predict true.")
print(bike == 'ninja')

print("Is bike == 'kawasaki'? I predict false.")
print(bike == 'kawasaki')

# Test no. 3
book = 'homosapians'
print("Is the book == 'homosapians'? I predict true.")
print(book == 'homosapians')

print("Is the book == 'mahabharat'? I predict false.")
print(book == 'mahabharat')

# Test no.4
food = 'paneer'
print("Is the food == 'dal makhani'? I predict false.")
print(food == 'dal makhani')

print("Is the food == 'paneer'? I predict true.")
print(food == 'paneer')

# Test no. 5
tourist_place = 'goa'
print("Is the tourist_place == 'goa'? I predict true.")
print(tourist_place == 'goa')

print("Is the tourist_place == 'sikkim'? I predict false.")
print(tourist_place == 'sikkim')

# Test no. 6
friend = 'gobar'
print("Is the friend == 'gobar'? I predict true.")
print(friend == 'gobar')

print("Is the friend == 'bhains'? I predict false.")
print(friend == 'bhains')


'''Q.You don’t have to limit the number of tests you 
create to 10. If you want to try more comparisons, write more tests and add 
them to conditional_tests.py. Have at least one True and one False result for 
each of the following:'''

# •	 Tests for equality and inequality with strings
# equality(==)
str1 = "Harry"
str2 = "harry"
print(str1 == str2) # false

# inequality(!=)
str1 = "Cherry"
str2 = "Teddy"
print(str1 != str2)  # True

# •	 Tests using the lower() function
str1 = "Harry"
str2 = "harry"
print(str1.upper() == str2.upper()) # True

# Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to

car = "Audi"
god = 1

print(car.lower() == "audi")  # True
print(car.upper() == "Audi")  # False
print(god == 1)              # True
print(god > 0)               # True
print(god > 10)              # False
print(god > 1)               # False
print(god < -1)              # False

# Tests using the and keyword and the or keyword
# and

ganesh_age = 22
ramesh_age = 20

print(ganesh_age >=21 and ramesh_age <=19) # false

# or
ganesh_age = 22
ramesh_age = 20

print(ganesh_age >=21 or ramesh_age <=19) # true

# Test whether an item is in a list
fruits = ['banana' , 'grapes' , 'orange' , 'coconut']
fruit_required = "grapes"

print(f"{fruit_required.title()} is in the bucket.")

#  Test whether an item is not in a list
patient = ['murari' , 'shankar' , 'abhishek' , 'tipu']
patient_available = "mukesh"

print(f"{patient_available.title()} is the only patient who is currently avaible now.")