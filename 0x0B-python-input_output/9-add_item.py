#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file:
"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


arguments = []
arguments = sys.argv
del arguments[0]


filename = "add_item.json"
try:
    my_dict = load_from_json_file(filename)
except:
    my_dict = []
save_to_json_file(my_dict + arguments, filename)
