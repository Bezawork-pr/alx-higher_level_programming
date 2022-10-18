#!/usr/bin/python3
"""Module contains one function

Takes parameter list of int or float and div int and float
Return new_matrix that is divide
and all the others return a type error"""


def matrix_divided(matrix, div):
    """Return new matrix

    Parameter list and int or float
    """
    mxstr = "matrix must be a matrix (list of lists) of integers/floats"
    if (isinstance(matrix, list) is False):
        raise TypeError(mxstr)
    if (isinstance(div, (int, float)) is False) or (type(div) is bool):
        raise TypeError("div must be a number")

    check_if_matrix = all(isinstance(elem, list) for elem in matrix)
    if check_if_matrix is False:
        raise TypeError(mxstr)
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for element in range(len(matrix[row])):
            if isinstance(matrix[row][element], (int, float)) is False:
                raise TypeError(mxstr)
            else:
                new_element = round(matrix[row][element] / div, 2)
                new_matrix[-1].append(new_element)
    return new_matrix
