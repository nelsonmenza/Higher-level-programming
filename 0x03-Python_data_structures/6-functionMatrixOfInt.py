#!/usr/bin/python3
def matrix_unpacking(matrix):
    # Join each list with a space and print as a single string
    for lst in matrix:
        print(' '.join(map(str, lst)), end=' ')

 # Define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Call the matrix_unpacking function with the matrix as argument
matrix_unpacking(matrix)
