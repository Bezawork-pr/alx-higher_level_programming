#!/usr/bin/python3
""" Create a class"""


class Square:
    """Create a class Square with private attribute that is size
    and raise Error type TypeError when value is not int
    and ValueError when int is less than 0.
    public instance method area returns area of square"""
    def __init__(self, size=0):
        """initialize Square"""
        if isinstance(size, (float, int)) is False:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """"Return area"""
        return (self.__size) ** 2

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

    def __eq__(self, other):
        """ check if equal"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return currentarea == otherarea

    def __ne__(self, other):
        """Checks if not equal"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return not currentarea == otherarea

    def __lt__(self, other):
        """Checks if first element is less than other"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return currentarea < otherarea

    def __gt__(self, other):
        """Checks if first element is greater than other"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return currentarea > otherarea

    def __ge__(self, other):
        """Checks if first element is greater or equal to than other"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return (currentarea > otherarea) or (currentarea == otherarea)

    def __le__(self, other):
        """Checks if first element is less than or equal to than other"""
        size = self.__size
        currentarea = self.area()
        otherarea = other.area()
        return (currentarea < otherarea) or (currentarea == otherarea)
