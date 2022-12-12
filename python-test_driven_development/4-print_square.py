#!/usr/bin/python3
"""
This function prints a square with the # character
"""


def print_square(size):
    '''prints a square'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    print("{}\n".format("#" * size) * size, end="")
