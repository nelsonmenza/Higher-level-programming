#!/usr/bin/python3
# A script to validate if the last digit is negative or positive

import random
number = random.randint(-10000, 10000)

if (number < 0):
    lastDigit = number % -10
elif (number > 0):
    lastDigit = number % 10

print("The last digit of {:d} is {:d}".format(number, lastDigit), end="")

if (lastDigit > 5):
    print(" and is greater than 5")
elif (lastDigit < 6 and lastDigit != 0):
    print(" and is less than 6 and not 0")
elif (lastDigit == 0):
    print(" and is zero")
