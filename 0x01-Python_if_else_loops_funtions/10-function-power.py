#!/usr/bin/python3
# function that compute 'a' to the power of 'b' and return the value.
def power_num(a, b):
    power = a**b
    return power


a = int(input("Introduce a number: "))
b = int(input("Introduce a number: "))

print(power_num(a, b))
