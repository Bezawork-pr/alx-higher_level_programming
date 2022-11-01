#!/usr/bin/python3
"""
Unittest for Square class
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """"Test Square class"""
    def test_normal_cases(self):
        """Test expected usage scenarios"""
        b1 = Square(5, 3, 1)
        self.assertEqual(b1.size, 5)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 1)
        self.assertEqual(b1.area(), 25)
        b1.update(89, 2, 3, 4)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)
        self.assertEqual(b1.id, 89)
        b2 = Square(1)
        self.assertEqual(b2.size, 1)
        self.assertEqual(b2.x, 0)
        self.assertEqual(b2.y, 0)
        b3 = Square(1, 2)
        self.assertEqual(b3.size, 1)
        self.assertEqual(b3.x, 2)
        self.assertEqual(b3.y, 0)
        b5 = Square(1, 2, 3, 4)
        self.assertEqual(b5.size, 1)
        self.assertEqual(b5.x, 2)
        self.assertEqual(b5.y, 3)
        self.assertEqual(b5.id, 4)

    def test_errors(self):
        """Test TypeErrors and ValueErrors"""
        with self.assertRaises(TypeError):
            s1 = Square("1")
        with self.assertRaises(TypeError):
            s3 = Square(1, "2")
        with self.assertRaises(TypeError):
            s4 = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            s5 = Square(-1)
        with self.assertRaises(ValueError):
            s6 = Square(1, -2)
        with self.assertRaises(ValueError):
            s8 = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s9 = Square(0)

    def test_str(self):
        """Test magic function str"""
        b5 = Square(1, 2, 3, 4)
        self.assertEqual(str(b5), "[Square] (4) 2/3 - 1")

    def test_is_sub_cls(self):
        """Test if Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Square, Rectangle), True)


if __name__ == "__main___":
    unittest.main()
