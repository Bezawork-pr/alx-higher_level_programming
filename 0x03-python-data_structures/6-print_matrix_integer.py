#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    matrix_length = len(matrix)
    for i in range(len(matrix)):
        if len(matrix) == 0:
            print("{}".format(None))
        for y in matrix[i]:
            if counter != matrix_length - 1:
                print("{:d}".format(y), end=" ")
                counter += 1
            else:
                print("{:d}".format(y))
                counter = 0
    return matrix
