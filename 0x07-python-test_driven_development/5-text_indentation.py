#!/usr/bin/python3
"""This module contain function text_indentation
Returns


"""


def text_indentation(text):
    """Return None

    prints"""
    if (isinstance(text, str)) is False:
        raise TypeError("text must be a string")
    to_be_printed = ""
    for char in text:
        if char == ".":
            print("{}".format(to_be_printed))
            print()
            del to_be_printed
            to_be_printed = ""
        elif char == "?":
            print("{}".format(to_be_printed))
            print()
            del to_be_printed
            to_be_printed = ""
        elif char == ":":
            print("{}".format(to_be_printed))
            print()
            del to_be_printed
            to_be_printed = ""
        else:
            if char == "\\":
                pass
            else:
                to_be_printed += char
