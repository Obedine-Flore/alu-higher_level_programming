#!/usr/bin/python3
"""
Define a square
"""

class Square:
    """Define a square through this class"""

    def _init_(self, size=0):
        """
        initialize Square class
            Args:
                size (int): size of the square
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
