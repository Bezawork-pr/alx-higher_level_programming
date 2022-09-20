#!/usr/bin/python3
def print_last_digit(number):
    stringnum = repr(number)
    lastdigit = stringnum[-1]
    print("{:d}".format(int(lastdigit)), end="")
    return int(lastdigit)
