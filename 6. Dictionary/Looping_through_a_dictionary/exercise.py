'''Q. Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When 
you’re sure that your loop works, add five more Python terms to your glossary. 
When you run your program again, these new words and meanings should 
automatically be included in the output.'''

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.'
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}.")

'''Q.Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.'''

rivers = {
    'ganga' : 'india',
    'yamuna' : 'india',
    'saraswati' : 'india',
}

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# •	 Use a loop to print the name of each river included in the dictionary.
print(f"\nThe following rivers are included in the data set:")
for river in rivers.keys():
    print(f"- {river.title()}.")

# 'Use a loop to print the name of each country included in the dictionary.
print(f"\nThe following country are included in the data set:")
for country in rivers.values():
    print(f"-{country.title()}.")

'''Use the code in favorite_languages.py (page 97).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not. 
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding. 
If they have not yet taken the poll, print a message inviting them to take 
the poll.'''