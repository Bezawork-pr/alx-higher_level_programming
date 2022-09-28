#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    checkkey = a_dictionary.get(key) if key in a_dictionary else -1
    if checkkey == 1:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
