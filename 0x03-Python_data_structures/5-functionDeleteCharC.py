#!/usr/bin/python3
def delete_char(string):
    """
    Deletes all occurrences of the letter 'c' (case insensitive) from a given string.
     Args:
        string (str): The input string.
     Returns:
        str: The modified string with 'c' characters removed.
    """
    new_string = ''
    for char in string:
        if char.lower() == 'c':
            new_string += ' '
        else:
            new_string += char
    return new_string


print(delete_char("Holberton School"))
print(delete_char("Chicago"))
print(delete_char("C is fun!"))
