'''Q.1  Rental Car: Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as “Let me see if I can find you 
a Subaru.”'''

car = input("What kind of car do you like? ")
print(f"Let me see if I can find you a {car.title()}.")

'''Q2.  Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying 
they’ll have to wait for a table. Otherwise, report that their table is ready.'''

party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

'''Q.3  Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not.'''

number = input("Enter a number, and I'will tell you whether it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of 10.")
else:
    print(f"\nThe number {number} is not multiple of 10.")