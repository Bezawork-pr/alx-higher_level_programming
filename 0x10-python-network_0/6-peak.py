#!/usr/bin/python3
""" This file contains a function that returns a peak from an array
I have used a while loop to get the peak"""


def find_peak(list_of_integers):
    """function find_peak: finds a peak in an array and returns it"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return
    length = len(list_of_integers)
    last_index = len(list_of_integers) - 1
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[1] <= list_of_integers[0]:
                return list_of_integers[0]
        elif i == last_index:
            if list_of_integers[last_index] \
                    >= list_of_integers[last_index - 1]:
                return list_of_integers[last_index]
        else:
            if list_of_integers[i] >= list_of_integers[i - 1] and \
                    list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]
