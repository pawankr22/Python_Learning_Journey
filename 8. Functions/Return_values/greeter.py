# Using a function with a while loop

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop 
while True:
    print("\nPlease tell me your first name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("first_name: ")
    if f_name == 'q':
        break
    l_name = input("last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")