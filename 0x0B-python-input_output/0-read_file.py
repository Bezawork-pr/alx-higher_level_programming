#!/usr/bin/python3
"""
This file cointains function read_file that reads from file
"""


def read_file(filename=""):
    """read_file func read from file and prints to STDOUT"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print("{}".format(read_data), end="")
