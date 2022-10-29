#!/usr/bin/python3
"""
class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, *args):
        """instantiate both super class and this class

        Args:
            width(int): Width of Rectangle
            height(int): height of Rectangle
            x(int): coordinate of Rectangle
            y(int): coordinate of Rectangle
            args: if more argument is given

        Raises:
            TypeError: if width, height, x and y are not int
            ValueError: if width and height are not greater than 0
            ValueError: if x is less than 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate of Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate of Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints to STDOUT"""
        width = self.width
        height = self.height
        while height != 0:
            width = self.width
            while width != 0:
                print("#", end="")
                width -= 1
            print()
            height -= 1
