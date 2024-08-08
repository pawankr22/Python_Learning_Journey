# A dictionary in a dictonary

# Storing three pieces of information about each user : First name , last name and location

users = {
    'pkumar' : {
        'first' : 'pawan',
        'last' : 'kumar',
        'location' : 'unknown',
    },

    'rroy' : {
        'first' : 'rohan',
        'last' : 'roy',
        'location' : 'deemapur',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tfull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")