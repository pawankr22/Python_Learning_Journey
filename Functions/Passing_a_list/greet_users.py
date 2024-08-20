# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in thr list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['abhishek', 'sumit' , 'verma']
greet_users(usernames)