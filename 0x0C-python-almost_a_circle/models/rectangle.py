#!/usr/bin/python3
"""
class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiate super and this class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)



        @property
        def width(self):
            """Width getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """Width setter"""
            if isinstance(value, int) is False:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Height getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """Height setter"""
            if isinstance(value, int) is False: 
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """X getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """X setter """
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Y getter"""
            return self.__y

        @y.setter
        def y(self, value):
            """Y setter"""
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
