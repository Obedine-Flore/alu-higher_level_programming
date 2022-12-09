#!/usr/bin/python3
"""
This function performs a unit test for the max. integer
"""

import unittest
max_integer = _import_('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)
        ''' case of an ordered list'''

    def test_unordered_list(self):
        self.assertEqual(max_integer([6, 2, 8, 4]), 8)
        ''' case of an unordered list '''

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)
        ''' case of a single element'''

    def test_floats(self):
        self.assertEqual(max_integer([1.0, 2.2, 3.5, 4.8]), 4.8)
        ''' case with decimal numbers'''

    def test_string(self):
        self.assertEqual(max_integer(["Baby"]), 'y')
        ''' case with a string'''

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)
        ''' case with an empty list'''
