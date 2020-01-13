#!/usr/bin/python3
"""
 This module contains the add_integer function
 Receives int or float
 Returns the addition of two variables as int
"""


def add_integer(a, b=98):
    """
     This function adds 2 integers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int) or not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
