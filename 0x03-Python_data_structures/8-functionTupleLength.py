#!/usr/bin/python3
def tuple_str_value(string):
    # Check if the string is empty
    if not string:
        return None
    # Create the tuple with the length and first character
    str_tuple = (len(string), string[0])
    # Return the tuple
    return str_tuple
