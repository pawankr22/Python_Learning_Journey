# A simple dictionary
alien_0 = {'color' : 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

# If a player shoot downs and alien how much should they get..
new_points = alien_0['points']
print(f"you have just earned {new_points} points!")

# adding x and y coordinates poistion of alien
alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0) 

# To modify a value in a dictionary, let's change color of the alien
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Let's track the position of an alien that can move a different speed

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# removing key value pairs . The removed key value pairs are removed permanentaly
alien_0 = {'color' : 'green', 'points':5}
del alien_0['points']
print(alien_0)