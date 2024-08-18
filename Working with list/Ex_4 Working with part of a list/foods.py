# Copying a list using [:]

my_foods = ['Pizza' , 'veg nan' , 'paneer roll']
friends_foods = my_foods[:]

print("My favourite foods are : ")
print(my_foods)

print("My friend's favourite food are: ")
print(friends_foods)

# To add some non-similar food in both list : 

my_foods.append('samosa')
friends_foods.append('burger')

print("My favourite foods are : ")
print(my_foods)

print("My friend's favourite food are: ")
print(friends_foods)