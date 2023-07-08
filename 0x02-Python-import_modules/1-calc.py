#!/usr/bin/python3
"""Write a function that sum, sub, mul and div and return the result.
    -Create a module to import each function and print examples of each function"""
# Import the calcModule module that contains arithmetic functions
from modules import calcModule

# Prompt the user to enter two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Print the sum of the two numbers using the sum() function from the calcModule
print("The sum of the two numbers is: ", calcModule.sum(a, b))

# Print the difference between the two numbers using the sub() function from the calcModule
print("The difference between the two numbers is: ", calcModule.sub(a, b))

# Print the product of the two numbers using the mult() function from the calcModule
print("The product of the two numbers is: ", calcModule.mult(a, b))

# Print the quotient of the two numbers using the div() function from the calcModule
print("The quotient of the two numbers is: ", calcModule.div(a, b))
