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

    def test_is_sub_cls(self):
        """Test if Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Square, Rectangle), True)


if __name__ == "__main___":
    unittest.main()
