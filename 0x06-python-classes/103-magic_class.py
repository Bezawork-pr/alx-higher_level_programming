#!/usr/bin/python3
"""Create a class"""


class MagicClass:
    """Create a class based on python bytecode provided"""

    def __init__(self, radius=0):
        """Receive radius as a parameter and set defaut to 0"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """This is a function to calculate the area based on the radius"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Get circumstance based on radius"""
        return (2 * math.pi) * self._MagicClass__radius