#!/usr/bin/python3
def multiply_by_two(lst):
    """
    Returns a list with all the multiples of 2 in the input list.
    """
    new_lst = []
    for n in lst:
        if n % 2 == 0:
            new_lst.append(n)
    return f'List with all multiples of 2: {new_lst}'


my_list = [1, 1, 2, 13, 34, 5, 90, -13, 3]
print(multiply_by_two(my_list))
