#!/usr/bin/python3
"""
This file loads and saves from and to json files
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []
for i in range(len(sys.argv)):
    if i != 0:
        my_list.append(sys.argv[i])
save_to_json_file(my_list, "add_item.json")
