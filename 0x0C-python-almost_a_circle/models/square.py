#!/usr/bin/python3
"""
This file contains a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate both super class and this class

        Args:
            size(int): size of square
            x: x coordinate of square
            y: y coordinate of square
            id: id of square

        Raises:
            TypeError: if size is not int
            TypeError: if x or y is not int
            ValueError: if size is less than or equal to zero
            ValueError: if x or y is less than zero
        """
        super().__init__(size, size, x, y, id)
        self.area()
        self.__str__()
