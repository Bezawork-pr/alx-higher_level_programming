#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    count = 0
    if number == 0:
        argument = "arguments."
    elif number == 1:
        argument = "argument:"
    elif number > 1:
        argument = "arguments:"
    print(f"{number} {argument}")
    for i in sys.argv:
        if count != 0:
            print(f"{count}: {i}")
        count += 1
