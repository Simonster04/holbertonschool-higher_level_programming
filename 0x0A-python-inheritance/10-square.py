#!/usr/bin/python3
"""
 contains Rectangle subclass of BaseGeometry class
 contains Square subclase of Rectangle subclass
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """  """
        return self.__width * self.__height

    def __str__(self):
        """  """
        return "[Rectangle] {}/{}". format(self.__width, self.__height)


class Square(Rectangle):
    """ defining a square """
    def __init__(self, size):
        """ attributes of a square """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """  """
        return self.__size * self.__size
