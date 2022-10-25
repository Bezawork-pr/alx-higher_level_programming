#!/usr/bin/python3
"""
This file contains one function
"""
import json


def save_to_json_file(my_obj, filename):
    """Function saves to json file"""
    with open(filename, "a", encoding="utf-8") as f:
        write_tofile = json.dump(my_obj, f)
