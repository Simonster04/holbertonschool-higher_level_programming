#!/usr/bin/python3
"""
 contains is_kind_of_class function
"""

def is_kind_of_class(obj, a_class):
    """ check if obj is instance of a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
