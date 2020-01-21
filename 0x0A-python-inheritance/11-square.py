#!/usr/bin/python3
"""
 contains Rectangle subclass of BaseGeometry class
 contains Square subclase of Rectangle subclass
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
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """attributes of a rectangle"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ str representation of the rectangle """
        return "[Rectangle] {}/{}". format(self.__width, self.__height)


class Square(Rectangle):
    """ defining a square """
    def __init__(self, size):
        """ attributes of a square """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """ returns the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ str representation of the square """
        return "[Square] {}/{}". format(self.__size, self.__size)
