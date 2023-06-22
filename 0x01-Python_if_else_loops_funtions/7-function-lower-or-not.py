#!/usr/bin/python3
# function to indentify if the character is lower or not.
def chr_validations(chr):
    if chr == chr.lower():
        chr_vld = True
    else:
        chr_vld = False
    return chr_vld


# Introduce a character.
chr = input("Introduce a character between a to z, lower or upper: ")
print(chr_validations(chr))
