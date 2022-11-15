#!/usr/bin/python3
"""this script returns the list of available attributes and methods of an object"""


def lookup(obj):
    """returns available attributes and methods of an object as a list"""
    return dir(obj)
