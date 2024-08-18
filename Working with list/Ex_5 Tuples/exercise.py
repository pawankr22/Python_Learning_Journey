'''Q. A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the 
change.'''


food_items= ('dal roti', 'makhani', 'chole bathure', 'samosa', 'bread')
print("Food items:")
for item in food_items:
    print(f"-{item}".title())


'''•	 The restaurant changes its menu, replacing two of the items with different 
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.'''

food_items = ('dosa', 'makhani', 'ice-cream', 'samosa', 'bread')
print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in food_items:
    print(f"- {item}".title())