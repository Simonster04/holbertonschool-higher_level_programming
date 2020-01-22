#!/usr/bin/python3
"""
 contains Student class
"""


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key in attrs:
            try:
                my_dict[key] = self.__dict__[key]
            except:
                pass
        return my_dict
