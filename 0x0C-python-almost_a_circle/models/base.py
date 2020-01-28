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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as myFile:
            if list_objs is None:
                myFile.write("[]")
            list_dict = [obj.to_dictionary() for obj in list_objs]
            myFile.write(cls.to_json_string(list_dict))
