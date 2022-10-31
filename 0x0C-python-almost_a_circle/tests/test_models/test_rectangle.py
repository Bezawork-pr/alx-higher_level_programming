#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """"Test Rectangle class"""
    def test_normal_cases(self):
        """Test expected usage scenarios"""
        b1 = Rectangle(5, 10, 8, 9)
        self.assertEqual(b1.width, 5)
        self.assertEqual(b1.height, 10)
        self.assertEqual(b1.x, 8)
        self.assertEqual(b1.y, 9)
        self.assertEqual(b1.area(), 50)
        b1 = Rectangle(5, 10, 8, 9)
        b1.update(89, 2, 3, 4)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 9)
        self.assertEqual(b1.id, 89)

    def test_type_error(self):
        """Test TypeErrors"""
        with self.assertRaises(TypeError):
            b1 = Rectangle(5.4, 10, 8, 9)
        with self.assertRaises(TypeError):
            b1 = Rectangle(5, 10.9, 8, 9)
        with self.assertRaises(TypeError):
            b1 = Rectangle(5, 10, 8.4, 9)
        with self.assertRaises(TypeError):
            b1 = Rectangle(5, 10, 8, 9.9)

    def test_value_error(self):
        """Test Value Errors"""
        with self.assertRaises(ValueError):
            b1 = Rectangle(-5, 10, 8, 9)
        with self.assertRaises(ValueError):
            b1 = Rectangle(5, -10, 8, 9)
        with self.assertRaises(ValueError):
            b1 = Rectangle(5, 10, -8, 9)
        with self.assertRaises(ValueError):
            b1 = Rectangle(5, 10, 8, -9)

    def test_is_sub_cls(self):
        """Test if Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)


if __name__ == "__main___":
    unittest.main()
