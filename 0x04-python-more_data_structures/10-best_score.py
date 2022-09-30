#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        maxvalue = max(values)
        getmaxvalkey = values.index(maxvalue)
        return keys[getmaxvalkey]
