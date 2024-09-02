#  Think of at least five places in the world you’d like to visit.
destinations = ['Manali' , 'New york' , 'Rishikesh' , 'Amsterdam' , 'London']
print(destinations)

''' Use sorted() to print your list in alphabetical order without modifying the actual list.'''
print(sorted(destinations))

''' Show that your list is still in its original order by printing it.'''
print("The items are still in its original order:", destinations)

''' Use sorted() to print your list in reverse alphabetical order without changing the order of the original list'''
reverse_sorted_list = sorted(destinations, reverse=True)
print(reverse_sorted_list)

''' Show that your list is still in its original order by printing it again'''
print("The list is still in the original order:", destinations)

''' Use reverse() to change the order of your list. Print the list to show that its order has changed.'''
destinations.reverse()
print("The list has reversed:" , destinations)

'''Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.'''
destinations.sort()
print(destinations)

''' Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.'''
destinations.sort(reverse=True)
print(destinations)


'''Working with one of the programs from Exercises 3-4 
through 3-7 (page 46), use len() to print a message indicating the number 
of people you are inviting to dinner.'''

# Guest list
guests = ['Rittu', 'Raushan', 'Subodh']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

length_of_the_list = len(guests)
print("Total no. of guest are:", length_of_the_list)

'''Think of something you could store in a list. For example, 
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.'''