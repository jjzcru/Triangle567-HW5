# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""

import unittest

from triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    """Test triangle program"""

    def test_input_in_triangle(self):
        """Test valid inputs in the function"""
        self.assertEqual(classify_triangle('3', '4', '5'), 'InvalidInput',
                         '3, 4, 5 are not strings not ints')
        self.assertRaises(TypeError, classify_triangle, 1, 2)
        self.assertRaises(TypeError, classify_triangle, True, 'A')
        self.assertEqual(classify_triangle(3, 0, 5), 'InvalidInput',
                         '0 as an input is invalid')
        self.assertEqual(classify_triangle(3, 3, 5.2), 'InvalidInput',
                         'Only integers number are valid')

    def test_right_triangle(self):
        """Test that make sure a triangle is a Right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3, 4, 5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right',
                         '5, 12, 13 is a Right triangle')
        self.assertEqual(classify_triangle(15, 8, 17), 'Right',
                         '15, 8, 17 is a Right triangle')
        self.assertNotEqual(classify_triangle(1, 1, 1), 'Right',
                            '1, 1, 1 should be Equilateral triangle')

    def test_scalene_triangle(self):
        """Test that make sure a triangle is a Scalene"""
        self.assertEqual(classify_triangle(6, 2, 5), 'Scalene',
                         '6, 2, 5 is a Scalene triangle')
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene',
                         '2, 3, 4 is a Scalene triangle')
        self.assertEqual(classify_triangle(9, 13, 14), 'Scalene',
                         '9, 13, 14 is a Scalene triangle')
        self.assertNotEqual(classify_triangle(1, 1, 1), 'Scalene',
                            '1, 1, 1 should be Equilateral triangle')

    def test_equilateral_triangles(self):
        """Test that make sure a triangle is a Equilateral"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral',
                         '1, 1, 1 should be equilateral')
        self.assertEqual(classify_triangle(4, 4, 4), 'Equilateral',
                         '4, 4, 4 should be equilateral')
        self.assertEqual(classify_triangle(7, 7, 7), 'Equilateral',
                         '7, 7, 7 should be equilateral')

    def test_isosceles_triangles(self):
        """Test that make sure a triangle is a Isosceles"""
        self.assertEqual(classify_triangle(4, 4, 2), 'Isoceles',
                         '4, 4, 2 should be Isoceles')
        self.assertEqual(classify_triangle(5, 2, 5), 'Isoceles',
                         '5, 2, 5 should be Isoceles')

    def test_invalid_triangle(self):
        """ Test if the input is a valid triangle """
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle',
                         'This is not a valid triangle')
        self.assertEqual(classify_triangle(2, 10, 4), 'NotATriangle',
                         'This is not a valid triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
