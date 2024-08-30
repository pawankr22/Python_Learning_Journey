"""Q. . Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):

    """Represent an ice cream stand."""
    def __init__(self, name, cuisine_type='ice_cream'):
        """initialize an icecream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


"""Q.  Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method."""
