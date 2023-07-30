#!/usr/bin/python3
def swap_value(a, b):
    # Swaps the values of two variables
    # store the value of a in a temporary variable
    temp = a
    # assign the value of b to a
    a = b
    # assign the value of temp to b
    b = temp
    # print the swapped values of a and b
    print('The value of X: {:d} and Y: {:d} after swapping.'.format(a, b))


x = 5
y = 10
# print the original values of x and y
print('The value of X: {:d} and Y: {:d} before swapping.'.format(x, y))
# call the function to swap the values of x and y
swap_value(x, y)
