#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000.
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute number.
last_digit = abs(number) % 10

# If the number is less than 0, change the last digit to a negative number.
if number < 0:
    last_digit = -abs(last_digit)

# Print the last digit of the number.
print("The last digit of {:d} is {:d}".format(number, last_digit), end="")

# Determine additional information based on the value of the number and last digit.
if number > 5 and last_digit != 0:
    print(" and is greater than 5")
elif number < 6 and last_digit != 0:
    print(" and is less than 6 and not 0")
elif last_digit == 0:
    print(" and is 0")
