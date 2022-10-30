#!/usr/bin/python3
"""
class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
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
        x = self.x
        y = self.y
        while y != 0:
            print()
            y -= 1
        while height != 0:
            width = self.width
            x = self.x
            while x != 0:
                print(" ", end="")
                x -= 1
            while width != 0:
                print("#", end="")
                width -= 1
            print()
            height -= 1

    def __str__(self):
        """Override the str method with this customized method"""
        my_string = "[" + type(self).__name__ + "] (" + str(self.id) + ") "
        my_string += str(self.x) + "/" + str(self.y) + " - "
        my_string += str(self.width) + "/" + str(self.height)
        return my_string

    def update(self, *args, **kwargs):
        """Update attributes with this public method"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, 'id', args[0])
                elif i == 1:
                    setattr(self, 'width', args[1])
                elif i == 2:
                    setattr(self, 'height', args[2])
                elif i == 3:
                    setattr(self, 'x', args[3])
                elif i == 4:
                    setattr(self, 'y', args[4])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, 'id', value)
                elif key == "width":
                    setattr(self, 'width', value)
                elif key == "height":
                    setattr(self, 'height', value)
                elif key == "x":
                    setattr(self, 'x', value)
                elif key == "y":
                    setattr(self, 'y', value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        my_dict = {}
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['id'] = self.id
        my_dict['height'] = self.height
        my_dict['width'] = self.width
        return my_dict
