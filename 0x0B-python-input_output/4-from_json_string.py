#!/usr/bin/python3
"""
This file contains one function
"""
import json


def from_json_string(my_str):
    """Returns object"""
    get_Json_obj = json.loads(my_str)
    return get_Json_obj
