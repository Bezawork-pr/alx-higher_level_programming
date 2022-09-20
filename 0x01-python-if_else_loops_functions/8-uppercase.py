#!/usr/bin/python3
def uppercase(str):
    toupper = ""
    for n in str:
        if ord(n) < 123 and ord(n) > 96:
            num = ord(n) - 32
            toupper += chr(num)
        elif ord(n) < 96:
            toupper += n
    print("{}".format(toupper))
