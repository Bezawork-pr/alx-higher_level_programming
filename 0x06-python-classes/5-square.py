#!/usr/bin/python3
""" Create a class"""


class Square:
    """Create a class Square with private attribute that is size
    and raise Error type TypeError when value is not int
    and ValueError when int is less than 0.
    public instance method area returns area of square"""
    def __init__(self, size=0):
        """initialize Square"""
        self.size = size

    def area(self):
        """"Return area"""
        return (self.__size) ** 2

    def my_print(self):
        """Draw area in # with print"""
        if self.__size == 0:
            print()
            return
        height = self.__size
        width = self.__size
        while width != 0:
            height = self.__size
            while height != 0:
                print("#", end="")
                height -= 1
            width -= 1
            print()

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
