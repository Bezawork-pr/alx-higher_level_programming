#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, searchvalue in a_dictionary.items():
            if searchvalue == value:
                del a_dictionary[key]
                break
    return a_dictionary
