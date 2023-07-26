#!/usr/bin/python3
# Print all possible combinations of numbers from 0 to 99
for i in range(100):
    if i != 99:
        # Print the number followed by a comma and a space
        print(i, end=", ")
    else:
        # Print the last number without a comma
        print(i)
