#!/usr/bin/python3
"""
class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiate super and this class"""
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Width getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """Width setter"""
            self.__width = value

        @property
        def height(self):
            """Height getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """Height setter"""
            self.__height = value

        @property
        def x(self):
            """X getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """X setter """
            self.__x = value

        @property
        def y(self):
            """Y getter"""
            return self.__y

        @y.setter
        def y(self, value):
            """Y setter"""
            self.__y = value
