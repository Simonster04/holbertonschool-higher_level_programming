#!/usr/bin/python3
"""

 This module contains the Rectangle class

"""


class Rectangle:
    """ defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        """ Returns like a string """
        return ((self.print_symbol * (self.__width) + '\n') * self.__height).strip("\n")

    def __repr__(self):
        """ Returns the object representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when you delete the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
