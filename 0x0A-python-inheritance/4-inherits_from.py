#!/usr/bin/python3
"""
 contains inherits_from function
"""


def inherits_from(obj, a_class):
    """ check if obj is sub instance of a_class """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        False
