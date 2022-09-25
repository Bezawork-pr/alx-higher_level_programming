#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    count = 0
    tuple_c, tuple_temp, tuple_temp2, tuple_temp3 = (), (), (), ()
    tuple_temp4, temp_result = (), ()
    while (len(tuple_a) < 2) and (len(tuple_temp2) != 2):
        add_zero = (0,)
        if len(tuple_a) == 0 and len(tuple_temp) == 0:
            tuple_temp = tuple_temp + add_zero
        elif len(tuple_a) == 1 or len(tuple_temp) == 1:
            tuple_temp2 = tuple_a + tuple_temp + add_zero
    while (len(tuple_b) < 2) and (len(tuple_temp4) != 2):
        add_zero = (0,)
        if len(tuple_b) == 0 and len(tuple_temp3) == 0:
            tuple_temp3 = tuple_temp3 + add_zero
        elif len(tuple_b) == 1 or len(tuple_temp3) == 1:
            tuple_temp4 = tuple_b + tuple_temp3 + add_zero
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        for i, e in zip(tuple_a[0:2], tuple_b[0:2]):
            addition = i + e
            new_element = (addition,)
            tuple_c = tuple_c + new_element
            del new_element
    elif len(tuple_a) < 2 and len(tuple_b) > 1:
        for i, e in zip(tuple_temp2, tuple_b[0:2]):
            addition = i + e
            new_element = (addition,)
            tuple_c = tuple_c + new_element
            del new_element
    elif len(tuple_a) > 1 and len(tuple_b) < 2:
        for i, e in zip(tuple_a[0:2], tuple_temp4):
            addition = i + e
            new_element = (addition,)
            tuple_c = tuple_c + new_element
            del new_element
    else:
        for i, e in zip(tuple_temp2, tuple_temp4):
            addition = i + e
            newelement = (addition,)
            tuple_c = tuple_c + new_element
            del new_element
    return tuple_c
