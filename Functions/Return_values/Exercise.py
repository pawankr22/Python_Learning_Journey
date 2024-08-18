'''Q.City Names: Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the 
values that are returned.'''

def city_country(city , country):
    """Return a string like 'Santiago,Chile'"""
    return f"{city.title()}, {country.title()}"

city = city_country('pune' , 'india')
print(city)

city = city_country('mumbai' , 'india')
print(city)

city = city_country('punjab' , 'india')
print(city)

'''Q.  Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Use None to add an optional parameter to make_album() that allows you to 
store the number of songs on an album. If the calling line includes a value for 
the number of songs, add that value to the album’s dictionary. Make at least 
one new function call that includes the number of songs on an album.'''

def make_album(artist, title , tracks=0):
    """Build a dictionary containing an information about an album"""
    album_dict = {
        'artist' : artist.title(),
        'title' : title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)