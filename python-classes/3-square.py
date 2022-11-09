#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square
    """Write a class Square that defines a square"""

    def _init_(self, size=0):
        if type(size) is not int:
            raise TypeError("sze must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        return self._size**2
