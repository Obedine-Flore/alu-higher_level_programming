#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered_list(self):
        """case of an ordered list"""
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_unordered_list(self):
        """case of an unordered list"""
        self.assertEqual(max_integer([5, 7, 1, 6]), 7)

    def test_empty_list(self):
        """case of an empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_max_at_beginning(self):
        """case with max at the begining"""
        self.assertEqual(max_integer([8, 6, 4, 2]), 8)

    def test_one_element(self):
        """case with a single element"""
        self.assertEqual(max_integer([2]), 2)

    def test_floats(self):
        """case with floats"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0, -4.0, 5.0]), 5.0)

    def test_ints_and_floats(self):
        """case with integers and floats"""
        self.assertEqual(max_integer([1.0, 3.5, -2, 4, 5.5]), 5.5)

    def test_string(self):
        """case of a string"""
        self.assertEqual(max_integer("School"), 'o')

    def test_list_of_strings(self):
        """case with a list of strings"""
        self.assertEqual(max_integer(["I", "Am", "Happy"]), "I")

    def test_empty_string(self):
        """case of an empty string"""
        self.assertEqual(max_integer(""), None)
    
if __name__ == '__main__':
    unittest.main()
