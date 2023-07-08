# function replaces an element at a specific position.
list = [1, 2, 3, "a", 5, 6, 5]
nw_list = []


def replace_elemt(list):
    nw_elem = input("Write a element: ")
    while True:
        position = int(input("Write a potition: "))
        if position <= len(list):
            break
        else:
            continue
    while True:
        nw_list = []
        for i in range(len(list)):
            list_elemt = list[i]
            nw_list.append(list_elemt)

        return nw_list


print(replace_elemt(list))
