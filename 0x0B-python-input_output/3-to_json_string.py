#!/usr/bin/python3
"""
This file contains one function
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of object"""
    with open("my_fileon.txt", "w", encoding="utf-8") as f:
        get_Json_string = json.dumps(my_obj, indent=None)
    return get_Json_string
