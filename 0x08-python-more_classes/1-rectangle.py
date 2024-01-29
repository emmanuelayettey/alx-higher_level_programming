#!/usr/bin/python3
""" an empty class rectangle that defines a rectangle
"""


class Rectangle:
    """ a rectangle class"""
    def __init__(self, width=0, height=0):
        """ Instanlling  optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError(" the width must be an integer")
        if value < 0:
            raise ValueError(" the width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ the height setter
        """
        if type(value) is not int:
            raise TypeError(" the height must be an integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value
