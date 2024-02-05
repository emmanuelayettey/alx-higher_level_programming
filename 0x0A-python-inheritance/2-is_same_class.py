#!/usr/bin/python3
"""the funciton returns True if the object is exactly an instance of the specified
class; otherwise False.
"""


def is_same_class(obj, a_class):
    """ the function returns True if the object is exactly an instance"""
    return True if type(obj) == a_class else False
