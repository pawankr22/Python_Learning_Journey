"""Q. Number Served: Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and 
print the value again.
Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a 
day of business."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow users to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to icrement the number of customers served.""" 
        self.number_served += additional_served

restaurant = Restaurant('The Taj', 'Burger')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))

restaurant.number_served = 234
print("Number served :" + str(restaurant.number_served))

restaurant.set_number_served = 1400
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served = 1300
print("Number served: " + str(restaurant.number_served))