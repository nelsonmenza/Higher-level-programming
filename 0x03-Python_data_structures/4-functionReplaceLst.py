#!/usr/bin/python3
# Function to replace an element at a specific position
def replace_element(lst, position, new_element, ):
    # Check if position is valid
    if position >= len(lst):
        return "Enter a valid position."
    else:
        new_lst = []
        # Copy elements from lst to new_lst
        for i in lst:
            new_lst.append(i)
        # Replace the element at the specified position
        new_lst[position] = new_element
        # Return the list with the new item
        return f'List with the element inserted: {new_lst}'

 # Initial list
lst = [1, 2, 3, "a", 5, 6, 4]
# Test the replace_element function
print(replace_element(lst, 6, 'NELSON'))
print(f'First list: {lst}')
