def delete_item(lst, indx):
    # Create a copy of the list
    lst_update = lst[:]
    # Delete the item at the specified index
    del lst_update[indx]
    # Print the original list
    print('Original List: ', lst)
    # Print the updated list with the item deleted
    print(f'List with deleted item at index {indx}: ', lst_update)


my_list = [1, 1, 2, 13, 34, 5, 90, -13, 3]
delete_item(my_list, 4)
