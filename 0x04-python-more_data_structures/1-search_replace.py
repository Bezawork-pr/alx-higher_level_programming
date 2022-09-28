#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    index = new_list.index(search) if search in new_list else -1
    if (index != (-1)):
        new_list[index] = replace
        return new_list
    else:
        return my_list
