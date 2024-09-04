# Writing to a file.
# Writing multiple lines.
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("This is appended line.\n")
    file_object.write("This is also a appended line.\n") 
    #  \n is included so that the both lines appears on the separate line.

# Appending a file.
