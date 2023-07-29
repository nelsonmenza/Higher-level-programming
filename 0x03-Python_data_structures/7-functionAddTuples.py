#!/usr/bin/python3
# Function to add two tuples
def add_tuples(tuple1, tuple2):
    new_tuple = []
    length1 = len(tuple1)
    length2 = len(tuple2)
    i = 0
    # Iterate through the tuples
    while True:
        sum = 0
        # Check if both tuples have elements at the current index
        if i < length1 and i < length2:
            sum = tuple1[i] + tuple2[i]
            i += 1
            new_tuple.append(sum)
         # If only tuple1 has elements at the current index
        elif i < length1:
            new_tuple.append(tuple1[i])
            i += 1
         # If only tuple2 has elements at the current index
        elif i < length2:
            new_tuple.append(tuple2[i])
            i += 1
         # If both tuples have been fully traversed
        else:
            break
    return tuple(new_tuple)


# Test cases
tuple_a = (1, 89)
print(add_tuples(tuple_a, (1, 2, 3, 4, 5)))
print(add_tuples(tuple_a, (1, 2, 3)))
print(add_tuples(tuple_a, (1, 2)))
print(add_tuples(tuple_a, (1,)))
print(add_tuples(tuple_a, ()))
