#!/usr/bin/python3
"""
 This module contains say_my_name function
 It receives first name and last name
 and returns My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
     This funtion prints 2 args received as first name and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
