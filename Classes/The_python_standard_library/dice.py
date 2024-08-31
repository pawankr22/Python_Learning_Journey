from random import randint

"""Making a class Die"""
class Die():
    """Represent a die which can be rolled."""

    def __init__(self, sides=6):
        """Initializing the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and 6 sides."""
        return randint(1 , self.sides)

"""Making a 6 -sided die and rolling it 10 times."""
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10 sided die, and show the results of 10 rolls.

d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20 sided die, and show the results of 10 rolls.

d20 = Die(sides=20)

results = []
for roll_num in range(20):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20 sided die:")
print(results)