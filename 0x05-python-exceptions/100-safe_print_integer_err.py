#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    checkifInt = isinstance(value, int)
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return checkifInt
