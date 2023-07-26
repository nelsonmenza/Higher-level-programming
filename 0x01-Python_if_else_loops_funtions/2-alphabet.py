#!/usr/bin/python3
# Print the alphabet in lowercase
for a in range(ord("a"), ord("z")+1):
    if a != ord("z"):
        # Print each lowercase letter followed by a comma and a space
        print(f"{chr(a)}", end=", ")
    else:
        # Print the last lowercase letter without a comma
        print(f"{chr(a)}")
