#!/usr/bin/python3
# function that print the number from 1 to 100 separated by space
"""If the number is multiple of 3:
    -Change the number to 'Fizz' 
   If the number is multiple of 5:
    -Change the number to 'Buzz'
   If ther number is multiple of 3 and 5
    -Change the number to 'FizzBuzz' """


def prt_num():
    for n in range(1, 101):
        if n % 15 == 0:
            n = "FizzBuzz"
        elif n % 3 == 0:
            n = "Fizz"
        elif n % 5 == 0:
            n = "Buzz"
        print(n, end=" ")


prt_num()
