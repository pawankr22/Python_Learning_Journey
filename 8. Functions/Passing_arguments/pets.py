# positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('doggo' , 'harry') 
# multiple function  call   
describe_pet('cat', 'mausi')
# Here we can call as many positional arguments as we need but the position matters,
# if we mix up the order we can get unexpected results like if we call "doggo" in place of
# pet_name and call "harry" in the place of dog's type.

"""Keyword arguments: what if we we write like this:
describe_pet(animal_type='doggo', pet_name='harry')"""
# the above statement we print the exact call which we have given/

'''There can also be a default value set to the animal_type or to the pet_name'''
def describe_pet(pet_name ,animal_type='dog'):
    """Display information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('doggo')

'''Equivalent function call'''
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named willie
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Each of the above function calls would have the same output as the previous examples

'''Avoiding Arguments Errors'''
# If we simply write "describe_pet()" This function will through an error.
