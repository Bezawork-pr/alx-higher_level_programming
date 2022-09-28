#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    add = 0
    for i in my_list:
        my_set.add(i)
    for y in my_set:
        add += y
    return add
