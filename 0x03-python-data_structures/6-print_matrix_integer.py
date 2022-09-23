#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    matrix_length = len(matrix)
    for i in range(len(matrix)):
        for y in matrix[i]:
            if counter != matrix_length - 1:
                print("{}".format(y), end=" ")
                counter += 1
            else:
                print("{}".format(y))
                counter = 0
    return matrix
