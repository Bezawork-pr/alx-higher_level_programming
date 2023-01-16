#!/usr/bin/python3
def find_peak(list_of_integers):
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
            if list_of_integers[last_index] >= list_of_integers[last_index - 1]:
                return list_of_integers[last_index]
        else:
            if list_of_integers[i] >= list_of_integers[i - 1] and \
                    list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]

