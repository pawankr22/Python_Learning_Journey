import pyjokes

# Generate a random joke
joke = pyjokes.get_joke()
print("Here's a random joke for you:")
print(joke)

# Generate a joke in a specific language and category
joke_neutral = pyjokes.get_joke(language='en', category='neutral')
print("\nHere's a neutral joke:")
print(joke_neutral)
