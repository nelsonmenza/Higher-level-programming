#!/usr/bin/python3
# Print the alphabet
for a in range(ord("a"), ord("z")+1):
    if (a != 101 or a != 113) and (a != ord("z")):
        # Print each letter, excluding 'e' and 'q', followed by a comma and a space
        print(f"{chr(a)}", end=", ")
    else:
        # Print the last letter without a comma
        print(f"{chr(a)}")
