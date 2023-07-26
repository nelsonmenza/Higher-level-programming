#!/usr/bin/python3
# Recursive Index Retrieval
def retrieve_index(lst, num):
    try:
        if 0 <= num < len(lst):  # Check if num is within the range of the list
            return lst[num]  # Return the element at the specified index
    except (ValueError, IndexError):  # Catch any ValueError or IndexError exceptions
        # Print an error message for invalid input
        print('Enter a valid value.')
        # Recursively call the function to try again
        return retrieve_index(lst, num)


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# Prompt the user to enter a number
num = int(input(f'Enter a number between 0 and {len(my_list)-1}: '))
# Print the result of the retrieve_index function
print(retrieve_index(my_list, num))
