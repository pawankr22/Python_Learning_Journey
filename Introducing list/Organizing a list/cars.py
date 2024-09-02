'''Sorting a list permanently with the sort() method'''

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort() # This will arrange the cars in alphabetical order and it can never be changed, it it permanent.

print(cars)

# TO arrange the items of list from Z-A, we use the argument reverse=True

cars.sort(reverse=True) # Again this is permanent and can never be changed.
print(cars)

'''Sorting a list temporarily with the sorted() function'''

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

## The sorted() function also accept the a revers=True argument .

'''Printing a list in reverse order using "reverse()" method '''

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars)

'''This will print the items in reverse order and this is also permanent but we can revert
   to the original order anytime by applying reverse() to the same list a second time 
'''
cars.reverse()
print(cars)


'''Finding the length of a list using the  "len()" function '''
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
length_of_the_list = len(cars)

print("The length of the list is :" , length_of_the_list)


'''Avoiding index errors when working with lists'''
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars[5])  # This will throw an error because there is no index of 5 as it start indexing from 0.
