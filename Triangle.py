# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""


def classifyTriangle(a: int, b: int, c: int) -> str:
    # Validate that the inputs are ints
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # All the sides needs to be a positive int bigger than 0
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # We make sure that the triangle is valid
    if not (a + b > c and b + c > a and c + a > b):
        return 'NotATriangle'

    # We sorted the entries to make sure that c is the largest one
    a, b, c = sorted([a, b, c])

    # now we know that we have a valid triangle
    if a == b == c:
        return 'Equilateral'
    elif pow(a, 2) + pow(b, 2) == pow(c, 2):
        return 'Right'
    elif a != b != c:
        return 'Scalene'
    else:
        return 'Isoceles'
