#!/usr/bin/python3
"""
Unittest for Bass class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """"Test Base class"""
    def test_normal_cases(self):
        """Test expected usage scenarios"""
        b1 = Base()
        b2 = Base()
        b3 = Base(19)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 19)

    def test_negatives_and_float(self):
        """Test float and negative"""
        b1 = Base(-3)
        b2 = Base(9.9)
        self.assertEqual(b1.id, -3)
        self.assertEqual(b2.id, 9.9)

    def test_other_types(self):
        """Test other non numerial types"""
        b1 = Base("one")
        b2 = Base({"number": 1})
        b3 = Base([1, 2])
        b4 = Base((1, 2))
        self.assertEqual(b1.id, "one")
        self.assertEqual(b2.id, {"number": 1})
        self.assertEqual(b3.id, [1, 2])
        self.assertEqual(b4.id, (1, 2))

    def test_same_id(self):
        """Same id cases"""
        b1 = Base(2)
        b2 = Base(2)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 2)


if __name__ == "__main___":
    unittest.main()
