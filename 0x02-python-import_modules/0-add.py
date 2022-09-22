#!/usr/bin/python3
def add():
    import add_0 as addition
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, addition.add(1, 2)))
add()
