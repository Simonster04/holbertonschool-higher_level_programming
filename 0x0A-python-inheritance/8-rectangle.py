#!/usr/bin/python3
"""
 contains Rectangle subclass of BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle """
    def __init__(self, width, height):
        """ inicialization of a rectangle """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
