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
        with open(filename, mode="w") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                myFile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        aux = []
        try:
            with open(filename, mode='r') as myFile:
                aux = cls.from_json_string(myFile.read())
                return [cls.create(**my_dict) for my_dict in aux]
        except:
            pass
        return aux
