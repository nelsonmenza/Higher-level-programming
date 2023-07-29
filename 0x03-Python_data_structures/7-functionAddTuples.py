#!/usr/bin/python3
# Function to add two tuples
def add_tuples(tuple1, tuple2):
    new_tuple = []
    length1 = len(tuple1)
    length2 = len(tuple2)
    num1 = 0
    num2 = 0
    max_length = max(length1, length2)
    for i in range(max_length):
        if i < length1:
            num1 += tuple1[i]

        if i < length2:
            num2 += tuple2[i]

    new_tuple.append(num1+num2)
    return tuple(new_tuple)
