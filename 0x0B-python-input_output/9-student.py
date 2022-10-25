#!/usr/bin/python3
"""
This file contains class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        """Public method returning
        that retrieves a dictionary representation
        """
        return self.__dict__
