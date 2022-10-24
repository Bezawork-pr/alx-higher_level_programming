#!/usr/bin/python3
"""
This file contains a class
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def __init__(self):
        pass

    def area(self):
        """area func"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        return value


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
