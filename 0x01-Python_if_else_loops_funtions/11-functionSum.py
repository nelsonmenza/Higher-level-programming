#!/usr/bin/python3
# Function to compute the sum of 'a' and 'b'
def sum_num(a, b):
    sum = a + b
    return sum


# Take user input for 'a' and 'b'
a = int(input("Introduce a number for 'a': "))
b = int(input("Introduce a number for 'b': "))

# Call the function to compute the sum of 'a' and 'b'
print(sum_num(a, b))
