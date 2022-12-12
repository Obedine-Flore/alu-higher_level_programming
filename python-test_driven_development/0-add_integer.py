#!/usr/bin/python3
"""
This script does an addition of two integers
"""


def add_integer(a, b=98):
    '''This function returns the sum of two numbers'''

    a = int(a)
    b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
