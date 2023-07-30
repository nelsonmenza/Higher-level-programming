#!/usr/bin/python3
# Function to find the maximum value in a list
def find_max(lst):
    if len(lst) == 0:
        return None
    else:
        lst.sort()
    return lst[-1]

 # Test cases
my_list = [1, 1, 2, 13, 34, 5, 90, -13, 3]
max_value = find_max(my_list)
print("Max: {}".format(max_value))
my_list = [-91, -90]
max_value = find_max(my_list)
print("Max: {}".format(max_value))
my_list = [1]
max_value = find_max(my_list)
print("Max: {}".format(max_value))
my_list = []
max_value = find_max(my_list)
print("Max: {}".format(max_value))
my_list = [-5, -1, -5]
max_value = find_max(my_list)
print("Max: {}".format(max_value))
