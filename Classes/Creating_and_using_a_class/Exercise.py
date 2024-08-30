"""Q. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('The Taj', 'Burger')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

"""Q.Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

"""Q. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user."""

class User:
    """Create a simple user profile."""
    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user."""
        self.first_name  = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.address = address.title()

    def describe_user(self):
        """Summary of the user profile."""
        print("\n" + self.first_name + "" + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.username)
        print(" location: " + self.address)

    def greet_user(self):
        """Display a personalized greetings to the user."""
        print("\nWelcome back, " + self.username + "!")

pawan = User('pawan' , 'kumar', 'p_kumar', 'cnct.pawan@gmail.com', 'faridabad')
pawan.describe_user()
pawan.greet_user()

sweta = User('sweta' , 'priya', 's_priya', 'cnct.swewta@gmail.com', 'gurgaon')
sweta.describe_user()
sweta.greet_user()