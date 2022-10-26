#!/usr/bin/python3
"""
This file contains a function that appends to file
"""


def append_after(filename="", search_string="", new_string=""):
    """Append after search"""
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
    with open(filename, "w", encoding="utf-8") as clear:
        pass
    with open(filename, "w", encoding="utf-8") as modify:
        for line in read:
            modify.write(line)
            for word in line.split():
                my_line = " ".join(line.split())
                if my_line == search_string:
                    modify.write(new_string)
                    break
                check_word = ""
                for letter in word:
                    check_word += letter
                    if check_word == search_string:
                        modify.write(new_string)
