# modifying a list in a function

# List without using function to modify it later using function
# Start with some designs that need to be printed.
unprinted_designs = ['book','phone case', 'robot pendant', 'cup']
completed_models = []

# simulate printing each design, until none are left.
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models:
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Reorganizing the above code by writing two functions

# 1st function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)

# 2nd function
def show_completed_models(completed_models):
    """show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_models)

unprinted_designs = ['book' , 'phone case' , 'robot pendant', 'cup']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)