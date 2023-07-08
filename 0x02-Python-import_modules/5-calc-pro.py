#!/usr/bin/python3
"""Write a function that sum, sub, mul and div and return the result.
    -Create a module to import each function and print examples of each function"""
# Import the calcmodule module that contains arithmetic functions
from modules import calcProModule

# Prompt the user to enter two numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
while True:
    operator = input("Enter a operator: ")
    operators = ["+", "-", "*", "/"]
    for i in operators:
        opr = operators[i]
        print(opr >= operator)

    print("Available operators: +, -, * and /")

# # Print the sum of the two numbers using the sum() function from the calcmodule
# print("The sum of the two numbers is: ", calcmodule.sum(a, b))

# # Print the difference between the two numbers using the sub() function from the calcmodule
# print("The difference between the two numbers is: ", calcmodule.sub(a, b))

# # Print the product of the two numbers using the mult() function from the calcmodule
# print("The product of the two numbers is: ", calcmodule.mult(a, b))

# # Print the quotient of the two numbers using the div() function from the calcmodule
# print("The quotient of the two numbers is: ", calcmodule.div(a, b))
