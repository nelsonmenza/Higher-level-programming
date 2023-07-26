#!/usr/bin/python3
# Slice and concatenate a string
string_slice = """Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with 
very clear syntax"""
# Stored different parts and print the result.
first_part = string_slice[39:67]
second_part = string_slice[107:112]
third_part = string_slice[0:6]
# The end result must be the following: "object-oriented programing Python"
print(f'"{first_part}{second_part}{third_part}"')
