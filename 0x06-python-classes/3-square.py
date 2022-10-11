#!/usr/bin/python3
"""
Define a Square
"""


class Square:
    """
    Private attribute: size
    """

    def __init__(self, size=0):
        """
        initalizes size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """
    Returns area of Square
    """

    def area(self):
        return self.__size ** 2
