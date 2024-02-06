#!/usr/bin/python3
""" a program that defines the class Student
"""


class Student:
    """ the function class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ the process that returns directory description """
        return self.__dict__.copy()