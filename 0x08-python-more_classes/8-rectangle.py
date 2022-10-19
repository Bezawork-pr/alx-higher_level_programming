#!/usr/bin/python3
"""This file contains a class"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The init method"""
        type(self).number_of_instances += 1
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
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculate area"""
        return self.height * self.width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_1 = rect_1.height * rect_1.width
        area_rect_2 = rect_2.height * rect_2.width
        if area_rect_1 == area_rect_2:
            return rect_1
        elif area_rect_1 > area_rect_2:
            return rect_1
        else:
            return rect_2

    def perimeter(self):
        """Calculate parameter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns string"""
        returnable = ""
        height = self.height
        width = self.width
        print_symbol = type(self).print_symbol
        separator = ", "
        if isinstance(print_symbol, list):
            joined = separator.join(print_symbol)
            print_symbol = "[" + joined + "]"
        if height == 0 or width == 0:
            return returnable
        while height != 0:
            width = self.width
            while width != 0:
                returnable += print_symbol
                width -= 1
            if height != 1:
                returnable += "\n"
            height -= 1
        return returnable

    def __repr__(self):
        """Returns formal string representation"""
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
