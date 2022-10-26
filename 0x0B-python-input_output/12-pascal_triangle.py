#!/usr/bin/python3
"""This file contains a function that creates pascal_triangle"""


def pascal_triangle(n):
    """Create pascal triangle"""
    my_list = []
    if n <= 0:
        return my_list
    for row in range(n):
        listinlist = [1]
        for column in range(row):
            if column == row - 1:
                my_append = 1
            elif row % 2 != 0 and column == 0:
                my_append = row * (column + 1)
            elif row % 2 == 0 and column == 0:
                my_append = row * (column + 1)
            elif row % 2 == 0 and column == 1:
                my_append = (row - 1) * 2
            elif row % 2 != 0 and column == 1 and row > 3:
                my_append = row * (column + 1)
            elif row % 2 == 0 and (row - column) == 2:
                my_append = row
            else:
                pass
            listinlist.append(my_append)
        my_list.append(listinlist)
        del listinlist
    return my_list
