#!/usr/bin/python3
# Function that print the last digit of number.
def last_digit(num):
    if not (num < 10 or num > -10):
        last_digit = abs(num % 10)
    else:
        last_digit = abs(num)
    return last_digit


num = int(input("Introduce a number: "))

print(last_digit(num))
