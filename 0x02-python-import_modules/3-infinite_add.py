#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sumit = 0
    flag = 0
    for i in sys.argv:
        if flag == 0:
            flag = 1
        else:
            sumit += int(i)
    print(f"{sumit}")
