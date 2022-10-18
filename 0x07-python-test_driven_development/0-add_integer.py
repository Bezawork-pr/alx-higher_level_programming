#!/usr/bin/python3
""" The name of the function is add_integer
This file contains a simple addition function which
takes only ints and floats as parameter if the
parameter provided is float function convert it to int
and returns sum. In other cases raises TypeError"""


def add_integer(a, b=98):
    """Return the sum of two ints.
            Parameter a: int
            Parameter b: int"""
    if isinstance(a, (int, float)) is False or type(a) is bool:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False or type(b) is bool:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
