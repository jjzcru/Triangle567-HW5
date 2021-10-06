# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # Test valid inputs in the function
    def testInputInTriangle(self):
        self.assertEqual(classifyTriangle('3', '4', '5'), 'InvalidInput',
                         '3, 4, 5 are not strings not ints')
        self.assertRaises(TypeError, classifyTriangle, 1, 2)
        self.assertRaises(TypeError, classifyTriangle, True, 'A')
        self.assertEqual(classifyTriangle(3, 0, 5), 'InvalidInput',
                         '0 as an input is invalid')
        self.assertEqual(classifyTriangle(3, 3, 5.2), 'InvalidInput',
                         'Only integers number are valid')

    # Test that make sure a triangle is a Right triangle
    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3, 4, 5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right',
                         '5, 12, 13 is a Right triangle')
        self.assertEqual(classifyTriangle(15, 8, 17), 'Right',
                         '15, 8, 17 is a Right triangle')
        self.assertNotEqual(classifyTriangle(1, 1, 1), 'Right',
                            '1, 1, 1 should be Equilateral triangle')

    # Test that make sure a triangle is a Scalene
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(6, 2, 5), 'Scalene',
                         '6, 2, 5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene',
                         '2, 3, 4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(9, 13, 14), 'Scalene',
                         '9, 13, 14 is a Scalene triangle')
        self.assertNotEqual(classifyTriangle(1, 1, 1), 'Scalene',
                            '1, 1, 1 should be Equilateral triangle')

    # Test that make sure a triangle is a Equilateral
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral',
                         '1, 1, 1 should be equilateral')
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral',
                         '4, 4, 4 should be equilateral')
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral',
                         '7, 7, 7 should be equilateral')

    # Test that make sure a triangle is a Isosceles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(4, 4, 2), 'Isoceles',
                         '4, 4, 2 should be Isoceles')
        self.assertEqual(classifyTriangle(5, 2, 5), 'Isoceles',
                         '5, 2, 5 should be Isoceles')

    # Test if the input is a valid triangle
    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle',
                         'This is not a valid triangle')
        self.assertEqual(classifyTriangle(2, 10, 4), 'NotATriangle',
                         'This is not a valid triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
