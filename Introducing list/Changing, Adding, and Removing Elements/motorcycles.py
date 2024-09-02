## Modifying Elements in a lists

# Lists of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying the lists of motorcycles
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[1] = 'Royal Enfield'
print(motorcycles)

motorcycles[2] = 'Kawasaki '
print(motorcycles)


## Adding elements to a list

# Appending element to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Adding more elements to the list using append()
motorcycles.append('ducati')
print(motorcycles)

# Adding items in the empty list
motorcycles = [] 

motorcycles.append('Bajaj') 
motorcycles.append('TVS') 
motorcycles.append('OLA') 

print(motorcycles)


## Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki'] 

# ducati will be added to the list using the insert() method
motorcycles.insert(0, 'ducati')  
print(motorcycles)

motorcycles.insert(1, 'bugati')  
print(motorcycles)



## Removing Elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

# Deleting honda from the list
del motorcycles[0] 
print(motorcycles)

# Deleting suzuki from the list
del motorcycles[1]
print(motorcycles)



## removing an item using the pop() method

# List of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Popped one of the item and stored in the variable "popped_motorcycle"
popped_motorcycle = motorcycles.pop() 

# this will print the motorcycles other than popped one
print(motorcycles)

# this will print the which motorcycle was popped
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 

''' If the items are listed in chronological order according to when we owned them. If this is the case, we can
use the pop() method to print a statement about the last motorcycle we bought.'''
last_owned = motorcycles.pop()

# This will print the senetence "The last motorcycle I owned was a Suzuki"
print("The last motorcycle I owned was a " + last_owned.title() + ".")

## Popping Items from any position in a list

motorcycles = ['honda' , 'yamaha' , 'suzuki']

first_owned = motorcycles.pop(0)

# This will print the sentence " The first mototcycle I owned was a honda"
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


## Removing an Item by value

motorcycles = ['honda' , 'yamaha' , 'suzuki' , 'ducati']
print(motorcycles)

# To remove the item we use the below code

motorcycles.remove ('ducati')
print(motorcycles)

'''We can also use the remove() method to work with a value that's being removed from a list. 
   Let's remove the value 'ducati' and print a reason for removing it from the list'''

motorcycles = ['honda' , 'yamaha' , 'suzuki' , 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")