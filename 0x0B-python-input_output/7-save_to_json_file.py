#!/usr/bin/python3
"""
 contains save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using JSON rep """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
