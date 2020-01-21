#!/usr/bin/python3
"""
 contains load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
