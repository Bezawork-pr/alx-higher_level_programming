#!/usr/bin/python3
"""This file contains one class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """init func"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__height = size
        self.__width = size
        self.area()
        self.__str__()
