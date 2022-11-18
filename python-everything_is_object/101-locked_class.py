#!/usr/bin/python3
"""
Defines the function of locked class
"""


class lockedClass:
    """
    This class prevents the user from dynamically initiating new attributes
    for any new attribute but attributes called 'first_name'
    """

    _slots_ = ['first_name']
