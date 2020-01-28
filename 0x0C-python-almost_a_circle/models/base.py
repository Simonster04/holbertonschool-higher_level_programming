#!/usr/bin/python3
"""
contains Base class
"""
import json


class Base:
    """ defines a base class for rest of project """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        return json.dumps(list_dictionaries)
