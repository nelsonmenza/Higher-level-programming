#!/usr/bin/python3
# Print all the posible combinations in numbers betwee 00 to 99
for i in range(100):
    for j in range(i, 100):
        # :0 add another 0 if the number is less than two digits.
        print("{:0=2d}, {:0=2d}".format(i, j))
