#!/usr/bin/python3
""" LockedClass.
"""


class LockedClass:
    """
    the function prevents users from instantiating new LockedClass attributes
    for anything anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
