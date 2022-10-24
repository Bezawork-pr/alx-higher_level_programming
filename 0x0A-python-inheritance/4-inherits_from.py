#!/usr/bin/python3
"""This file cointains one function"""


def inherits_from(obj, a_class):
    """Checks if object is instance of class or other class derived from it
    and subclass checks if subclass of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
