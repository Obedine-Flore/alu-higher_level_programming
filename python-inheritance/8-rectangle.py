#!/usr/bin/python3
'''Class rectangle that inherits from BaseGeometry'''


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class inherits BaseGeommetry'''

    def _init_(self, width, height):
        '''A function that created a rectangle'''
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self._height = height
