#!/usr/bin/python3
"""
This file contains one function
"""


def write_file(filename="", text=""):
    """This function writes to files and return length of written text"""
    with open(filename, "w", encoding="utf-8") as f:
        file_write = f.write(text)
    return len(text)
