#!/usr/bin/python3
""" Create a class"""


class Square:
    """Create a class Square with private attribute that is size
    and attribute position that is a tuple
    and raise Error type TypeError when value is not int
    and ValueError when int is less than 0.
    public instance method area returns area of square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize Square"""
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        self.__position = value

    def area(self):
        """"Return area"""
        return (self.__size) ** 2

    def my_print(self):
        """Draw area in # with print"""
        if self.__size == 0:
            print()
            return
        position = self.__position[0]
        height = self.__size
        width = self.__size
        while width != 0:
            height = self.__size
            position = self.__position[0]
            while position != 0:
                print(" ", end="")
                position -= 1
            while height != 0:
                print("#", end="")
                height -= 1
            width -= 1
            print()
