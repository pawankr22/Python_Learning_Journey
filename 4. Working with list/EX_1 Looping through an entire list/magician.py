magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
    print(magician)

    # To start a loop for list of cats, a list of dogs and a general list of items
    # for cat in cats:
    # for dog in dogs:
    # for item in list_of_items:

for magician in magicians :
    print(f"{magician.title()}, that was a great trick!")
    print(f"Your speed was also great {magician.title()}.")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

    # print("Thank you , everyone. That was a great magic show!") This does'nt need to intended , so now it will throw an error.
print("Thank you , everyone. That was a great magic show!")


# loop for dogs
dogs = ['German' , 'Bulldog' , 'Pitbul']
for dog in dogs:
    print(dog)

for dog in dogs:
    print(f"{dog.title()} is a brave dog.")

# loop for cows
cows = ['sahiwal' , 'bull' , 'murrah']
for cow in cows :
    print(cow)

for cow in cows : 
    print(f"{cow.title()} is a good breed of cow.")


'''Avoiding Identation Errors'''
# Forgetting to indent

'''magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
print(magician) ''' # This code will throw an error because the print is not indented. 


#forgetting to indent the additional line
magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
# The print statement at below is supposed to be indented, but because 
# Python finds at least one indented line after the for statement, it doesn’t 
# report an error. As a result, the first print statement is executed once for 
# each name in the list because it is indented. The second print statement is 
# not indented, so it is executed only once after the loop has finished running. Because the final value of magician is 'carolina', she is the only one 
# who receives the “looking forward to the next trick” message:
   print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick {magician.title()}.\n")   