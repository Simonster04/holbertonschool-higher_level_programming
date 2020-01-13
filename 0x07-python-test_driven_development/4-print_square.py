#!/usr/bin/python3
"""

 This module contains print_square function

"""


def print_square(size):
    """ This function prints a square with the character '#' """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
