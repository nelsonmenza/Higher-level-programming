#!/usr/bin/python3
# Print the alphabet
for a in range(ord("a"), ord("z")+1):
    if (a != 101 or a != 113) and (a != ord("z")):
        print(f"{chr(a)},", end=" ")
    else:
        print(f"{chr(a)}", end="")
