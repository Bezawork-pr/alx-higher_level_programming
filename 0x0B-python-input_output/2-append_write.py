#!/usr/bin/python3
"""
This file contains one function
"""


def append_write(filename="", text=""):
    """append_write appends text to file"""
    with open(filename, "a", encoding="utf-8") as f:
        file_append = f.write(text)
    return file_append
