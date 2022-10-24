#!/usr/bin/python3
"""This file contains a class"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, num):
        """init method"""
        super().__init__
        self.__num = num

    def __eq__(self, int):
        """checks if equal but reversed"""
        return self.__num != int

    def __ne__(self, int):
        """check if not equal but reversed"""
        return self.__num == int
