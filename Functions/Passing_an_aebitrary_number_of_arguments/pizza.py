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