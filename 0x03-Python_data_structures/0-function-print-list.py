# Function to print all the element of list
list = [1, 2, 3, 4, 5, 6, 8, 9, 10]


def print_list(list):
    i = 0
    while True:
        if i == len(list):
            break
        else:
            print(list[i])
            i += 1


print_list(list)
