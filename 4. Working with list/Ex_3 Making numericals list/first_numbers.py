# To print the counting from 1 to 5 we use following method.
for value in range(1, 6):
    print(value) # This will print 1 to 5 bcz of the off-by-one behaviour

# To print the counting from 1 to 10 we will have to write the following program:
for value in range(1, 11):
    print(value)

print("\n")

# The following code will print the no.from 0-5.
for value in range(6):
    print(value)

# To print a list of numbers we can use : list(range(1,5))
numbers = list(range(1,5))
print(numbers)
