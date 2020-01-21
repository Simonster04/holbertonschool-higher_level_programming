#!/usr/bin/python3
"""
 contains Rectangle subclass of BaseGeometry class
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


class Rectangle(BaseGeometry):
    """ A rectangle """
    def __init__(self, width, height):
        """ inicialization of a rectangle """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
