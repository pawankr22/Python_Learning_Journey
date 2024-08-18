# To print the square of the numbers between 1-10:
squares  = []
for value in range(1, 101):
    # square = value**2
    squares.append(value**3) # To use more concisely
print(squares)

# Same code which has written above to print a result can be done in only one line of code:
squares = [value**2 for value in range(1,11)]
print(squares)