#!/usr/bin/python3
"""
 contains class_to_json
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data
     structure for JSON serialization """
    return obj.__dict__
