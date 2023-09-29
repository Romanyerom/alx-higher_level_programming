#!/usr/bin/python3

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):

    def test_initialization_success(self):

        s1 = Square(5)

        s2 = Square(10)

        self.assertEqual(s1.size, 5)

        self.assertEqual(s2.size, 10)

    def test_initialization_without_arguments(self):

        self.assertRaises(TypeError, Square)

if __name__ == '__main__':

    unittest.main()
