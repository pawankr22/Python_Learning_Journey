# What will happen if ask for the point of an alien that doesnot have the point value set

alien_0 = {'color': 'green', 'speed' : 'medium'}
# print(alien_0['points']) # this will throw an error so instead of getting error we use "get()"

# get()
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
