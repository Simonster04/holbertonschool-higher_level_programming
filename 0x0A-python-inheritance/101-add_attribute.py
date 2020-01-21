#!/usr/bin/python3
"""
 contains add_attribute function
"""


def add_attribute(instance, attribute, value):
    """ Adds a new attribute """
    if hasattr(instance, "__dict__"):
        setattr(instance, attribute, value)
    else:
        raise TypeError("can't add new attribute")
