#!/usr/bin/python3
"""
This file contains a function that
returns the dictionary description
"""
import json


def class_to_json(obj):
    """returns description"""
    return json.dumps(obj.__dict__)
