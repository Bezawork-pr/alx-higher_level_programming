#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_copy = my_list[:]
        my_copy[idx] = element
        return my_copy
    my_copy = my_list[:]
    return my_copy
