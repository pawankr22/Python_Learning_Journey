# # Checking for special items

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza\n")

# But what if pizzeria runs out of green peppers?

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are running out of green peppers.")
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")


# Checking that a list is not empty.
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza.")

else:
    print("Are you sure you want a plain pizza?")


# Using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Sorry, we don't have " + requested_topping + ".")
 
print("\nFinished making your pizza!")