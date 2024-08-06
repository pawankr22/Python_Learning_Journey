# Slicing a list 

players = ['Virat' , 'Rohit' , 'Bumrah' , 'Dhoni' , 'Sachin']

# It will print rohit , bumrah and dhoni as python stops one before the call 
print (players[1:4]) 

# It will print virat, rohit and bumrah
print(players[0:3])  

# It will starts from 0 and print till 4 means : virat , rohi , bumrah and dhoni
print(players[:4]) 

# It will starts from 2 and will print till the end
print(players[2:])

# It will print the last three players from the list
print(players[-3:])

# It will starts from 0 and will go till 2
print(players[:-2])

'''Looping through a Slice'''
players = ['Virat' , 'Rohit' , 'Bumrah' , 'Dhoni' , 'Sachin']
print("Here are the first three members of my team:")
for player in players[:3]:
    print(player.title())