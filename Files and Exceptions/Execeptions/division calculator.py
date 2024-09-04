# Handling the zero divison error

# Using try-except blocks
try:
    print(87/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exception to prevent crashes
print("Give me two numbers I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("second_number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

