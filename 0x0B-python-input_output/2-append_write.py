#!/usr/bin/python3
""" this module contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ the function that appends to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
