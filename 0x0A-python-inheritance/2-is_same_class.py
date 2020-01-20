#!/usr/bin/python3
"""
contains is_same_class function
"""


def is_same_class(obj, a_class):
    """ check if obj is an instance of a_class """
    if type(obj) == a_class:
        return True
    else:
        return False
