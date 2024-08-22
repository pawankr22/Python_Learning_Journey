# Passing An Arbitary Number Of Arguments

def make_pizza(*toppings):
    """Summarize the pizza we want are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    """Print the list of toppings that have been requested."""
    # print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# mixing positional and arbitary arguments

# If the  function needs to take in a size for the pizza,
# that parameter must come before the parameter *toppings

def make_pizza(size, *toppings):
    """summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
make_pizza(10, 'butter', 'mushroom')