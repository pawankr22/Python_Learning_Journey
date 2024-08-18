alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# storing each aliens in a list
aliens = [alien_0, alien_1, alien_2]

# looping through the list.
for alien in aliens:
 print(alien)

'''A more realistic example would involve more than three aliens with 
code that automatically generates each alien. In the following example we 
use range() to create a fleet of 30 aliens:'''

# Making an empty list for storing aliens.
aliens = []
# Making 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# To change the first three aliens to  yellow,medium-speed aliens worth 10 points each.
for alien in aliens[:3]:
   if alien['color'] ==  'green':
      alien['color'] = 'yellow'
      alien['speed'] = 'medium'
      alien['points'] = 10
   elif alien['color'] == 'yellow':
      alien['color'] = 'red'
      alien['speed'] = 'fast'
      alien['points'] = 15
 
# Show the first 20 aliens.
for alien in aliens[:20]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")