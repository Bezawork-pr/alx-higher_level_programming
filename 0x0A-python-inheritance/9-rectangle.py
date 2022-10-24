#!/usr/bin/python3
"""
This file contains a class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """init fun"""
        super().__init__
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """magic func str"""
        my_string = type(self).__name__ + " "
        my_string += str(self.__width) + "/" + str(self.__height)
        return my_string
