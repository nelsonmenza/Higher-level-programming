#!/usr/bin/python3
# Function to print numbers from 1 to 100 with replacements for multiples of 3, 5, or both
def prt_num():
    for n in range(1, 101):
        if n % 15 == 0:
            n = "FizzBuzz"
        elif n % 3 == 0:
            n = "Fizz"
        elif n % 5 == 0:
            n = "Buzz"
        print(n, end=" ")


# Call the function to print the numbers
prt_num()
