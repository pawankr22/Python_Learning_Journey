'''Q.Message: Write a function called display_message() that prints one sentence
 telling everyone what you are learning about in this chapter. Call the 
function, and make sure the message displays correctly.'''

def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()


"""Q.  Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call."""

def favourite_book(title): # Here title is a parameter.
    """Display favourite book"""
    print(f"\nOne of my favourite books is {title}.")

favourite_book('Alice in Wonderland')
favourite_book('Do Epic Shit') # Here we can call as many arguments as we can.
