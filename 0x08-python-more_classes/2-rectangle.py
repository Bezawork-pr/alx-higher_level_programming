#!/usr/bin/python3
"""This file contains a class"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """The init method"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculate area"""
        return self.height * self.width

    def perimeter(self):
        """Calculate parameter"""
        return 2 * (self.height + self.width)
