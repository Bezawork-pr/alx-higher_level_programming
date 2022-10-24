#!/usr/bin/python3
"""
This file contains class
"""


class MyList(list):
    """This class inherits from list
    Function print_sorted: sorts and prints list"""

    def __init__(self):
        """initiates class"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        my_list = sorted(self)
        print(my_list)
