#!/usr/bin/python3
# Function to change a character to uppercase
def change_upper(chr):
    if chr == chr.lower():
        # If the character is lowercase, convert it to uppercase
        chr = chr.upper()
    return chr


# Take user input
chr = input(
    "Introduce a character, either uppercase or lowercase, from 'a' to 'z': ")

# Call the function to change the character to uppercase if needed
print(change_upper(chr))
