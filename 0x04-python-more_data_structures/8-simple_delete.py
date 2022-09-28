#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    checkkey = a_dictionary.get(key) if key in a_dictionary else -1
    if checkkey != (-1):
        del a_dictionary[key]
    return a_dictionary
