#!/usr/bin/python3
""" Create a class"""


class Square:
    """Create a class Square with private attribute that is size
    and raise Error type TypeError when value is not int
    and ValueError when int is less than 0"""
    def __init__(self, size=0):
        self.__size = size
        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
