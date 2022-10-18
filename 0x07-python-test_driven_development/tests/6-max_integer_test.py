#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class to test provided fun"""

    def test_empty_list(self):
        """Test when lisy is empty"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_only_one_element(self):
        """Test result when list contains onlye one element"""
        my_list = [9]
        self.assertEqual(max_integer(my_list), 9)

    def test_find_max_positive(self):
        """Checks Max when list elements are positive"""
        my_list = [9, 7, 4]
        self.assertEqual(max_integer(my_list), 9)

    def test_find_max_negative(self):
        """Checks Max when list elements are negative"""
        my_list = [-9, -7, -4]
        self.assertEqual(max_integer(my_list), -4)

    def test_file_doc_string_check(self):
        """Checks if there is file doc_string"""
        file_doc_string = __import__('6-max_integer').__doc__
        self.assertTrue(len(file_doc_string) > 1)

    def test_function_doc_string_check(self):
        """Checks if there is function docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_max_at_beg(self):
        """Checks if function works well when max at beginning"""
        my_list = [9, 7, 4]
        self.assertEqual(max_integer(my_list), 9)

    def test_max_in_middle(self):
        """Checks if function works well when max in the middle"""
        my_list = [4, 9, 7]
        self.assertEqual(max_integer(my_list), 9)

    def test_max_at_end(self):
        """Checks if function works well when max at the end"""
        my_list = [4, 7, 9]
        self.assertEqual(max_integer(my_list), 9)

    def test_string(self):
        """checks if TypeError is raised when string is given as parameter"""
        my_list = [4, 7, 9, "end"]
        with self.assertRaises(TypeError):
            max_integer(my_list)


if __name__ == "__main__":
    unittest.main()
