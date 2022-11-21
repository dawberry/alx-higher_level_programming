#!/usr/bin/python3
"""
module to calculate sum of integer
"""

def add_integer(a, b):
    """
    the function adds a and b
    Returns: the sum of two numbers

    """
    typeof = [int, float]

    if type(a) not in typeof:
        raise TypeError("a must be an integer")

    if type(b) not in typeof:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
