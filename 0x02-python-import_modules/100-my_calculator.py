#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    flag = 0
    a = 0
    b = 0
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in sys.argv:
        if flag == 0:
            flag = 1
        elif flag == 1:
            a = int(i)
            astring = i
            flag = 2
        elif flag == 2:
            sign = i
            flag = 3
        elif flag == 3:
            b = int(i)
            bstring = i
            if sign == "+":
                result = a + b
                print("{:s} + {:s} = {:d}".format(astring, bstring, result))
            elif sign == '-':
                result = a - b
                print("{:s} - {:s} = {:d}".format(astring, bstring, result))
            elif sign == '*':
                result = a * b
                print("{:s} * {:s} = {:d}".format(astring, bstring, result))
            elif sign == '/':
                result = a / b
                print("{:s} / {:s} = {:d}".format(astring, bstring, result))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
