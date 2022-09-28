#!/usr/bin/python3
def weight_average(my_list=[]):
    mulandadd = 0
    add = 0
    if my_list:
        for i in my_list:
            mulandadd += i[0] * i[1]
            add += i[1]
        return mulandadd/add
    return 0
