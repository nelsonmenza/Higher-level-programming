#!/usr/bin/python3
# Print the alphabet in lower case
for a in range(ord("a"), ord("z")+1):
    if a != ord("z"):
        print(f"{chr(a)}", end=", ")
    else:
        print(f"{chr(a)}")
