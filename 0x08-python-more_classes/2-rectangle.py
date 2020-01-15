#!/usr/bin/python3
"""

 This module contains the Rectangle class

"""


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """ initialization """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter for private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for private instance attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private instance attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)
