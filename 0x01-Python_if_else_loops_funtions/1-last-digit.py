#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# last_digit absolute number.
last_digit = abs(number) % 10
# if the number is less than 0 change to negative number.
if number < 0:
    last_digit = -abs(last_digit)
print("The last digit of {:d} is {:d}".format(number, last_digit), end="")
#
if number > 5 and last_digit != 0:
    print(" and is greater than 5")
elif number < 6 and last_digit != 0:
    print(" and is less than 6 and not 0")
elif last_digit == 0:
    print(" and is 0")
