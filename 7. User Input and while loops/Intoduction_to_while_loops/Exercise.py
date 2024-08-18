'''Q.. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.'''

prompt = "\nEnter the pizza toppings which you will like to add to your pizza."
prompt += "\nEnter 'quit' to end the program."

while True:
 topping = input(prompt)
 if topping != 'quit':
    print(f"I will add {topping} to your pizza.")
 else:
    break

'''Q.  Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.'''

prompt = "\nWhat is your age?"
prompt += "\nEnter 'quit' when you are finished"

while True:
  age = input(prompt)
  if age == 'quit':
    break
  age = int(age)

  if age < 3:
    print(" Your ticket is free.")
  elif age < 13:
    print(" Your ticket fee is $10.")
  else:
    print(" Your ticket fee is $15.")

'''Q.  Write different versions of either Exercise 7-4 or Exercise 7-5 
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value.'''