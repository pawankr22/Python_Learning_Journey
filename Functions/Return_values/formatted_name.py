# returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('pawan', 'kumar')
print(musician)

# making an argument optional
# Like if a name has a middle name we need to add the middle name argument with optional so that 
# if a person without a middle name can also enter their name without any problem.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return an full name neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('pawan','kumar')
print(musician)
musician = get_formatted_name('rittu' , 'raj' , 'pranav')
print(musician)