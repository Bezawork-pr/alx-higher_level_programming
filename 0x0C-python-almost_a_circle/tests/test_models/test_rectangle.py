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
        b3 = Rectangle(3, 2)
        self.assertEqual(b3.width, 3)
        self.assertEqual(b3.height, 2)
        self.assertEqual(b3.x, 0)
        self.assertEqual(b3.y, 0)
        b4 = Rectangle(2, 4, 6)
        self.assertEqual(b4.width, 2)
        self.assertEqual(b4.height, 4)
        self.assertEqual(b4.x, 6)
        self.assertEqual(b4.y, 0)
        b5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(b5.width, 1)
        self.assertEqual(b5.height, 2)
        self.assertEqual(b5.x, 3)
        self.assertEqual(b5.y, 4)
        self.assertEqual(b5.id, 5)

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
        with self.assertRaises(ValueError):
            b1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            b1 = Rectangle(1, 0)

    def test_is_sub_cls(self):
        """Test if Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_str_(self):
        """Test magic function str"""
        b1 = Rectangle(4, 5, 6, 7, 7)
        self.assertEqual(str(b1), "[Rectangle] (7) 6/7 - 4/5")

    def test_to_dictionary(self):
        """Test to_dictionary function"""
        b1 = Rectangle(4, 5, 6, 7, 7)
        my_dict = {'x': 6, 'y': 7, 'id': 7, 'height': 5, 'width': 4}
        self.assertEqual(b1.to_dictionary(), my_dict)

    def test_all_other_funcs(self):
        """Test other cases"""
        r1 = Rectangle(3, 5, 1, 4, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (5) 1/4 - 3/5')


if __name__ == "__main___":
    unittest.main()
