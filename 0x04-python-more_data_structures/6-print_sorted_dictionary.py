#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.items(), key=lambda x: str(x[1]))
    for i in sort_dict:
        print(i[0],i[1])
