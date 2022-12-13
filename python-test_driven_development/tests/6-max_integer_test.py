#!/usr/bin/python3
"""
This function performs a unit test for the max. integer
"""

import unittest
max_integer = _import_('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        '''case of an ordered list'''
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_unordered_list(self):
        '''case of an unordered list'''
        self.assertEqual(max_integer([6, 2, 8, 4]), 8)

    def test_single_element(self):
        '''case of a single element'''
        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        '''case with floating point numbers'''
        self.assertEqual(max_integer([1.0, 2.2, 3.5, 4.8]), 4.8)

    def test_string(self):
        '''case with a string'''
        self.assertEqual(max_integer(["Baby"]), 'y')

    def test_empty_string(self):
        '''case of an empty list'''
        self.assertEqual(max_integer(""), None)

    def test_max_at_begining(self):
        self.asserEqual(max_integer([8, 7, 6, 4]), 8)
        ''' case with max at the begining'''

    def test_max_at_end(self):
        ''' case with max at the end'''
        self.assertEqual([2, 5, 4, 7]), 7)

    def test_integers(self):
        '''case with negative numbers'''
        self.assertEqual([-1, 4, 1, 3]), 4)

    def test_negative_integers(self):
        '''case with negative integers only'''
        self.assertEqual([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        '''case with an empty list'''
        self.assertEqual([], None)
