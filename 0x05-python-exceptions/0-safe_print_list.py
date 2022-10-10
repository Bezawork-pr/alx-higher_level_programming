def safe_print_list(my_list=[], x=0):
    count = 1
    try:
        for i in my_list:
            print("{}".format(i), end="")
            if count == x:
                break
            count += 1
    except IndexError:
        raise IndexError
    if x > count:
        count -= 1
    print()
    return count
