#!/usr/bin/python3
"""This file contains one function
This function prints area using hash
It takes parameter size
function checks value is greater than 0
and checks if size is not int and throws error message"""


def print_square(size):
    """Function returns None

    Parameter size a positive int """
    if isinstance(size, int) is False or type(size) is bool:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    height = size
    width = size
    while height != 0:
        width = size
        while width != 0:
            print("#", end="")
            width -= 1
        print()
        height -= 1
