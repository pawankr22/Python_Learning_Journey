'''Q. Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary.'''

friend_1 = {
    'first_name' : 'Ramesh',
    'last_name' : 'shah',
    'age' : 19,
    'city' : 'faridabad'
}
print(friend_1['first_name'])
print(friend_1['last_name'])
print(friend_1['age'])
print(friend_1['city'])

# print(friend_1['first_name'] + friend_1['last_name'] )

'''Q. Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program.'''

favourite_numbers = {
    'avinash' : '45',
    'suraj' : '34',
    'shreya' : '23',
    'tulip' : '98',
    'dilip' : '00'
}

num = favourite_numbers['avinash']
print(f"Avinash's favourite number is {num}.")

num = favourite_numbers['suraj']
print(f"Suraj's favourite number is {num}.")

num = favourite_numbers['shreya']
print(f"Shreya's favourite number is {num}.")

num = favourite_numbers['tulip']
print(f"Tulip's favourite number is {num}.")

num = favourite_numbers['dilip']
print(f"Dilip's favourite number is {num}.")

'''A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.'''

'''Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.'''

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

'''	Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output.'''

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")