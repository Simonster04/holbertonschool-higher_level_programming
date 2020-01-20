#!/usr/bin/python3
"""
 This module contains the Rectangle class
"""


class Rectangle:
    """ defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializing """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Returns the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        """ Returns like a string """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """ Returns the object representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when you delete the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """" compares two rectangles """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with wid == hei == siz """
        return cls(size, size)
