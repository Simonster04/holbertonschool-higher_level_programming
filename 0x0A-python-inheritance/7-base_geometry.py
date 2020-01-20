#!/usr/bin/python3
"""
 contains BaseGeometry class,
 area Public instance method,
 integer_validator Public instance method
"""


class BaseGeometry:
    """"""
    def __init__(self):
        """"""

    def area(self):
        """"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
