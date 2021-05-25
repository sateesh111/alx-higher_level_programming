#!/usr/bin/python3
"""
This module defines a function that adds two integers
"""


def add_integer(a, b=98):
    """ Returns the sum of a and b as integers if
    they are both integers and an Error if they are not
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
