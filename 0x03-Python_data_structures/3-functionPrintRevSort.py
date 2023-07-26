#!/usr/bin/python3
def list_reverse(lst):
    # Sort the list in descending order
    lst.sort(reverse=True)
    # Print the reversed list
    print(lst)

 # Test the function with a sample list
lst = [1, 2, 3, 4, 5, 6, 7]
list_reverse(lst)
