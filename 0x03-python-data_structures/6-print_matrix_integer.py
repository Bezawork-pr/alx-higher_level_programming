#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    if (len(matrix[0]) == 0):
        matrix_length = 0
        print()
        return matrix
    else:
        matrix_length = len(matrix)
    for i in range(matrix_length):
        for y in matrix[i]:
            if counter != matrix_length - 1:
                print("{:d} ".format(y), end="")
                counter += 1
            else:
                print("{:d}".format(y))
                counter = 0
    return matrix
