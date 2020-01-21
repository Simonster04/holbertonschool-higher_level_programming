#!/usr/bin/python3
"""
 script that adds all arguments to a Python list
 and then save them to a file
"""


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

from sys import argv

try:
    jsonlist = load_from_json_file("add_item.json")
except:
    jsonlist = []

for item in argv[1:]:
    jsonlist.append(item)

save_to_json_file(jsonlist, "add_item.json")
