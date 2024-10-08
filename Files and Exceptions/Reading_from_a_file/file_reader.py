with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents,"\n")

# Using a for loop on the file object to examine each line from a file one at a time.
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# making a list of lines from a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())