'''Q. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.'''

def make_shirt(size,message):
    """summarize the size of the shirt and the message printed on it"""
    print(f"\nI will make a {size} shirt.")
    print(f"It will show the message '{message}'.")

make_shirt('large' , 'Be Bold')
make_shirt(message='readability counts' , size='medium') # this is calling the function using keyword arguments.

'''Q. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message.'''

def make_shirt(message, size = 'large'):
    """summarize the size of the shirt and the message printed on it"""
    print(f"\nI will make a {size} shirt.")
    print(f"It will show the message '{message}'.")

make_shirt('I love python')
make_shirt(message='This is not a bug , Its a function.' , size='medium')


'''Q.  Cities: Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the 
default country.'''

def describe_city(city,country='India'):
    """Printing the city and the country"""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('New Delhi')
describe_city('pune')
describe_city('london' , 'britain')