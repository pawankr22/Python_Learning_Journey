# Tuple

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# Tuple is a permanent list which cannot be changed externely
# dimension[0] = 240 # This will throw an error as 'tuple' does'nt support item assignment

# Tuples are technically defined by the presence of comma, if there is only one item then we should use ',' after
my_t = (4,)

# Looping through all the values in a tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# writing over a tuple

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimension = (400,23)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)