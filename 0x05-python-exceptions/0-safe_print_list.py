#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
    print()
    if x > i + 1:
        return i
    else:
        return i + 1