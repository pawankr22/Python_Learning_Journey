# Removing all the instances of specific values from a list

pets = ['dog' , 'cat' , 'goldfish' , 'dog' , 'cat' , 'rabbit' , 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)