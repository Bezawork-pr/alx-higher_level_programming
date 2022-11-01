#!/usr/bin/python3
"""
This file contains class Square
class square is a subclass of Rectangle
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

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override magic method str"""
        sq_string = "[" + type(self).__name__ + "] " + "("
        sq_string += str(self.id) + ") " + str(self.x)
        sq_string += "/" + str(self.y) + " - "
        sq_string += str(self.width)
        return sq_string

    def update(self, *args, **kwargs):
        """update attributes using magic vairables args and kwargs"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, 'id', args[0])
                elif i == 1:
                    setattr(self, 'size', args[1])
                elif i == 2:
                    setattr(self, 'x', args[2])
                elif i == 3:
                    setattr(self, 'y', args[3])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, 'id', value)
                elif key == "size":
                    setattr(self, 'size', value)
                elif key == "x":
                    setattr(self, 'x', value)
                elif key == "y":
                    setattr(self, 'y', value)

    def to_dictionary(self):
        """Return dictionary representation of square"""
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['x'] = self.x
        square_dict['size'] = self.size
        square_dict['y'] = self.y
        return square_dict
