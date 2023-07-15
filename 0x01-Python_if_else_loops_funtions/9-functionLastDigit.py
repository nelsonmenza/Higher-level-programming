#!/usr/bin/python3
# Function to print the last digit of a number
def last_digit(num):
    if not (num < 10 or num > -10):
        # If the number has more than one digit, calculate the last digit
        last_digit = abs(num % 10)
    else:
        # If the number has only one digit, it is the last digit
        last_digit = abs(num)
    return last_digit


# Take user input
num = int(input("Introduce a number: "))

# Call the function to get the last digit of the number
print(last_digit(num))
