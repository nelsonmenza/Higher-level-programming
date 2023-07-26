#!/usr/bin/python3
"""
A simple calculator program that imports a custom module to perform arithmetic operations.
- The calcProModule module contains functions for sum, subtraction, multiplication, and division.
- The user is prompted to enter two numbers and an operator to perform the desired operation.
"""

# Import the calcProModule module that contains arithmetic functions
from modules import calcProModule

try:
    # Prompt the user to enter two numbers
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    operator = input("Enter an operator (+, -, *, or /): ")
    if operator == "+":
        # Perform addition and print the result
        print(calcProModule.sum(a, b))
    elif operator == "-":
        # Perform subtraction and print the result
        print(calcProModule.sub(a, b))
    elif operator == "*":
        # Perform multiplication and print the result
        print(calcProModule.mult(a, b))
    elif operator == "/":
        # Perform division and print the result
        print(calcProModule.div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")

except ValueError:
    print("Usage: <a> <operator> <b>")
