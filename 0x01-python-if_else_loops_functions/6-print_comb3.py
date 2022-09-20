#!/usr/bin/python3
for i in range(0, 10):
    for n in range(0, 10):
        if i < n and (str(i) + str(n) != "89"):
            print("{}, ".format(str(i) + str(n)), end="")
        elif i == 8 and n == 9:
            print("{}".format(str(i) + str(n)))
