#!/usr/bin/python3
"""
This file contains one function
"""
import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        read = json.load(f)
    return read
