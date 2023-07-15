#!/usr/bin/python3
# Function to compute 'a' to the power of 'b'
def power_num(a, b):
    power = a**b
    return power


# Take user input for 'a' and 'b'
a = int(input("Introduce a number for 'a': "))
b = int(input("Introduce a number for 'b': "))

# Call the function to compute the power of 'a' raised to 'b'
print(power_num(a, b))
