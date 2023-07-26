#!/usr/bin/python3
# This function replaces an element at a specific position.
def replace_element(lst):
    new_lst = []
    # Copy elements from lst to new_lst
    for i in lst:
        new_lst.append(i)
     # Ask for the new element to be inserted
    new_element = input('Enter an element: ')
    # Ask for the type of data.
    while True:
        data = input(
            'Enter the type of data you want to add to the list. Enter (I) for int and (S) for string: ')
        # Convert new_element to int if data is 'i'
        if data.lower() == 'i':
            new_element = int(new_element)
            break
        # Break the loop if data is 's'
        elif data.lower() == 's':
            break
        else:
            print('Enter a valid input.')  # Loop for invalid input.
     # Ask for the position to insert the new element
    new_position = int(input(
        f'Enter the position where you want to insert the value (0 to {len(lst)-1}): '))
    # Replace the element at the specified position
    new_lst[new_position] = new_element
    # Return the list with the new item
    return f'List with the element inserted: {new_lst}'


lst = [1, 2, 3, "a", 5, 6, 4]
try:

    print(replace_element(lst))
    print(f'First list: {lst}')
except ValueError:
    print('Error, check your input.')
