#!/usr/bin/python3
# Function that change a character to uppercase.
def change_upper(chr):
    if chr == chr.lower():
        chr = chr.upper()
    return chr


chr = input("Introduce a character upper o lower, from a to z: ")
print(change_upper(chr))
