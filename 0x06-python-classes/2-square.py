#!/usr/bin/python3
""" a class square that defines a square"""


class Square:
    """ a class square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int):the size of the square
        """
        if type(size) is not int:
            raise TypeError('the size must be an integer')
        elif size < 0:
            raise ValueError('the size must be >= 0')
        else:
            self.__size = size  #: size of the square
