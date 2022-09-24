#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    matrix_length = len(matrix)
    if matrix_length > 0:
        for i in range(len(matrix)):
            for y in matrix[i]:
                if counter != matrix_length - 1:
                    print("{:d}".format(y), end=" ")
                    counter += 1
                else:
                    print("{:d}".format(y))
                    counter = 0
    elif matrix_length == 0:
        print()
    return matrix
