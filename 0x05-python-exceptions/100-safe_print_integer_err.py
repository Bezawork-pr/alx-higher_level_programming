#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    checkifInt = isinstance(value, int)
    string = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        sys.stderr.write(string)
    return checkifInt
