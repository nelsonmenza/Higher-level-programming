#!/usr/bin/python3
"""Write a function that sums two number and return the result.
    -Create a module to import the function add() and print the result
"""
# Import the addmodule module that contains the add() function
from modules import addModule

# Prompt the user to enter two numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# Print the result of adding the two numbers using the add() function from the addmodule
print(addModule.add(a, b))
