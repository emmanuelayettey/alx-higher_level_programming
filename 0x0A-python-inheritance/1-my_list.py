#!/usr/bin/python3
""" a class list, MyList that inherits from the list
"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """function prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
