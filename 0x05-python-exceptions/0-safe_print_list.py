def safe_print_list(my_list=[], x=0):
    count = 1
    for i in my_list:
        try:
            print("{}".format(i), end="")
            if count == x:
                break
            count += 1
        except:
            continue
    if x > count:
        count -= 1
    print()
    return count
