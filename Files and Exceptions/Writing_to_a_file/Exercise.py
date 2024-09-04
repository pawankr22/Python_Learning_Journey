"""Q1. Guest: Write a program that prompts the user for their name. When they
respond, write name to a file called guest.txt"""

name = input("What's your name?")
filename = 'guest.txt'

with open (filename, 'w') as f:
    f.write(name.title())

"""Q2. Guest book: Write a while loop that prompts users for their name. when they enter their name
, print a greetings to the screen and add a line recording their visit in a file called guest_book.txt
.Make sure each entry appears on a new line in the file."""

filename = 'guest_book.txt'

print("Enter Quit, when you are finished.")
while True:
    name = input("What's your name?")
    if name == 'Quit':
        break
    else:
        with open (filename, 'a') as f:
            f.write(name.title() + '\n')
            print("Hi " + name + ", You have been added to the guest book.")