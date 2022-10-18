#!/usr/bin/python3
"""This file contains one function that returns
stringliteral plus parameter given.
Isinstance built in function checks
if parameter provided is str
otherwise throws a TypeError"""


def say_my_name(first_name, last_name=""):
    """Return: string literal plus parameter passed

    parameter: first_name and last_name"""
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
