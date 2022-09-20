#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stringnum = repr(number)
if number < 0:
    lastdigit = "-" + stringnum[-1]
elif number >= 0:
    lastdigit = stringnum[-1]
strings = "Last digit of"
gre = "and is greater than 5"
les = "and is less than 6 and not 0"
if int(lastdigit) > 5:
    print("{} {:d} is {:d} {}".format(strings, number, int(lastdigit), gre))
elif int(lastdigit) < 6 and int(lastdigit) > 0:
    print("{} {:d} is {:d} {}".format(strings, number, int(lastdigit), les))
elif int(lastdigit) < 0:
    print("{} {:d} is {:d} {}".format(strings, number, int(lastdigit), les))
elif int(lastdigit) == 0:
    print("{} {:d} is {:d} and is 0".format(strings, number, int(lastdigit)))
