# -*- coding: utf-8 -*-
"""
@author: Jose J. Cruz
"""


def classify_triangle(first_side: int, second_side: int,
                      third_side: int) -> str:
    """Validate that the inputs are ints"""
    if not (isinstance(first_side, int) and
            isinstance(second_side, int) and isinstance(third_side, int)):
        return 'InvalidInput'

    # All the sides needs to be a positive int bigger than 0
    if first_side <= 0 or second_side <= 0 or third_side <= 0:
        return 'InvalidInput'

    # We make sure that the triangle is valid
    if not (
            first_side + second_side > third_side and second_side +
            third_side > first_side and third_side + first_side > second_side):
        return 'NotATriangle'

    # We sorted the entries to make sure that c is the largest one
    first_side, second_side, third_side = sorted(
        [first_side, second_side, third_side])

    triangle_type: str = 'Isoceles'

    # now we know that we have a valid triangle
    if first_side == second_side == third_side:
        triangle_type = 'Equilateral'
    elif pow(first_side, 2) + pow(second_side, 2) == pow(third_side, 2):
        triangle_type = 'Right'
    elif first_side != second_side != third_side:
        triangle_type = 'Scalene'

    return triangle_type
