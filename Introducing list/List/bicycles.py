''' List is a collection of items in a particular order. We can make a list that includes the letters the letters of the alphabet
,the digit from 0-9, or the names of all the people , like in our family.'''


bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print(bicycles)

# Accessing elements in a list
print(bicycles[0]) # this will print trek.
print(bicycles[1].title()) # .title() will make the initial letter capital

# To access the last item of a list We use [-1]
print(bicycles[-1].title()) # this code will print the last item of the list  i.e . specialized

'''Similarly The index -2 returns the second item from the end of the list, the -3 returns the third item from the end and so forth'''


# Using individual values from a list

# WE can use f-string to create a message based on value from the list.
message = f"My first bicycle was a {bicycles[3].title()}."
print(message)