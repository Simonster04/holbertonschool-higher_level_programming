#!/usr/bin/python3
"""
 contains BaseGeometry class,
 area Public instance method,
 integer_validator Public instance method
"""


class BaseGeometry:
    """ class with area and integer_validation
     public instance methods """
    def area(self):
        """ raises an Exception if it is called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value is int and > than 0 """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
