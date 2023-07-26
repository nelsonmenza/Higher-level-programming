#!/usr/bin/python3
# Print all possible combinations of numbers from 0 to 99
for i in range(100):
    for j in range(i, 100):
        # Print the two numbers as a combination separated by a comma and a space
        print(i, j, sep=", ", end=" ")
